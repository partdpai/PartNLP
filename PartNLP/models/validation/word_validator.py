"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
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
