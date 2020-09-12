"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from PartNLP.models.helper.constants import BATCH_SIZE_BASED_ON_PACKAGE


def init_config():
    """
    :return: all set values(config)
    """
    config = {
        'text': '', 'Language': 'persian',
        'FilePath': '', 'operations': [],
        'package': '', 'FileFormat': '',
        'multiProcessType': '', 'OutputFilePath': '',
        'batchSize': 1000, 'selectedOperations': []
    }
    return config


def set_pipeline_config(file_path, use_multiprocess,
                        package, processors, **kwargs):
    """
    Args:
        file_path:
        use_multiprocess:
        package:
        processors:
        **kwargs:
    Returns:
        config
    """
    config = init_config()
    config['FilePath'] = file_path
    config['operations'], config['multiProcessType'] = processors, use_multiprocess
    config['selectedOperations'], config['package'] = config['operations'], package
    set_file_format(config, **kwargs)
    return config


def set_batch_size(config, **kwargs):
    """
    Args:
        config:
        **kwargs:
    Returns:
    """
    if 'batch_size' in kwargs.keys():
        config['batchSize'] = kwargs['batch_size']
    else:
        config['batchSize'] = BATCH_SIZE_BASED_ON_PACKAGE[config['package']]


def set_file_format(config, **kwargs):
    """
    Args:
        config:
        **kwargs:
    Returns:
    """
    if 'file_format' in kwargs.keys():
        config['FileFormat'] = kwargs['file_format']
