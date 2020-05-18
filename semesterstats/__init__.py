import configparser
import os
import glob
from .logging import AppLog
from .parser import parse_into_database
from .api import App

config = configparser.ConfigParser()
config.read("config.ini")

try:
    os.mkdir("imported")
except FileExistsError:
    AppLog.info("imported Folder is present, Skipping...")

try:
    os.mkdir("FormattedData")
except FileExistsError:
    AppLog.info("FormattedData Folder is present, Skipping...")

filenames = glob.glob("FormattedData/*.csv")

for f in filenames:
    parse_into_database(f)

__all__ = ["App"]
