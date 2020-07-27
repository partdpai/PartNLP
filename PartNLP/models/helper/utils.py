"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from tqdm import tqdm


def batch_data(data, batch_size):
    """
    Args:
        data:
        batch_size:
    Returns:
    """
    data_size = len(data)
    for ndx in tqdm(range(0, data_size, batch_size)):
        yield data[ndx:min(ndx + batch_size, data_size)]
