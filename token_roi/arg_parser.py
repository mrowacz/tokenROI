import sys
import getopt


def parse_token_config(argv):
    out = {
        "debug": False,
        "init": False,
        "upload": False,
        "fetch": False,
        "all": False,
        "edit": False

    }
    help_string = """
How to use:
--init initialize config in ${HOME}/.local/token/
--upload to google disk
--all show all data even eth balances
"""
    try:
        opts, args = getopt.getopt(argv, "hi:u:f:d:a:e:",
                                   ["init", "upload", 'fetch', 'debug', 'all', 'edit'])
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
        elif opt in ("-a", "--all"):
            out['all'] = True
        elif opt in ("-e", "--edit"):
            out['edit'] = True
    return out
