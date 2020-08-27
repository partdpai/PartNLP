"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from PartNLP.models.validation.validator import Validator


class WordValidator(Validator):
    """
            WORD VALIDATOR
    """
    def __init__(self, config):
        super(WordValidator, self).__init__(config)

    def isvalid(self):
        """
        :return:
        """
        return True, '', None

    def get_dependencies(self):
        return ['S_TOKENIZE']
