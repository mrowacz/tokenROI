import logging
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from config import *


def upload_file(gdrive, file):
    """
    :type gdrive: GoogleDrive
    :param file: String
    """
    drive_list = gdrive.ListFile(
        {'q': "'root' in parents and trashed=false"}
    ).GetList()
    file_list = list(filter(lambda x: x['title'] == file,
                            drive_list))
    fhandler = None
    print(file_list)
    if not file_list:
        fhandler = gdrive.CreateFile({'id': file})
        print('empty')
    else:
        fhandler = file_list[0]

    fhandler.SetContentFile(config_dir() + file)
    fhandler.Upload()


def upload_configs():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    logging.info("Uploading " + TOKEN_CONF)
    upload_file(drive, TOKEN_CONF)
    logging.info("Uploading " + WALLETS_CONF)
    upload_file(drive, WALLETS_CONF)
