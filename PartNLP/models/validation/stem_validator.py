"""
This class checks all requirements should be passed by stemmer.
"""
from PartNLP.models.validation.validator import Validator


class StemValidator(Validator):
    def __init__(self, config):
        self.config = config

    def isvalid(self):
        """
        :return:
        """
        return True, '', None

    def get_dependencies(self):
        return ['S_TOKENIZE', 'W_TOKENIZE']
