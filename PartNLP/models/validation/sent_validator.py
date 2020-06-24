"""
This class checks all requirements should be passed by the sentences_tokenizer."""
from PartNLP.models.validation.validator import Validator


class SentValidator(Validator):
    def __init__(self, config):
        pass

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
