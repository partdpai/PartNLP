"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from PartNLP.models.validation.validator import Validator
from PartNLP.models.helper.constants import SUPPORTED_PROCESSORS_FOR_PACKAGES
from PartNLP.models.helper.color import Color


class ProcessorsValidator(Validator):
    def __init__(self, config):
        super().__init__(config)
        self.supported_operations = SUPPORTED_PROCESSORS_FOR_PACKAGES[self.config['package']]

    def isvalid(self):
        return self.is_name_valid()

    def is_name_valid(self):
        self.prepare_input_value()

        # Check if processors is empty.
        if not self.config['processors']:
            return False, f'{Color.FAIL}Warning{Color.ENDC} No operator selected. List of supported operations:' \
                          f'{Color.HEADER}{self.supported_operations}{Color.ENDC}', self.config['processors']
        # Check if whether operators of the processor are supported or not.
        for p in self.config['processors']:
            if p not in self.supported_operations:
                return False, f'{Color.FAIL}{p}{Color.ENDC} Operator is not supported. ' \
                              f'List of supported operators : {Color.HEADER}{self.supported_operations}{Color.ENDC}', p
        return True, '', None
    
    def update_config_value(self, name, old_value, new_value):
        # Add new value to empty processors list
        if not self.config['processors']:
            self.config['processors'].append(new_value)
        # Assign new value to the old one
        else:
            idx = self.config['processors'].index(old_value)
            self.config['processors'][idx] = new_value

    def prepare_input_value(self):
        for p in self.config['processors']:
            p = p.upper()

    def get_dependencies(self):
        dependencies = self.config['processors']
        return dependencies
