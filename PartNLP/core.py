"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import os
import logging
from tqdm import tqdm
from PartNLP.models.helper import configuration
from PartNLP.models.validation.config_validator import config_validator
from PartNLP.models.helper.constants import NAME_TO_PACKAGE_DICT, \
    NAME_TO_METHODS, NAME_TO_READER_AND_WRITER
from PartNLP.models.helper.readers_and_writers.reader_and_writer \
    import InputDocument, OutPutDocument
from PartNLP.models.helper.time_and_usage_profiling import profile


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
    def __init__(self, input_file_path, input_file_format, lang='persian',
                 package='HAZM', processors=[], **kwargs):
        self.output_list, self.document = [], []
        config = self.__initialize_config(input_file_path, input_file_format,
                                          lang, package, processors)
        config_validator(config)
        self.reader_writer_obj = NAME_TO_READER_AND_WRITER[config['InputFileFormat']]()
        self._work_flow(config, self.output_list)

    @profile
    def _work_flow(self, config, output_list):
        processors, package = config['processors'], config['package']
        # Execute selected operator by calling its corresponded method
        os.makedirs(os.getcwd() + '/preprocessed', exist_ok=True)
        data = InputDocument(config['InputFilePath'], config['InputFileFormat'])
        for lines in tqdm(self.reader_writer_obj.read_data(data, batch_size=10000000)):
            config['text'] = '\n'.join(lines)
            model = NAME_TO_PACKAGE_DICT[package](config)
            for operation in processors:
                output_value = NAME_TO_METHODS[operation](model)
                if operation in output_list:
                    self.reader_writer_obj.write_data(
                        OutPutDocument(output_value, operation, package))
        logging.info(f'the result has been saved in {os.getcwd()}/preprocessed folder')

    def __initialize_config(self, input_file_path, input_file_format,
                            lang, package, processors):
        config = configuration.get_config()
        config['InputFileFormat'] = input_file_format
        config['processors'] = processors
        self.output_list = config['processors']
        config['package'] = package
        config['InputFilePath'] = input_file_path
        config['Language'] = lang
        return config
