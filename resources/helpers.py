import os
from pathlib import Path

import tomli


class Helpers:
    """"
    Reusable helper functions
    """
    _instance = None

    # Simple Singleton implementation
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Helpers, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.conf_path = os.path.join(str(Path(__file__).parent.parent), 'config.toml')
        with open(self.conf_path, 'rb') as file:
            self.data = tomli.load(file)
            print(self.data)

    def get_data(self, entity, username):
        return self.data[entity].get(username, None)


helpers = Helpers()
