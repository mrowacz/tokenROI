import sys
import getopt


def parse_argv(argv):
    out = {
        "debug": False,
        "init": False,
        "upload": False,
        "restore": False,
        "all": False,
        "edit": False,
        "email": False
    }
    help_string = """
How to use:
--all show all data even eth balances
--init initialize config in ${HOME}/.local/token/
--upload to dropbox
--restore download config from dropbox
--debug enable debug messages
--email sent mail with summary
"""
    try:
        opts, args = getopt.getopt(argv, "hi:u:r:d:a:e:",
                                   ["init", "upload", 'restore', 'debug',
                                    'all', 'edit', "email"])
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
        elif opt in ("-r", "--restore"):
            out['restore'] = True
        elif opt in ("-d", "--debug"):
            out['debug'] = True
        elif opt in ("-a", "--all"):
            out['all'] = True
        elif opt in ("-e", "--edit"):
            out['edit'] = True
        elif opt in ("-m", "--email"):
            out['email'] = True
    return out
