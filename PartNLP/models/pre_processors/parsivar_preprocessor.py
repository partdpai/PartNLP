"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
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
        return self.sentences

    def word_tokenize(self):
        self.words = [self.model.Tokenizer().tokenize_words(sent) for sent in self.sentences]
        return self.words

    def normalize(self):
        """
        :return:
        """
        normalizer = Normalizer()
        for line in self.data.split('\n'):
            if line != "":
                self.normalize_text.append(normalizer.normalize(line))
        return self.normalize_text

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
        return self.stem_words
