import os
import json
import requests

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

    header_format = "{:<10} {:<14} {:<14} {:<5}"
    print(header_format.format("TOKEN", "ICO PRICE", "LAST", "ROI"))

    for token in tokens:
        key_str = "ETH_" + token

        if not key_str in idex_tickers:
            continue
            
        ico_price = "{0:.8f}".format(float(tokens[token]))
        last_price = "{0:.8f}".format(float(idex_tickers[key_str]['last']))
        roi = "{0:.2f}%".format(100 * (float(last_price) - tokens[token])/tokens[token])
        print(header_format.format(token, ico_price, last_price, roi))
