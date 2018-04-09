import logging
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
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


def token_config_upload():
    print( os.getcwd())
    global gauth, drive
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    file_list = drive.ListFile(
        {'q': "'root' in parents and trashed=false"}).GetList()
    file_list = list(filter(lambda x: x['title'] == 'token_list.txt',
                            file_list))
    file_list[0].SetContentFile(token_config_path())
    file_list[0].Upload()