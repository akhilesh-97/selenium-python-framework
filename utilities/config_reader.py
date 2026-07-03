import configparser

config = configparser.ConfigParser()
config.read("config/config.ini")


def get_base_url():
    return config["DEFAULT"]["base_url"]


def get_browser():
    return config["DEFAULT"]["browser"]


def get_timeout():
    return config["DEFAULT"]["timeout"]
