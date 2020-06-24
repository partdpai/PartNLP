"""This function uses to find all the needed validators based on config.
"""
from PartNLP.models.helper.color import Color
from PartNLP.models.validation.pos_validator import PosValidator
from PartNLP.models.helper.constants import SUPPORTED_PROCESSORS
from PartNLP.models.validation.validator import Validator
from PartNLP.models.validation.sent_validator import SentValidator
from PartNLP.models.validation.word_validator import WordValidator
from PartNLP.models.validation.stem_validator import StemValidator
from PartNLP.models.validation.package_validator import PackageValidator
from PartNLP.models.validation.language_validator import LanguageValidator
from PartNLP.models.validation.lemmatize_validator import LemmatizeValidator
from PartNLP.models.validation.normalize_validator import NormalizeValidator
from PartNLP.models.validation.processor_validator import ProcessorsValidator


name_to_validator_dic = {
    'package': (1, PackageValidator),
    'Language': (2, LanguageValidator),
    'processors': (3, ProcessorsValidator),
    'NORMALIZE': (4, NormalizeValidator),
    'S_TOKENIZE': (5, SentValidator),
    'W_TOKENIZE': (6, WordValidator),
    'POS': (7, PosValidator),
    'STEM': (8, StemValidator),
    'LEMMATIZE': (9, LemmatizeValidator),
}


def get_new_value_from_cmd(message):
    print(message)
    return input('Please enter a valid value:')


def config_validator(config, set_values=True, get_new_value=get_new_value_from_cmd):
    check_list = set()

    def call_validator(v_name):
        # set and validate
        print(f'{Color.Yellow}validating {v_name} in process...{Color.ENDC}')
        validator = name_to_validator_dic[v_name][1](config)
        success, message, val = validator.isvalid()
        while not success:
            validator.update_config_value(v_name, val, get_new_value(message))
            success, message, val = validator.isvalid()
        check_list.add(v_name)
        # dependency check
        for d in validator.get_dependencies():
            if d not in check_list:
                call_validator(d)

    requires_validation = [name for name in name_to_validator_dic if name in config]
    requires_validation = sorted(requires_validation, key=lambda x: name_to_validator_dic[x][0])
    for v_name in requires_validation:
        call_validator(v_name)

    processors = [name for name in check_list if name in SUPPORTED_PROCESSORS]
    config['processors'] = processors
    config['processors'] = sorted(config['processors'], key=lambda x: name_to_validator_dic[x][0])
