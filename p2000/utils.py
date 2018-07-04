import json


def load_config():
    """
    Load the config file as JSON.
    :return: The config file as JSON.
    """
    with open('./resources/config.json') as f:
        return json.load(f)