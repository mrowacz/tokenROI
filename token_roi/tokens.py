import logging
from token_roi.config import *


def initialize_configuration():
    create_config_dir()
    init_config(token_config_path(), TOKEN_CONF_CONTENT)
    init_config(wallet_config_path(), WALLETS_CONF_CONTENT)
    init_config(config_dir() + EMAIL_CONF, EMAIL_CONF_CONTENT)
    logging.info("Configuration initialized")


def create_config_dir():
    try:
        logging.debug("Create dir " + config_dir())
        os.makedirs(config_dir())
    except FileExistsError:
        logging.error(config_dir() + ' already exists')


def init_config(file, content):
    with open(file, 'w') as f:
        f.write(content)
