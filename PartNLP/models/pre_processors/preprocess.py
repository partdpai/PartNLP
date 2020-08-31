"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""


class PreProcess:
    """
            PreProcess
    """
    def __init__(self, config):
        self.stem_words, self.model = [], None
        self.lemmatized_words, self.words = [], []
        self.normalize_text, self.sentences = [], []
        self.language, self.data = config['Language'], config['text']

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
        self.words = \
            [self.model.word_tokenize(sent) for sent in self.sentences]
        return self.words

    def lemmatize(self): pass

    def normalize(self): pass

    def stem(self): pass

    def pos(self): pass
