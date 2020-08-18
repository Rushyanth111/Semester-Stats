import configparser

config = configparser.ConfigParser()
config.read("config.ini")

is_dev = False

formatted_data_path = config["Routes"]["FilePath"]
database_store_path = config["Routes"]["DataBasePath"]
developer_app_mode = config["Developer"]["ApplicationMode"]
# If the mode is developement, then change these variables.

if developer_app_mode == "Dev":
    database_store_path = ":memory:"
    is_dev = True
