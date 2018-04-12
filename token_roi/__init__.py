import json
import editor
import requests
from token_roi.tokens import *
from token_roi.arg_parser import *
from cloud import *

def handle_tokens():
    out = []
    tks = {}
    with open(token_config_path()) as f:
        conf_list = list(
            filter(lambda  x: not x == '',
                   filter(lambda x: '#' not in x,
                          map(lambda x: x.rstrip(), f.readlines())
                          )
                   )
        )
        for c in conf_list:
            token, price, amount = c.split(" ")
            tks[token] = {
                'price': float(price),
                'amount': float(amount)
            }

    r = requests.post('https://api.idex.market/returnTicker')

    assert r.status_code == 200
    idex_tickers = json.loads(r.text)

    HEADER_TEXT = '\x1b[0;30;46m'
    GREEN_TEXT = '\x1b[6;30;42m'
    RED_TEXT = '\x1b[1;37;40m'
    END_SIGN = '\x1b[0m'

    header_format = "{:<10} {:<14} {:<14} {:<14} {:<14}"
    print(HEADER_TEXT + header_format.format(
        "TOKEN", "ICO PRICE", "LAST", "ROI", "TOTAL"
    ) + END_SIGN)

    for token in sorted(tks):
        key_str = "ETH_" + token

        if not key_str in idex_tickers or str(
                idex_tickers[key_str]['last']) == 'N/A':
            continue

        t_price = tks[token]['price']
        t_amount = tks[token]['amount']
        ico_price = "{0:.8f}".format(float(t_price))
        last_price = "{0:.8f}".format(float(idex_tickers[key_str]['last']))
        total_eth = "{0:.8f}".format(t_amount * float(last_price))
        out.append(float(total_eth))
        roi_float = 100 * (float(last_price) - t_price) / t_price
        roi = "{0:.2f}%".format(roi_float)

        if roi_float > 100:
            print(
                GREEN_TEXT + header_format.format(token, ico_price, last_price,
                                                  roi, total_eth)
                + END_SIGN)
        else:
            print(RED_TEXT + header_format.format(token, ico_price, last_price,
                                                  roi, total_eth)
                  + END_SIGN)
    return out


def handle_wallets():
    out = []
    with open(wallet_config_path()) as f:
        wei = 1e-18
        data = f.readlines()
        url = "https://api.etherscan.io/api?module=account&action=balance" \
              "&address={}&tag=latest"
        for addr in list(map(lambda x: x.rstrip(), data)):
            r = requests.get(url.format(addr))
            if r.status_code == 200:
                js_r = json.loads(r.text)
                if js_r['message'] == 'OK':
                    print('{0:}: {1:.4f}'.
                          format(addr, float(js_r['result']) * wei))
                    out.append(float(js_r['result']) * wei)
    return out


def main():
    os.chdir(config_dir())
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    argv = sys.argv[1:]
    parameters = parse_token_config(argv)
    if parameters['debug']:
        logger.setLevel(level=logging.DEBUG)
        logging.debug(parameters)
    if parameters['init']:
        initialize_configuration()
        sys.exit(0)
    elif parameters['upload']:
        dbx = dropbox_start()
        dropbox_push_file(dbx, TOKEN_CONF)
        dropbox_push_file(dbx, WALLETS_CONF)
    elif parameters['restore']:
        dbx = dropbox_start()
        dropbox_restore_file(dbx, TOKEN_CONF,
                             rev=select_revision(dbx, TOKEN_CONF))
        dropbox_restore_file(dbx, WALLETS_CONF,
                             rev=select_revision(dbx, WALLETS_CONF))
    elif parameters['edit']:
        editor.edit(filename=token_config_path(), use_tty=True)
        editor.edit(filename=wallet_config_path(), use_tty=True)
    else:
        sum_eth = 0
        sum_eth += sum(handle_tokens())
        if parameters['all']:
            sum_eth += sum(handle_wallets())
            print("eth sum: {0:.2f}".format(sum_eth))
