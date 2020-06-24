"""
In this script, we are going to add all constant values in which used in the entire project.
"""
from PartNLP.models.pre_processors.hazm_preprocessor import HAZMPreprocessor as HAZM
from PartNLP.models.pre_processors.stanza_preprocessor import STANZAPreprocessor as STANZA
from PartNLP.models.pre_processors.parsivar_preprocessor import PARSIVARPreprocessor as PARSIVAR

NAME_TO_PACKAGE_DICT = {'HAZM': HAZM, 'PARSIVAR': PARSIVAR, 'STANZA': STANZA}

NAME_TO_METHODS = {'NORMALIZE': lambda m: m.normalizer(), 'S_TOKENIZE': lambda m: m.sent_tokenize(),
                         'W_TOKENIZE': lambda m: m.word_tokenize(), 'STEM': lambda m: m.stem(),
                         'LEMMATIZE': lambda m: m.lemmatize(), 'POS': lambda m: m.pos()}

SUPPORTED_LANGUAGES_TO_PACKAGES = {'PERSIAN': ['HAZM', 'PARSIVAR', 'STANZA'], 'ENGLISH': ['STANZA']}
SUPPORTED_PROCESSORS = ['NORMALIZE', 'S_TOKENIZE', 'STEM', 'W_TOKENIZE', 'LEMMATIZE', 'POS']
NAME_OF_SUPPORTED_LANGUAGES = ['ENGLISH', 'PERSIAN']
NAME_OF_SUPPORTED_PACKAGES = ['HAZM', 'PARSIVAR', 'STANZA']
