"""
Pipeline runs pre-process such as word-tokenize, sent-tokenize, stemming
"""
from PartNLP.models.helper import configuration
from PartNLP.models.validation.config_validator import config_validator
from PartNLP.models.helper.constants import NAME_TO_PACKAGE_DICT, NAME_TO_METHODS


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

        >>> Pipeline(package='HAZM', text=text, processors=['S_TOKENIZE', 'W_TOKENIZE'])
     """

    def __init__(self, lang='persian', package='HAZM', processors=[], text='', input_file='', report_process=True,
                 logging_level='INFO', verbose=None, use_gpu=True, **kwargs):
        # text = ''
        config = configuration.get_config()
        config['processors'] = processors
        config['package'] = package
        config['InputFilePath'] = input_file
        config['text'] = text
        config['Language'] = lang
        # Check dependencies and validate config
        config_validator(config)
        self._work_flow(config)

    def _work_flow(self, config):
        processors, package = config['processors'], config['package']
        # Call the model
        model = NAME_TO_PACKAGE_DICT[package](config)
        # Execute selected operator by calling its corresponded method
        for value in processors:
            NAME_TO_METHODS[value](model)
        model.write_to_file()
