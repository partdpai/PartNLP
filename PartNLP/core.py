"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import os
import logging
from time import perf_counter
from PartNLP.utils.helper import run
from PartNLP.utils.pipeline_configuration import set_pipeline_config, set_batch_size
from PartNLP.models.helper.program_profiling import show_program_profile
from PartNLP.models.validators.config_validator import config_validator
from PartNLP.models.helper.constants import NAME_TO_READER_AND_WRITER
from PartNLP.models.helper.readers_and_writers.reader_and_writer \
    import InputDocument


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

        # >>> Pipeline(package='HAZM', text=text, operations=['S_TOKENIZE', 'W_TOKENIZE'])
     """
    def __init__(self, file_path, use_multiprocess='',
                 package='', operations=[], **kwargs):
        config = set_pipeline_config(file_path, use_multiprocess,
                                     package, operations, **kwargs)
        config_validator(config)
        set_batch_size(config, **kwargs)
        self.reader_writer_obj = NAME_TO_READER_AND_WRITER[config['FileFormat']]()
        self._work_flow(config)

    def _work_flow(self, config):
        start_time = perf_counter()
        data = InputDocument(config['FilePath'], config['FileFormat'])
        run(config, data, self.reader_writer_obj)
        logging.warning(f'the result has been saved in {config["OutputPath"]}/preprocessed folder')
        program_time = perf_counter() - start_time
        file_size = self.reader_writer_obj.get_file_size(config['FilePath'])
        show_program_profile(config=config, program_time=program_time, file_size=file_size)


if __name__ == '__main__':
    Pipeline(file_path='/home/mostafa/Desktop/small_dataset.txt', number_of_cpus=2, number_of_batches=3)