import logging

AppLog = logging.Logger("AppLogger", level=logging.DEBUG)
AppLog.addHandler(logging.StreamHandler())
