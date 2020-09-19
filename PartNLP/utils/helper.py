"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import concurrent.futures
import multiprocessing
from collections import defaultdict
import psutil
from tqdm import tqdm
from PartNLP.models.helper.constants import \
    NAME_TO_PACKAGE_DICT, NAME_TO_METHODS
from PartNLP.models.helper.readers_and_writers.reader_and_writer \
    import OutPutDocument


def run(config, data, reader):
    """
    Args:
        config:
        data:
        reader:
    Returns:
    """
    check_multiprocess(config, data, reader)


def check_multiprocess(config, data, reader):
    """
    Args:
        config:
        data:
        reader:
    Returns:
    """
    if config['multiProcessType'] == 'free_order_base':
        run_with_free_order_multiprocessing(config, data, reader)
    elif config['multiProcessType'] == 'order_base':
        run_with_ordered_multiprocessing(config, data, reader)
    else:
        run_without_multiprocessing(config, data, reader)


def run_with_free_order_multiprocessing(config, data, reader):
    """
    Args:
        config:
        data:
        reader:
    Returns:
    """
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for index, batch_text in enumerate(
                tqdm(reader.read_data(data, config['batchSize']))):
            executor.submit(run_operations, config=config, batch_text=batch_text,
                            index=index, reader=reader)


def run_without_multiprocessing(config, data, reader):
    """
    Args:
        config:
        data:
        reader:
    Returns:
    """
    for index, batch_text in enumerate(
            tqdm(reader.read_data(data, config['batchSize']))):
        run_operations(config=config, batch_text=batch_text, index=index, reader=reader)


def run_operations(**kwargs):
    """
    Args:
        **kwargs:
    Returns:
    """
    kwargs['config']['text'] = kwargs['batch_text']
    model = NAME_TO_PACKAGE_DICT[kwargs['config']['package']](kwargs['config'])
    for operation in kwargs['config']['operations']:
        run_operation(model=model, operation=operation,
                      index=kwargs['index'], config=kwargs['config'], reader=kwargs['reader'])


def run_operation(**kwargs):
    """
    Args:
        **kwargs:
    Returns:
    """
    output_value = NAME_TO_METHODS[kwargs['operation']](kwargs['model'])
    if kwargs['operation'] in kwargs['config']['selectedOperations']:
        kwargs['reader'].write_data(
            OutPutDocument(output_value, kwargs['operation'], kwargs['config']['package'],
                           kwargs['config']['OutputPath']))


def run_with_ordered_multiprocessing(config, data, reader):
    """
    Args:
        config:
        data:
        reader:
    Returns:
    """
    batch_texts = []
    number_of_chunks = config['number_of_batches'] if config['number_of_batches'] \
        else find_number_of_chunks(config['batchSize'])
    print(f'number of chunks is: {number_of_chunks}')
    preprocessed_values = defaultdict(list)
    for index, batch_text in tqdm(enumerate(reader.read_data(data, config['batchSize']))):
        if (index + 1) % number_of_chunks == 0:
            batch_texts.append(batch_text)
            preprocessed_values = do_ordered_multiprocess(config=config, batch_texts=batch_texts)
            write(config, preprocessed_values, reader)
            batch_texts, preprocessed_values = [], []
        else:
            batch_texts.append(batch_text)
    if batch_texts:
        write(config, do_ordered_multiprocess(config=config, batch_texts=batch_texts), reader)
        batch_texts = []


def do_ordered_multiprocess(**kwargs):
    """
    Args:
        **kwargs:
    Returns:
    """
    batch_texts_lists = []
    [batch_texts_lists.append((kwargs['config'], batch_text))
     for batch_text in kwargs['batch_texts']]
    if kwargs['config']['number_of_cpus']:
        with multiprocessing.Pool(kwargs['config']['number_of_cpus']) as pool:
            preprocessed_values = pool.map(get_preprocessed_dict, batch_texts_lists)
            pool.close()
    else:
        with multiprocessing.Pool() as pool:
            preprocessed_values = pool.map(get_preprocessed_dict, batch_texts_lists)
            pool.close()
    return preprocessed_values


def get_preprocessed_dict(lis):
    """
    Args:
        lis:
    Returns:
    """
    preprocessed_dict = defaultdict(dict)
    lis[0]['text'] = lis[1]
    model = NAME_TO_PACKAGE_DICT[lis[0]['package']](lis[0])
    for operation in lis[0]['operations']:
        output_value = NAME_TO_METHODS[operation](model)
        if operation in lis[0]['selectedOperations']:
            preprocessed_dict[operation] = output_value
    return preprocessed_dict


def write(config, preprocessed_values, reader):
    """
    Args:
        config:
        preprocessed_values:
        reader:
    Returns:
    """
    for batch in preprocessed_values:
        for key, value in batch.items():
            reader.write_data(OutPutDocument(value, key, config['package'], config['OutputPath']))


def find_number_of_chunks(batch_size):
    """
    Args:
        batch_size:
    Returns:
    """
    require_memory_usage = psutil.virtual_memory().available / 80
    return int(require_memory_usage / batch_size)
