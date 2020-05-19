from semesterstats import App
import uvicorn
import os
import glob
from .logging import AppLog
from .parser import parse_into_database


def main():
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
    uvicorn.run(App, port=9000)


if __name__ == "__main__":
    main()
