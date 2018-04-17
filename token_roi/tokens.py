import logging
from token_roi.config import *


def yes_no_dialog(msg):
    assert isinstance(msg, str)
    cnt = 0
    while True:
        if cnt > 10:
            return False
        text = input(msg + ' Y/N')
        if text in ['Y', 'N']:
            return True if text == 'Y' else False
        cnt += 1


def init_dropbox():
    choice = yes_no_dialog('Would you like to init dropbox')
    if choice:
        key = input('Enter dropbox key: ')
        init_config(dropbox_config_path(), key)


def initialize_configuration():
    create_config_dir()
    init_config(token_config_path(), TOKEN_CONF_CONTENT)
    init_config(wallet_config_path(), WALLETS_CONF_CONTENT)
    init_config(config_dir() + EMAIL_CONF, EMAIL_CONF_CONTENT)
    init_dropbox()
    logging.info("Configuration initialized")


def create_config_dir():
    try:
        logging.debug("Create dir " + config_dir())
        os.makedirs(config_dir())
    except FileExistsError:
        logging.info(config_dir() + ' already exists')


def init_config(file, content):
    with open(file, 'w') as f:
        f.write(content)
    print('Initialized config: ' + file)
