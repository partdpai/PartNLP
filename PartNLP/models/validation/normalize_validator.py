"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from PartNLP.models.validation.validator import Validator


class NormalizeValidator(Validator):
    def __init__(self, config):
        """
        Args:
            config:
        """
        super(NormalizeValidator, self).__init__(config)
        self.config = config

    def isvalid(self):
        """
        :return: True or False, error_message
        """
        return True, '', None

    def get_dependencies(self):
        return []
