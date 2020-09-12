"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from PartNLP.models.validators.validator import Validator
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
        """
        Returns:
            success, message, error_value
        """
        # Check if operations is empty.
        if not self.config['operations']:
            return False, f'{Color.fail}Warning{Color.endc} ' \
                          f'No operator selected. List of supported operations:' \
                          f'{Color.header}{self.supported_operations}' \
                          f'{Color.endc}', self.config['operations']
        # Check if whether operators of the processor are supported or not.
        for operation in self.config['operations']:
            if operation not in self.supported_operations:
                return False, f'{Color.fail}{operation}{Color.endc} Operator is not supported. ' \
                              f'List of supported operators : {Color.header}' \
                              f'{self.supported_operations}{Color.endc}', operation
        return True, '', None

    def update_config_value(self, name, old_value, new_value):
        # Add new value to empty operations list
        if not self.config['operations']:
            self.config['operations'].append(new_value)
        # Assign new value to the old one
        else:
            idx = self.config['operations'].index(old_value)
            self.config['operations'][idx] = new_value

    def get_dependencies(self):
        dependencies = self.config['operations']
        return dependencies
