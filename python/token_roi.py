import json
import os
import editor
import requests
import sys
import logging
from token_roi.tokens import TokenArguments
from token_roi.wallets import WalletArguments


def handle_tokens():
    out = []
    tokens = {}
    with open(TokenArguments.get_config_path()) as f:
        conf_list = list(map(lambda x: x.rstrip(), f.readlines()))
        for c in conf_list:
            token, price, amount = c.split(" ")
            tokens[token] = {
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

    for token in sorted(tokens):
        key_str = "ETH_" + token

        if not key_str in idex_tickers or str(
                idex_tickers[key_str]['last']) == 'N/A':
            continue

        t_price = tokens[token]['price']
        t_amount = tokens[token]['amount']
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
    with open(WalletArguments.get_config_path()) as f:
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
                          format(addr, float(js_r['result'])*wei))
                    out.append(float(js_r['result'])*wei)
    return out


if __name__ == "__main__":
    os.chdir(TokenArguments.get_path())
    logging.basicConfig(level=logging.FATAL)
    argv = sys.argv[1:]
    parameters = TokenArguments.parse(argv)
    if parameters['debug']:
        logging.basicConfig(level=logging.DEBUG)
    logging.debug("parameters " + str(parameters))
    if parameters['init']:
        TokenArguments.handle_init()
    elif parameters['upload']:
        TokenArguments.handle_upload()
    elif parameters['edit']:
        editor.edit(filename=TokenArguments.get_config_path(), use_tty=True)
    else:
        sum_eth = 0
        sum_eth += sum(handle_tokens())
        if parameters['all']:
            sum_eth += sum(handle_wallets())
            print("eth sum: {0:.2f}".format(sum_eth))
