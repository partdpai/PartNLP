"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import os
import logging
from pathlib import Path
from PartNLP.models.helper.readers_and_writers.reader_and_writer \
    import ReaderAndWriter, Document


class TxtReaderAndWriter(ReaderAndWriter):
    """
            TXT READER
    """
    def __init__(self):
        super(TxtReaderAndWriter, self).__init__()
        self.docs = []

    def read_data(self, data, batch_size):
        """
        Args:
            data: An object of InputDocument
        Returns:
            Document: An object
        """
        with open(data.path, encoding='utf-8', errors='ignore') as file:
            while True:
                self.docs = file.readlines(batch_size)
                if not self.docs:
                    break
                yield self.docs

    def write_data(self, result_data):
        """
        Args:
            result_data: an object of OutPutDocument
        Returns:
            None
        """
        with open(os.getcwd() + '/preprocessed' + '/' +
                  result_data.package + '.' + result_data.operation + '.txt', 'a') as outfile:
            for value in result_data.output_value:
                outfile.write(str(value))
                outfile.write('\n')
            outfile.close()
        logging.getLogger().setLevel(logging.INFO)

    def get_file_size(self, path):
        return Path(path).stat().st_size
