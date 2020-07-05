import configparser
import os

config = configparser.ConfigParser()
config.read("config.ini")

is_dev = False

if os.environ.get("APP_MODE") is None or os.environ.get("APP_MODE") == "DEV":
    is_dev = True

formatted_data_path = config["Routes"]["FilePath"]
database_store_path = config["Routes"]["DataBasePath"]
# If the mode is developement, then change these variables.


if is_dev:
    database_store_path = ":memory:"
