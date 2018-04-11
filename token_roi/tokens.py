import logging
from token_roi.config import *


def initialize_configuration():
    create_config_dir()
    token_config_init()
    wallet_config_init()
    logging.info("Configuration initialized")


def create_config_dir():
    try:
        logging.debug("Create dir " + config_dir())
        os.makedirs(config_dir())
    except FileExistsError:
        logging.error(config_dir() + ' already exists')


def token_config_init():
    with open(token_config_path(), 'w') as f:
        f.write(TOKEN_CONF_CONTENT)


def wallet_config_init():
    with open(wallet_config_path(), 'w') as f:
        f.write(WALLETS_CONF_CONTENT)

