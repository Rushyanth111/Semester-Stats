import configparser
import csv
import logging
import re
from timeit import default_timer as timer

import uvicorn

from Parser.ParsingLogic import ParseIntoDatabase
from Routes.MainRouter import App

# Set up:
config = configparser.ConfigParser()
config.read("config.ini")

filenames = [
    "FormattedData/Data-CS-2016-2015-6.csv",
    "FormattedData/Data-CS-2016-2015-7.csv",
    "FormattedData/Data-CS-2017-2017-5.csv",
]

for f in filenames:
    ParseIntoDatabase(f)

#uvicorn.run(App, host="127.0.0.1", port=5000, log_level="debug")
