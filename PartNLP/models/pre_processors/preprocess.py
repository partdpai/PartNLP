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
        return self.sentences

    def word_tokenize(self):
        """
        :return:
        """
        self.words = [self.model.word_tokenize(sent) for sent in self.sentences]
        return self.words

    def lemmatize(self):
        pass

    def stem(self):
        pass

    def pos(self):
        pass

    def read_from_file(self, path=''):
        """
        :param path:
        :return:
        """
        if path:
            self.data = open(path, encoding='utf-8', errors='ignore').read()
