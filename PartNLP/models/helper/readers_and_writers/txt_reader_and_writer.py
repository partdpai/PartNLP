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
        self.docs, self.next_document = [], False
        self.splitter = ''

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
        path = self._get_path(result_data)
        with open(path, 'a') as outfile:
            self._write_structured_data_base_operation(result_data, outfile)
        logging.getLogger().setLevel(logging.INFO)

    def _get_path(self, result_data):
        path = os.path.join(result_data.output_path, 'preprocessed/')
        if not os.path.isdir(path):
            os.mkdir(path)
        return path + result_data.package + '.' + result_data.operation + '.txt'

    def _write_structured_data_base_operation(self, result_data, outfile):
        """
        Args:
            result_data:
            outfile:
        Returns:
        """
        if result_data.operation == 'normalize':
            self._write_paragraph_level(result_data.output_value, outfile)
        elif result_data.operation == 's_tokenize':
            self._write_sentence_level(result_data.output_value, outfile)
        else:
            self._write_word_level(result_data.output_value, outfile)

    def _write_paragraph_level(self, items, outfile):
        """
        Args:
            items:
            outfile:
        Returns:
        """
        for item in items:
            self.next_document = False
            if item and item != '\n':
                outfile.write(str(item) + '\n')
                self.next_document = True
            outfile.write(f'{self.splitter} \n') if self.next_document else None

    def _write_sentence_level(self, chunks, outfile):
        """
        Args:
            chunks:
            outfile:
        Returns:
        """
        for chunk in chunks:
            self.iterate_items(chunk, outfile)
            outfile.write(f'{self.splitter} \n') if self.next_document else None

    def _write_word_level(self, chunks, outfile):
        """
        Args:
            chunks:
            outfile:
        Returns:
        """
        for chunk in chunks:
            self.next_document = False
            for words in chunk:
                self.iterate_items(words, outfile)
            outfile.write(f'{self.splitter} \n') if self.next_document else None

    def iterate_items(self, items, outfile):
        """
        Args:
            items:
            outfile:
        Returns:
        """
        self.next_document = False
        for item in items:
            outfile.write(str(item) + '\n') if item and item != '\n' else None
            self.next_document = True

    def get_file_size(self, path):
        """
        Args:
            path:
        Returns:
        """
        return Path(path).stat().st_size
