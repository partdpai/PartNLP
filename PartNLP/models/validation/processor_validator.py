"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from PartNLP.models.validation.validator import Validator
from PartNLP.models.helper.constants import SUPPORTED_PROCESSORS_FOR_PACKAGES
from PartNLP.models.helper.color import Color


class ProcessorsValidator(Validator):
    """
        PROCESSORS VALIDATOR
    """
    def __init__(self, config):
        super().__init__(config)
        self.supported_operations = SUPPORTED_PROCESSORS_FOR_PACKAGES[self.config['package']]

    def isvalid(self):
        return self.is_name_valid()

    def is_name_valid(self):
        self.prepare_input_value()

        # Check if processors is empty.
        if not self.config['processors']:
            return False, f'{Color.fail}Warning{Color.endc} ' \
                          f'No operator selected. List of supported operations:' \
                          f'{Color.header}{self.supported_operations}' \
                          f'{Color.endc}', self.config['processors']
        # Check if whether operators of the processor are supported or not.
        for p in self.config['processors']:
            if p not in self.supported_operations:
                return False, f'{Color.fail}{p}{Color.endc} Operator is not supported. ' \
                              f'List of supported operators : {Color.header}' \
                              f'{self.supported_operations}{Color.endc}', p
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
