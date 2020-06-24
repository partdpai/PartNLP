"""
This model designed to pre-process data and
it has many features to help users to minimize their codes for
pre-processing purposes!
"""
import os
import json
import logging
from PartNLP.models.helper.color import Color


class PreProcess:
    """
    for testing
    """
    def __init__(self, config):
        self.sentences = []
        self.words = []
        self.result = []
        self.stem_words = []
        self.lemma = []
        self.lemmatized_words = []
        self.non_stopwords = []
        if config['text'] != '':
            self.data = config['text']
        else:
            self.file_path = config['InputFilePath']
            self.read_from_file(self.file_path)
        self.language = config['Language']
        self.dataset_type = config['DatasetType']
        self.input_path = config['InputFilePath']
        self.output_path = config['OutputFilePath']

    def sent_tokenize(self):
        """
        :return:
        """
        self.sentences = self.model.sent_tokenize(self.data)
        self.result = self.sentences

    def word_tokenize(self):
        """
        :return:
        """
        self.words = [self.model.word_tokenize(sent) for sent in self.sentences]
        self.result = self.words

    def lemmatize(self):
        pass

    def stem(self):
        pass

    def pos(self):
        pass

    def write_to_file(self):
        """
        :param path:
        :return:
        """
        path = os.getcwd() + '/output.txt'
        with open(path, 'w') as outfile:
            for value in self.result:
                outfile.writelines(str(value))
            outfile.close()
        logging.getLogger().setLevel(logging.INFO)
        logging.info(f'the result has been saved in {path}')

    def read_from_file(self, path=''):
        """
        :param path:
        :return:
        """
        if path:
            self.data = open(path, encoding='utf-8', errors='ignore').read()
