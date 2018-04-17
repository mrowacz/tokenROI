import os

CONF_PATH = '/.local/token/'
TOKEN_CONF = 'token_list.txt'
WALLETS_CONF = 'eth_wallets.txt'
DROPBOX_CONF = 'dropbox.txt'
EMAIL_CONF = 'email.json'
TOKEN_CONF_CONTENT = """# token_roi tokens configuration file
# <TOKEN ID> <YOUR ICO PRICE> <AMOUNT OF COINS>
# for example
WPR 0.000125 1000
"""
WALLETS_CONF_CONTENT = """# token_roi tokens configuration file
# <YOUR ETH ADDRESS>
0x2a0c0DBEcC7E4D658f48E01e3fA353F44050c208
"""

EMAIL_CONF_CONTENT = """{
    "user": "<user@gmail>",
    "server": "<smtp server addr>,
    "password": "your password",
    "to": "<recipent@gmail>"
}
"""


def config_dir():
    home_dir = os.getenv("HOME")
    abs_path = home_dir + CONF_PATH
    return abs_path


def token_config_path():
    return config_dir() + TOKEN_CONF


def wallet_config_path():
    return config_dir() + WALLETS_CONF


def dropbox_config_path():
    return config_dir() + DROPBOX_CONF