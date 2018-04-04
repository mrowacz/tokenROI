import os

class WalletArguments:
    CONF_PATH = '/.local/token/'
    CONF_NAME = 'eth_wallets.txt'

    @staticmethod
    def get_path():
        home_dir = os.getenv("HOME")
        abs_path = home_dir + WalletArguments.CONF_PATH
        return abs_path

    @staticmethod
    def get_config_path():
        dir_path = WalletArguments.get_path()
        return dir_path + WalletArguments.CONF_NAME
