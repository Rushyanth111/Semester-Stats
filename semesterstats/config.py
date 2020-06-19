# This module initiates all of the required modules
# and keeps them as a global access plane.
import configparser
from .models import ModelInterface


config = configparser.ConfigParser()
config.read("config.ini")

db = ModelInterface(database_name="imported/data.db")
