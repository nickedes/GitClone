from configparser import ConfigParser
from github import Github


def getPass():
    """Returns the username and password stored in the config file."""
    config = ConfigParser()
    config.read('config.ini')
    user, passwd = config['Github']['user'], config['Github']['pass']
    return user, passwd


def connect():
    """Creates a Github instance so that we can access Github api."""
    user, passwd = getPass()
    return Github(user, passwd)
