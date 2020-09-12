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

    def normalize(self):
        """
        :return:
        """
        for paragraph in self.data:
            if paragraph != "":
                self.normalize_text.append(
                    self.model.Normalizer().normalize(paragraph))
        return self.normalize_text

    def sent_tokenize(self):
        """
        :return:
        """
        for paragraph in self.data:
            self.sentences.append(self.model.sent_tokenize(paragraph))
        return self.sentences

    def word_tokenize(self):
        """
        :return:
        """
        for paragraph in self.sentences:
            temp_words = []
            for sent in paragraph:
                temp_words.append(self.model.word_tokenize(sent))
            self.words.append(temp_words)
        return self.words

    def lemmatize(self): pass

    def stem(self): pass

    def pos(self): pass
