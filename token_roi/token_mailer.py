import json
import smtplib
from token_roi.config import *


def sendemail(from_addr, to_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems


def send_stats(message):
    conf = json.load(open(config_dir() + EMAIL_CONF, 'r'))
    sendemail(from_addr=conf['user'],
              to_addr_list=conf['to'],
              subject='token_roi',
              message=message,
              login=conf['user'],
              password=conf['password'],
              smtpserver=conf['server'])