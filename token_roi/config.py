import os

CONF_PATH = '/.local/token/'
CONF_TOKENS = 'token_list.txt'
CONF_WALLETS = 'eth_wallets.txt'
CONF_CONTENT = """
# token_roi configuration file
# <TOKEN ID> <YOUR ICO PRICE> <AMOUNT OF COINS>
# for example
# WPR 0.000125 1000
"""


def config_dir():
    home_dir = os.getenv("HOME")
    abs_path = home_dir + CONF_PATH
    return abs_path


def token_config_path():
    return config_dir() + CONF_TOKENS


def wallet_config_path():
    return config_dir() + CONF_WALLETS
