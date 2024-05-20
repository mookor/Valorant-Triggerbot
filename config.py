import yaml

class Config:

    def __init__(self, filename):
        with open(filename, 'r') as yaml_config:
            self.config = yaml.safe_load(yaml_config)

    def __getitem__(self, key):
        return self.config[key]
    