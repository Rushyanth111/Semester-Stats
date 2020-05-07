import csv
import re
from Parser.ParsingLogic import ParseIntoDatabase
from timeit import default_timer as timer

filenames = [
    "FormattedData/Data-2016-2015-6.csv",
    "FormattedData/Data-2016-2015-7.csv",
    "FormattedData/Data-2017-2017-5.csv",
]

start = timer()
for f in filenames:
    ParseIntoDatabase(f)
stop = timer()
print(start - stop, "ms")

