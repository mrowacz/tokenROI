import sys
import logging
from token_roi.config import *
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

BACKUPPATH = '/TokenRoi/'


def select_revision(dropbox, file):
    print("Finding available revisions on Dropbox...")
    entries = dropbox.files_list_revisions(BACKUPPATH + file, limit=30).entries
    revisions = sorted(entries, key=lambda entry: entry.server_modified)
    return revisions[-1].rev


def dropbox_push_file(dropbox, file):
    """
    :type dropbox: Dropbox
    :param file: String
    """
    with open(config_dir() + file, 'rb') as f:
        logging.info("Uploading " + file + " to Dropbox as " +
                     BACKUPPATH + "...")
        try:
            dropbox.files_upload(f.read(), BACKUPPATH + file,
                                 mode=WriteMode('overwrite'))
        except ApiError as err:
            if (err.error.is_path() and
                    err.error.get_path().reason.is_insufficient_space()):
                logging.error("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                logging.error(err.user_message_text)
                sys.exit(-1)
            else:
                logging.error(err)
                sys.exit(-1)


def dropbox_restore_file(dropbox, file, rev=None):
    logging.info("Restoring " + BACKUPPATH + file + " to revision "
                 + str(rev) + " on Dropbox...")
    dropbox.files_restore(BACKUPPATH + file, rev)
    logging.info(
        "Downloading current " + BACKUPPATH + " from Dropbox, overwriting " +
        config_dir() + file + "...")
    dropbox.files_download_to_file(config_dir() + file, BACKUPPATH + file, rev)


def dropbox_start():
    token = None
    with open(dropbox_config_path(), 'r') as f:
        token = f.readline().rstrip()

    if len(token) == 0:
        logging.error("ERROR: Looks like you didn't add your access token. "
                      "Open up backup-and-restore-example.py in a text editor and "
                      "paste in your token in line 14.")

    print("Creating a Dropbox object...")
    dbx = dropbox.Dropbox(token)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        logging.error("ERROR: Invalid access token; try re-generating an "
                      "access token from the app console on the web.")
        sys.exit(-1)
    return dbx
