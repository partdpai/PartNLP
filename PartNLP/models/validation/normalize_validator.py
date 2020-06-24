"""
This class validates all requirements should be passed by normalize class.
"""
from PartNLP.models.validation.validator import Validator


class NormalizeValidator(Validator):
    def __init__(self, config):
        # self.package = config['package']
        self.config = config

    def isvalid(self):
        """
        :return: True or False, error_message
        """
        return True, '', None

    def get_dependencies(self):
        return []
