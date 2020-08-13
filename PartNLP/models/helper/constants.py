"""
In this script, we are going to add all constant values in which used in the entire project.
"""
from PartNLP.models.pre_processors.hazm_preprocessor import HAZMPreprocessor as HAZM
from PartNLP.models.pre_processors.stanza_preprocessor import STANZAPreprocessor as STANZA
from PartNLP.models.pre_processors.parsivar_preprocessor import PARSIVARPreprocessor as PARSIVAR
from PartNLP.models.helper.readers_and_writers.txt_reader_and_writer import TxtReaderAndWriter
from PartNLP.models.helper.readers_and_writers.json_reader_and_writer import JsonReaderAndWriter

NAME_TO_PACKAGE_DICT = {'HAZM': HAZM, 'PARSIVAR': PARSIVAR, 'STANZA': STANZA}

NAME_TO_METHODS = {'NORMALIZE': lambda m: m.normalize(), 'S_TOKENIZE': lambda m: m.sent_tokenize(),
                   'W_TOKENIZE': lambda m: m.word_tokenize(), 'STEM': lambda m: m.stem(),
                   'LEMMATIZE': lambda m: m.lemmatize(), 'POS': lambda m: m.pos()}

NAME_TO_READER_AND_WRITER = {'TXT': TxtReaderAndWriter, 'JSON': JsonReaderAndWriter}

SUPPORTED_LANGUAGES_TO_PACKAGES = {'PERSIAN': ['HAZM', 'PARSIVAR', 'STANZA'], 'ENGLISH': ['STANZA']}
SUPPORTED_PROCESSORS_FOR_PACKAGES = {'HAZM': ['NORMALIZE', 'S_TOKENIZE', 'STEM', 'W_TOKENIZE', 'LEMMATIZE'],
                                     'PARSIVAR': ['NORMALIZE', 'S_TOKENIZE', 'STEM', 'W_TOKENIZE'],
                                     'STANZA': ['S_TOKENIZE', 'W_TOKENIZE', 'LEMMATIZE']
                                     }
SUPPORTED_PROCESSORS = ['NORMALIZE', 'S_TOKENIZE', 'STEM', 'W_TOKENIZE', 'LEMMATIZE']
NAME_OF_SUPPORTED_LANGUAGES = ['ENGLISH', 'PERSIAN']
NAME_OF_SUPPORTED_PACKAGES = ['HAZM', 'PARSIVAR', 'STANZA']
EQUIVALENT_LANGUAGES_TO_STANZA = {'ENGLISH': 'en', 'PERSIAN': 'fa'}

PROCESSORS_TO_LABELS = {'S_TOKENIZE': 'Sent tokenize', 'STEM': 'Stem',
                        'W_TOKENIZE': 'Word tokenize',
                        'NORMALIZE': 'Normalize', 'LEMMATIZE': 'Lemma'}

STANZA_RESOURCE_NAMES = {'persian': 'fa', 'english': 'en'}
