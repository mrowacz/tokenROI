import json
import requests
from termcolor import colored

if __name__ == "__main__":

    tokens = {}
    with open("token_list.txt") as f:
        conf_list = list(map(lambda x: x.rstrip(), f.readlines()))
        for c in conf_list:
            token, price = c.split(" ")
            tokens[token] = float(price)

    r = requests.post('https://api.idex.market/returnTicker')

    assert r.status_code == 200
    idex_tickers = json.loads(r.text)

    HEADER_TEXT = '\x1b[0;30;46m'
    GREEN_TEXT = '\x1b[6;30;42m'
    RED_TEXT = '\x1b[1;37;40m'
    END_SIGN = '\x1b[0m'

    header_format = "{:<10} {:<14} {:<14} {:<5}"
    print(HEADER_TEXT + header_format.format("TOKEN", "ICO PRICE", "LAST", "ROI") + END_SIGN)

    for token in tokens:
        key_str = "ETH_" + token

        if not key_str in idex_tickers or str(idex_tickers[key_str]['last']) == 'N/A':
            continue

        ico_price = "{0:.8f}".format(float(tokens[token]))
        last_price = "{0:.8f}".format(float(idex_tickers[key_str]['last']))
        roi_float = 100 * (float(last_price) - tokens[token])/tokens[token]
        roi = "{0:.2f}%".format(roi_float)

        if roi_float > 100:
            print(GREEN_TEXT + header_format.format(token, ico_price, last_price, roi) + END_SIGN)
        else:
            print(RED_TEXT + header_format.format(token, ico_price, last_price, roi) + END_SIGN)
