"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import os
import logging
import concurrent.futures
from time import perf_counter
from tqdm import tqdm
from PartNLP.models.helper import configuration
from PartNLP.models.helper.program_profiling import show_program_profile
from PartNLP.models.validation.config_validator import config_validator
from PartNLP.models.helper.constants import NAME_TO_PACKAGE_DICT, \
    NAME_TO_METHODS, NAME_TO_READER_AND_WRITER, BATCH_SIZE_BASED_ON_PACKAGE
from PartNLP.models.helper.readers_and_writers.reader_and_writer \
    import InputDocument, OutPutDocument


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
    def __init__(self, file_path, use_multiprocess=True, lang='persian',
                 package='HAZM', processors=[], **kwargs):
        self.output_list = []
        config = self.__initialize_config(file_path, lang,
                                          package, processors,
                                          use_multiprocess, **kwargs)
        config_validator(config)
        self.reader_writer_obj = NAME_TO_READER_AND_WRITER[config['InputFileFormat']]()
        self._work_flow(config, self.output_list)

    def _work_flow(self, config, selected_operations):
        start_time = perf_counter()
        os.makedirs(os.getcwd() + '/preprocessed', exist_ok=True)
        data = InputDocument(config['InputFilePath'], config['InputFileFormat'])
        self._check_multiprocess(config, selected_operations, data)
        logging.warning(f'the result has been saved in {os.getcwd()}/preprocessed folder')
        program_time = perf_counter() - start_time
        show_program_profile(config['package'], self.batch_size,
                             config['processors'], program_time,
                             config['use_multiprocess'],
                             self.reader_writer_obj.get_file_size(config['InputFilePath']))

    def _check_multiprocess(self, config, selected_operations, data):
        if config['use_multiprocess']:
            self._run_with_multiprocessing(config, selected_operations, data)
        else:
            self._run_without_multiprocessing(config, selected_operations, data)

    def _run_with_multiprocessing(self, config, output_list, data):
        with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
            for index, batch_text in enumerate(
                    tqdm(self.reader_writer_obj.read_data(data, batch_size=self.batch_size))):
                executor.submit(
                    self._run, config, config['processors'],
                    output_list, config['package'], batch_text, index)

    def _run_without_multiprocessing(self, config, output_list, data):
        for index, batch_text in enumerate(
                tqdm(self.reader_writer_obj.read_data(data, batch_size=self.batch_size))):
            self._run(config, config['processors'],
                      output_list, config['package'], batch_text, index)

    def _run(self, *args):
        args[0]['text'] = '\n'.join(args[4])
        model = NAME_TO_PACKAGE_DICT[args[3]](args[0])
        for operation in args[1]:
            self._run_operation(model, operation, args[2], args[3], args[5])

    def _run_operation(self, *args):
        output_value = NAME_TO_METHODS[args[1]](args[0])
        if args[1] in args[2]:
            self.reader_writer_obj.write_data(
                OutPutDocument(output_value, args[1], args[3]))

    def __initialize_config(self, input_file_path, lang, package,
                            processors, use_multiprocess, **kwargs):
        config = configuration.get_config()
        config['processors'], config['use_multiprocess'] = processors, use_multiprocess
        self.output_list, config['package'] = config['processors'], package
        config['InputFilePath'], config['Language'] = input_file_path, lang
        if 'batch_size' in kwargs.keys():
            self.batch_size = kwargs['batch_size']
        else:
            self.batch_size = BATCH_SIZE_BASED_ON_PACKAGE[config['package']]
        return config
