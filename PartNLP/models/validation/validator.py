"""
This class makes a structure for its children to validate themselves.
"""


class Validator:
    def __init__(self, config):
        self.config = config

    def isvalid(self):
        """
        :return: True or False, error_message
        """
        pass

    def prepare_input_value(self):
        pass

    def update_config_value(self, name, old_value, new_value):
        self.config[name] = new_value

    def get_dependencies(self):
        return []
