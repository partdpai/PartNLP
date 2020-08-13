"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import json
import logging
import os
from PartNLP.models.helper.readers_and_writers.reader_and_writer\
    import ReaderAndWriter, Document, Types


class JsonReaderAndWriter(ReaderAndWriter):
    """
            JSON READER
    """
    def __init__(self):
        super(JsonReaderAndWriter, self).__init__()
        self.docs = []

    def read_data(self, data, batch_size) -> Document:
        """
        Args:
            data: An object of InputDocument
        Returns:
            Document: An object of Document
        """
        with open(data.path, encoding='utf-8') as json_file:
            self.docs = json.load(json_file, strict=False)
            self.docs['text'] = self.docs['text'].split(data.separator)
            return Document(self.docs['text'], Types.txt_type)

    def write_data(self, result_data):
        """
        Args:
            result_data:
        Returns:
            None
        """
        with open(os.getcwd() + '/preprocessed' + '/' +
                  result_data.package + '.' + result_data.operation + '.json', 'w') as outfile:
            self.docs['text'] = result_data.output_value
            [json.dump(value, outfile, ensure_ascii=False) for value in self.docs['text']]
            outfile.close()
        logging.getLogger().setLevel(logging.INFO)
