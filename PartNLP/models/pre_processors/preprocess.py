"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import os
import json
import logging
from PartNLP.models.helper.color import Color


class PreProcess:
    """
            PreProcess
    """
    def __init__(self, config):
        self.normalize_text = []
        self.sentences = []
        self.words = []
        self.result = []
        self.stem_words = []
        self.lemmatized_words = []
        self.non_stopwords = []
        self.data = config['text']
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

    def normalize(self):
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
            print()
