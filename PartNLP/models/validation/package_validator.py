"""
This class validates all requirements should be passed by package.
"""
from PartNLP.models.helper.color import Color
from PartNLP.models.validation.validator import Validator
from PartNLP.models.helper.constants import NAME_OF_SUPPORTED_PACKAGES
from pathlib import Path
import stanza
import json
import os


class PackageValidator(Validator):
    def __init__(self, config):
        super().__init__(config)

    def isvalid(self):
        success, message, val = True, '', None
        success, message, val = self.is_name_valid()
        if success:
            return self.check_install_resources()
        else:
            return success, message, val

    def is_name_valid(self):
        # Check whether package selected.
        if not self.config['package']:
            return False, f'{Color.FAIL}Warning:{Color.ENDC} no package selected. List of supported package:' \
                          f'{Color.HEADER}{NAME_OF_SUPPORTED_PACKAGES}{Color.ENDC}', self.config['Language']
        self.prepare_input_value()
        if self.config['package'] not in NAME_OF_SUPPORTED_PACKAGES:
            package = self.config['package']
            return False, f'{package} is not supported. List of supported packages: ' \
                          f'{NAME_OF_SUPPORTED_PACKAGES}', package
        return True, '', None

    def check_install_resources(self):
        if self.config['package'] == 'STANZA':
            HOME_DIR = str(Path.home())
            DEFAULT_MODEL_DIR = os.getenv('STANZA_RESOURCES_DIR', os.path.join(HOME_DIR, 'stanza_resources/'))
            dir = DEFAULT_MODEL_DIR
            # rename persian language to fa and use dir = dir + self.config['Language']
            dir = dir + 'fa'
            if not os.path.isdir(dir):
                lang = self.config['Language']
                return False, f'stanza needs {Color.HEADER}{lang} resource. do you want to install(y, n){Color.ENDC}', \
                       'install_resource'
        return True, '', None

    def prepare_input_value(self):
        self.config['package'] = self.config['package'].upper()

    def update_config_value(self, name, old_value, new_value):
        if old_value == 'install_resource':
            if new_value == 'y':
                stanza.download('fr')
            else:
                raise Exception('you can not run this package without the resources')
        else:
            self.config['package'] = new_value

    def get_dependencies(self):
        return []
