"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from PartNLP.models.validation.validator import Validator


class SentValidator(Validator):
    def __init__(self, config):
        super(SentValidator, self).__init__(config)

    def isvalid(self):
        """
        :param :
        :return:
        """
        return self.is_name_valid()

    def is_name_valid(self):
        return True, '', None

    def get_dependencies(self):
        return []
