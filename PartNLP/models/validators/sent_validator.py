"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from PartNLP.models.validators.validator import Validator


class SentValidator(Validator):
    """
        SENTENCE VALIDATOR
    """
    def __init__(self, config):
        super(SentValidator, self).__init__(config)

    def isvalid(self):
        """
        :param :
        :return:
        """
        return self.is_name_valid()

    def is_name_valid(self):
        """
        Returns:
        """
        return True, '', None

    def get_dependencies(self):
        return []
