"""
        SEMANTIC SEARCH ENGINE
            AUTHORS:
                MOSTAFA & SAMAN
"""
import os
import logging
from PartNLP.models.helper import configuration
from PartNLP.models.validation.config_validator import config_validator
from PartNLP.models.helper.constants import NAME_TO_PACKAGE_DICT, NAME_TO_METHODS
from PartNLP.models.helper.readers_and_writers.txt_reader_and_writer import TxtReader, TxtWriter
from PartNLP.models.helper.readers_and_writers.reader_and_writer \
    import InputDocument, OutPutDocument
from PartNLP.models.helper.utils import batch_data


class Pipeline:
    """
    **Supported packages**:

        1. HAZM
        2. PARSIVAR
        3. STANZA

    **Supproted languages**:

        1. Persian

    **Supproted operations**:


        1. Normalize          Usage(NORMALIZE)
        2. Tokenize Sentences Usage(S_TOKENIZE)
        3. Tokenize Words     Usage(W_TOKENIZE)
        4. Stem Words         Usage(STEM)
        5. Lemmatize Words    Usage(LEMMATIZE)

    EXAMPLE:

    text = 'برای بدست آوردن نتایج بهتر میتوان از پیش پردازش بهره برد'

        # >>> Pipeline(package='HAZM', text=text, processors=['S_TOKENIZE', 'W_TOKENIZE'])
     """

    def __init__(self, lang='persian', package='HAZM',
                 processors=[], text='', input_file='', **kwargs):
        config = configuration.get_config()
        config['processors'] = processors
        output_list = config['processors']
        config['package'] = package
        config['InputFilePath'] = input_file
        config['Language'] = lang
        if config['InputFilePath'] != '':
            self.document = TxtReader().read_data(
                InputDocument(config['InputFilePath'], 'txt'))
        # Check dependencies and validate config
        config_validator(config)
        self._work_flow(config, output_list)

    def _work_flow(self, config, output_list):
        processors, package = config['processors'], config['package']
        # Execute selected operator by calling its corresponded method
        os.makedirs(os.getcwd() + '/preprocessed', exist_ok=True)
        for lines in batch_data(self.document.text, batch_size=1):
            config['text'] = '\n'.join(lines)
            model = NAME_TO_PACKAGE_DICT[package](config)
            for operation in processors:
                output_value = NAME_TO_METHODS[operation](model)
                if operation in output_list:
                    TxtWriter().write_data(OutPutDocument(output_value, operation, package))
        logging.info(f'the result has been saved in {os.getcwd()}/preprocessed folder')
