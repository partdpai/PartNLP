"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import os
import logging
from PartNLP.models.helper.readers_and_writers.reader_and_writer \
    import ReaderAndWriter, Document, Types


class TxtReaderAndWriter(ReaderAndWriter):
    """
            TXT READER
    """
    def __init__(self):
        super(TxtReaderAndWriter, self).__init__()
        self.docs = []

    def read_data(self, data):
        """
        Args:
            data: An object of InputDocument
        Returns:
            Document: An object
        """
        self.docs = open(data.path, encoding='utf-8', errors='ignore').read()
        self.docs = self.docs.split(data.separator)
        return Document(self.docs, Types.txt_type)

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
