"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from PartNLP.models.validators.validator import Validator
from PartNLP.models.helper.constants import SUPPORTED_MULTI_PROCESS_STATUS
from PartNLP.models.helper.color import Color


class MultiProcessValidator(Validator):
    """
        PROCESSORS VALIDATOR
    """
    def __init__(self, config):
        super().__init__(config)
        self.supported_multi_process_status = SUPPORTED_MULTI_PROCESS_STATUS

    def isvalid(self):
        return self.is_name_valid()

    def is_name_valid(self):
        """
        Returns:
        """
        # Check if whether multiprocess type is supported or not.
        if self.config['multiProcessType'] not in self.supported_multi_process_status:
            return False, f'{Color.fail}{self.config["multiProcessType"]}{Color.endc}' \
                          f' multiProcessType is not supported. ' \
                          f'List of supported multiProcessTypes : {Color.header}' \
                          f'{self.supported_multi_process_status}{Color.endc}', \
                           self.config['multiProcessType']
        return True, '', None

    def update_config_value(self, name, old_value, new_value):
        # Add new value to empty operations list
        self.config['multiProcessType'] = new_value

    def get_dependencies(self):
        return []
