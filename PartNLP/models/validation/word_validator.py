"""
This class checks all requirements should be passed by word_tokenize.
"""
from PartNLP.models.validation.validator import Validator


class WordValidator(Validator):
    def __init__(self, config):
        pass

    def isvalid(self):
        """
        :return:
        """
        return True, '', None

    def get_dependencies(self):
        return ['S_TOKENIZE']
