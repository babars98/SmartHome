import os
from configparser import ConfigParser

script_directory = os.path.dirname(__file__)
file_path = os.path.join(os.path.dirname(script_directory), 'config.ini')

config = ConfigParser()
config.read(file_path)

def getconfig():
    return config