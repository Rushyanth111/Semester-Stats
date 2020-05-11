import configparser
import os
import glob
from .Logging import AppLog
from .Parser import ParseIntoDatabase
from .Routes import App

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
    ParseIntoDatabase(f)

__all__ = ["App"]
