"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from PartNLP.models.helper.color import Color
from PartNLP.models.validation.validator import Validator
from PartNLP.models.helper.constants import \
    NAME_OF_SUPPORTED_PACKAGES, EQUIVALENT_LANGUAGES_TO_STANZA
from pathlib import Path
import stanza
import os


class PackageValidator(Validator):
    """
            PACKAGE VALIDATOR
    """
    def __init__(self, config):
        super().__init__(config)

    def isvalid(self):
        success, message, val = self.is_name_valid()
        if success:
            return self.check_install_resources()
        else:
            return success, message, val

    def is_name_valid(self):
        # Check whether package selected.
        if not self.config['package']:
            return False, f'{Color.fail}Warning:{Color.endc} ' \
                          f'no package selected. List of supported package:' \
                          f'{Color.header}{NAME_OF_SUPPORTED_PACKAGES}' \
                          f'{Color.endc}', self.config['Language']
        self.prepare_input_value()
        if self.config['package'] not in NAME_OF_SUPPORTED_PACKAGES:
            package = self.config['package']
            return False, f'{package} is not supported. List of supported packages: ' \
                          f'{NAME_OF_SUPPORTED_PACKAGES}', package
        return True, '', None

    def check_install_resources(self):
        if self.config['package'] == 'STANZA':
            home_dir = str(Path.home())
            default_model_dir = os.getenv('STANZA_RESOURCES_DIR',
                                          os.path.join(home_dir, 'stanza_resources/'))
            directory = default_model_dir
            directory = directory + EQUIVALENT_LANGUAGES_TO_STANZA[
                self.config['Language'].upper()]
            if not os.path.isdir(directory):
                lang = self.config['Language']
                return False, f'stanza needs {Color.header}{lang} ' \
                              f'resource. do you want to install(y, n){Color.endc}', \
                              'install_resource'
        return True, '', None

    def prepare_input_value(self):
        self.config['package'] = self.config['package'].upper()

    def update_config_value(self, name, old_value, new_value):
        if old_value == 'install_resource':
            if new_value == 'y':
                stanza.download(EQUIVALENT_LANGUAGES_TO_STANZA[self.config['Language']])
            else:
                raise Exception('you can not run this package without the resources')
        else:
            self.config['package'] = new_value

    def get_dependencies(self):
        return []
