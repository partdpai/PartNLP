"""This class validates all requriements should be passed by language.
"""
from PartNLP.models.helper.color import Color
from PartNLP.models.validation.validator import Validator
from PartNLP.models.helper.constants import NAME_OF_SUPPORTED_LANGUAGES
from PartNLP.models.helper.constants import SUPPORTED_LANGUAGES_TO_PACKAGES


class LanguageValidator(Validator):
    def __init__(self, config):
        self.config = config

    def isvalid(self):
        self.prepare_input_value()
        # Check whether language selected or not
        if not self.config['Language']:
            return False, f'{Color.FAIL}Warning:{Color.ENDC} no language selected. List of supported languages:' \
                          f'{Color.HEADER}{NAME_OF_SUPPORTED_LANGUAGES}{Color.ENDC}', self.config['Language']
        if self.config['Language'] not in NAME_OF_SUPPORTED_LANGUAGES:
            language = self.config['Language']
            return False, f'{Color.BLUE}{language}{Color.ENDC} is not supported. List of supported languages:' \
                          f'{Color.HEADER}{NAME_OF_SUPPORTED_LANGUAGES}{Color.ENDC}', self.config['Language']
        # check valid language for package.
        if self.config['package'] not in SUPPORTED_LANGUAGES_TO_PACKAGES[self.config['Language']]:
            package, language = self.config['package'], self.config['Language']
            return False, f'{Color.FAIL}{package}{Color.ENDC} ' \
                          f'package is not supported for {Color.FAIL}{language}{Color.ENDC} language.', \
                          self.config['Language']
        return True, '', self.config['Language']

    def prepare_input_value(self):
        self.config['Language'] = self.config['Language'].upper()

    def get_dependencies(self):
        return []
