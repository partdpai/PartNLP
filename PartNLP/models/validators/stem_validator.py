"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from PartNLP.models.validators.validator import Validator


class StemValidator(Validator):
    """
            STEM VALIDATOR
    """
    def __init__(self, config):
        super(StemValidator, self).__init__(config)
        self.config = config

    def isvalid(self):
        """
        :return:
        """
        return True, '', None

    def get_dependencies(self):
        return ['s_tokenize', 'w_tokenize']
