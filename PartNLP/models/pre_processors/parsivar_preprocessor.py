"""Using Parsivar to preprocessing document.
"""
from parsivar import Normalizer, FindStems
from PartNLP.models.pre_processors.preprocess import PreProcess
from PartNLP.models.helper.color import Color
import parsivar


class PARSIVARPreprocessor(PreProcess):
    """ PARSIVARPreprocessor
    """
    def __init__(self, config=None):
        # Initialize its constructor using parent constructor.
        super().__init__(config)
        self.model = parsivar

    def sent_tokenize(self):
        self.sentences = self.model.Tokenizer().tokenize_sentences(self.data)
        self.result = self.sentences

    def word_tokenize(self):
        self.words = [self.model.Tokenizer().tokenize_words(sent) for sent in self.sentences]
        self.result = self.words

    def normalizer(self):
        """
        :return:
        """
        normalizer = Normalizer()
        self.data = normalizer.normalize(self.data)
        self.result = self.data

    def stem(self):
        """
        :return:
        """
        stemmer = FindStems()
        for words in self.words:
            temp = []
            for word in words:
                temp.append(stemmer.convert_to_stem(str(word)))
            self.stem_words.append(temp)
        self.result = self.stem_words
