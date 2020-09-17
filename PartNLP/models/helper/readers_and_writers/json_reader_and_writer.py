"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import os
import json
import logging
from pathlib import Path
from collections import defaultdict
from PartNLP.models.helper.readers_and_writers.reader_and_writer \
    import ReaderAndWriter, Document


class JsonReaderAndWriter(ReaderAndWriter):
    """
            TXT READER
    """
    def __init__(self):
        super(JsonReaderAndWriter, self).__init__()
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
        nested_data = defaultdict(dict)
        path = self._get_path(result_data)
        with open(path, 'a') as outfile:
            if result_data.operation == 'normalize':
                nested_data = self._build_nested_paragraphs(result_data.output_value)
            elif result_data.operation == 's_tokenize':
                nested_data = self._build_nested_sentences(result_data.output_value)
            else:
                nested_data = self._build_nested_words(result_data.output_value)
            outfile.write(json.dumps(nested_data, ensure_ascii=False, indent=4) + '\n')
        logging.getLogger().setLevel(logging.INFO)

    def _get_path(self, result_data):
        """
        Args:
            result_data:
        Returns:
        """
        path = os.path.join(result_data.output_path, 'preprocessed/')
        if not os.path.isdir(path):
            os.mkdir(path)
        return path + result_data.package + '.' + result_data.operation + '.json'

    def _build_nested_paragraphs(self, data):
        """
        Args:
            data:
        Returns:
        """
        parent_name, child_name = 'دیتا', 'پاراگراف'
        return self._iterate_items(data, parent_name, child_name, 1)

    def _build_nested_sentences(self, data):
        """
        Args:
            data:
        Returns:
        """
        parent_name, child_name, nested_data = 'پاراگراف', 'جمله', defaultdict(dict)
        index = 0
        for paragraph in data:
            if paragraph:
                temp = self._iterate_items(paragraph, parent_name, child_name, index + 1)
                nested_data[str(list(temp.keys())[0])] = list(temp.values())[0]
                index += 1
        return {'دیتا': nested_data}

    def _build_nested_words(self, data):
        """
        Args:
            data:
        Returns:
        """
        parent_name, child_name, nested_sentences = 'جمله', 'کلمه', defaultdict(dict)
        paragraph_index = 0
        for paragraph in data:
            if paragraph:
                sentence_index = 0
                for sentence in paragraph:
                    if sentence:
                        temp = self._iterate_items(
                            sentence, parent_name, child_name, sentence_index + 1)
                        nested_sentences[f'پاراگراف{paragraph_index + 1}'][str(list(temp.keys())[0])] \
                            = list(temp.values())[0]
                        paragraph_index += 1
                        sentence_index += 1
        return {'دیتا1': nested_sentences}

    def _iterate_items(self, items, parent_name, child_name, index):
        """
        Args:
            items:
            parent_name:
            child_name:
            index:
        Returns:
        """
        components, nested_components = defaultdict(dict), defaultdict(dict)
        index_item = 0
        for item in items:
            if item != '\n':
                components[f'{child_name}{index_item + 1}'] = item
                index_item += 1
        nested_components[f'{parent_name}{index}'] = components
        return nested_components

    def get_file_size(self, path):
        """
        Args:
            path:
        Returns:
        """
        return Path(path).stat().st_size
