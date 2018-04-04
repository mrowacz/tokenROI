import getopt
import logging
import os
import sys
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

CONF_CONTENT = """
tests
"""


class TokenArguments:
    CONF_PATH = '/.local/token/'
    CONF_NAME = 'token_list.txt'

    @staticmethod
    def parse(argv):
        out = {
            "debug": False,
            "init": False,
            "upload": False,
            "fetch": False
        }
        help_string = """
How to use:
--init initialize config in ${HOME}/.local/token/token_list.txt
--upload to google disk
"""
        try:
            opts, args = getopt.getopt(argv, "hi:u:f:d:",
                                       ["init", "upload", 'fetch', 'debug'])
        except getopt.GetoptError:
            print(help_string)
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print(help_string)
                sys.exit()
            elif opt in ("-i", "--init"):
                out['init'] = True
            elif opt in ("-u", "--upload"):
                out['upload'] = True
            elif opt in ("-f", "--fetch"):
                out['fetch'] = True
            elif opt in ("-d", "--debug"):
                out['debug'] = True
        return out

    @staticmethod
    def get_path():
        home_dir = os.getenv("HOME")
        abs_path = home_dir + TokenArguments.CONF_PATH
        return abs_path

    @staticmethod
    def get_config_path():
        dir_path = TokenArguments.get_path()
        return dir_path + TokenArguments.CONF_NAME

    @staticmethod
    def handle_init():
        abs_path = TokenArguments.get_path()
        try:
            os.makedirs(abs_path)
            with open(TokenArguments.get_config_path(), 'w') as f:
                f.write(CONF_CONTENT)
        except FileExistsError:
            logging.error(abs_path + ' already exists')
        print('Configuration initialized!')
        sys.exit(0)
        pass

    @staticmethod
    def handle_upload():
        print( os.getcwd())
        global gauth, drive
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)
        file_list = drive.ListFile(
            {'q': "'root' in parents and trashed=false"}).GetList()
        print(file_list)