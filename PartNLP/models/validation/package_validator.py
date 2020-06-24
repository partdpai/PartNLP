"""
This class validates all requirements should be passed by package.
"""
from PartNLP.models.helper.color import Color
from PartNLP.models.validation.validator import Validator
from PartNLP.models.helper.constants import NAME_OF_SUPPORTED_PACKAGES


class PackageValidator(Validator):
    def __init__(self, config):
        super().__init__(config)

    def isvalid(self):
        return self.is_name_valid()

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

    def prepare_input_value(self):
        self.config['package'] = self.config['package'].upper()

    def update_config_value(self, name, old_value, new_value):
        self.config['package'] = new_value

    def get_dependencies(self):
        return []
