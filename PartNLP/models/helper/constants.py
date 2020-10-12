"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from PartNLP.models.pre_processors.hazm_preprocessor import HAZMPreprocessor as HAZM
from PartNLP.models.pre_processors.stanza_preprocessor import STANZAPreprocessor as STANZA
from PartNLP.models.pre_processors.parsivar_preprocessor import PARSIVARPreprocessor as PARSIVAR
from PartNLP.models.helper.readers_and_writers.txt_reader_and_writer import TxtReaderAndWriter
from PartNLP.models.helper.readers_and_writers.json_reader_and_writer import JsonReaderAndWriter

NAME_TO_PACKAGE_DICT = {'hazm': HAZM, 'parsivar': PARSIVAR, 'stanza': STANZA}

NAME_TO_METHODS = {'normalize': lambda m: m.normalize(), 's_tokenize': lambda m: m.sent_tokenize(),
                   'w_tokenize': lambda m: m.word_tokenize(), 'stem': lambda m: m.stem(),
                   'lemmatize': lambda m: m.lemmatize(), 'pos': lambda m: m.pos()}

NAME_TO_READER_AND_WRITER = {'txt': TxtReaderAndWriter, 'json': JsonReaderAndWriter}

SUPPORTED_LANGUAGES_TO_PACKAGES = {'persian': ['hazm', 'parsivar', 'stanza'], 'english': ['stanza']}
SUPPORTED_PROCESSORS_FOR_PACKAGES = \
    {'hazm': ['normalize', 's_tokenize', 'stem', 'w_tokenize', 'lemmatize'],
     'parsivar': ['normalize', 's_tokenize', 'stem', 'w_tokenize'],
     'stanza': ['s_tokenize', 'w_tokenize', 'lemmatize']
     }
SUPPORTED_PROCESSORS = ['normalize', 's_tokenize', 'stem', 'w_tokenize', 'lemmatize', 'pos']
NAME_OF_SUPPORTED_LANGUAGES = ['english', 'persian']
NAME_OF_SUPPORTED_PACKAGES = ['hazm', 'parsivar', 'stanza']
EQUIVALENT_LANGUAGES_TO_STANZA = {'english': 'en', 'persian': 'fa'}

PROCESSORS_TO_LABELS = {'s_tokenize': 'Sent tokenize', 'stem': 'Stem',
                        'w_tokenize': 'Word tokenize',
                        'normalize': 'Normalize', 'lemmatize': 'Lemma'}

BATCH_SIZE_BASED_ON_PACKAGE = {'hazm': 1000000, 'parsivar': 10000, 'stanza': 100000}

SUPPORTED_FILE_FORMATS = ['txt', 'json']

SUPPORTED_MULTI_PROCESS_STATUS = ['order_base', 'free_order_base', 'none']
