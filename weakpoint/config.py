
import yaml

from weakpoint.exceptions import ConfigException
from weakpoint.fs import File


class Config(dict):
    def __init__(self, string):
        super(Config, self).__init__()

        try:
            self.update(yaml.load(string))
        except yaml.YAMLError:
            raise ConfigException('YAML Error')
        except:
            raise ConfigException('Invalid config format.')



            
