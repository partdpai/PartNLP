"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from PartNLP.models.validators.validator import Validator
from PartNLP.models.helper.constants import SUPPORTED_FILE_FORMATS
from PartNLP.models.helper.color import Color


class FileFormatValidator(Validator):
    """
        PROCESSORS VALIDATOR
    """
    def __init__(self, config):
        super().__init__(config)
        self.supported_file_format = SUPPORTED_FILE_FORMATS

    def isvalid(self):
        return self.is_name_valid()

    def is_name_valid(self):
        """
        Returns:
        """
        # Check if file format is empty.
        if not self.config['FileFormat']:
            return False, f'{Color.fail}Warning{Color.endc} ' \
                          f'No FileFormat selected. List of supported FileFormat:' \
                          f'{Color.header}{self.supported_file_format}' \
                          f'{Color.endc}', self.config['FileFormat']
        # Check if whether operators of the processor are supported or not.
        if self.config['FileFormat'] not in self.supported_file_format:
            return False, f'{Color.fail}{self.config["FileFormat"]}{Color.endc}' \
                          f' FileFormat is not supported. ' \
                          f'List of supported FileFormats : {Color.header}' \
                          f'{self.supported_file_format}{Color.endc}', self.config['FileFormat']
        return True, '', None

    def update_config_value(self, name, old_value, new_value):
        # Add new value to empty operations list
        self.config['FileFormat'] = new_value

    def get_dependencies(self):
        return []
