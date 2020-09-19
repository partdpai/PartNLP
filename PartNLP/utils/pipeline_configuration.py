"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import os
from PartNLP.models.helper.constants import BATCH_SIZE_BASED_ON_PACKAGE


def init_config():
    """
    :return: all set values(config)
    """
    config = {
        'text': '', 'Language': 'persian',
        'FilePath': '', 'operations': [],
        'package': '', 'FileFormat': '',
        'multiProcessType': '', 'OutputPath': '',
        'batchSize': 1000, 'selectedOperations': [],
        'number_of_batches': 0, 'number_of_cpus': 0
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
    set_output_file_path(config, **kwargs)
    set_number_of_batches(config, **kwargs)
    set_number_of_cpus(config, **kwargs)
    return config


def set_output_file_path(config, **kwargs):
    """
    Args:
        config:
        **kwargs:
    Returns:
    """
    if 'output_path' in kwargs.keys():
        config['OutputPath'] = kwargs['output_path']
    else:
        config['OutputPath'] = os.getcwd()


def set_number_of_cpus(config, **kwargs):
    """
    Args:
        config:
        **kwargs:
    Returns:
    """
    if 'number_of_cpus' in kwargs.keys():
        config['number_of_cpus'] = kwargs['number_of_cpus']


def set_number_of_batches(config, **kwargs):
    """
    Args:
        config:
        **kwargs:
    Returns:
    """
    if 'number_of_batches' in kwargs.keys():
        config['number_of_batches'] = kwargs['number_of_batches']


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
