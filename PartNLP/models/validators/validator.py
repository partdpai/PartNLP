"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""


class Validator:
    """
        VALIDATOR
    """
    def __init__(self, config):
        self.config = config

    def isvalid(self):
        """
        :return: True or False, error_message
        """
        pass

    def prepare_input_value(self):
        """
        Returns:
        """
        pass

    def update_config_value(self, name, old_value, new_value):
        """
        Args:
            name:
            old_value:
            new_value:
        Returns:
        """
        self.config[name] = new_value

    def get_dependencies(self):
        return []
