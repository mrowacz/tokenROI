import logging

import sys
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from config import *


def token_config_init():
    try:
        os.makedirs(config_dir())
        with open(token_config_path(), 'w') as f:
            f.write(CONF_CONTENT)
    except FileExistsError:
        logging.error(config_dir() + ' already exists')
    print('Configuration initialized!')
    sys.exit(0)


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