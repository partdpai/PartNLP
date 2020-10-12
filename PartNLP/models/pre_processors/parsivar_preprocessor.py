"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import parsivar
from parsivar import Normalizer, FindStems
from PartNLP.models.pre_processors.preprocess import PreProcess


class PARSIVARPreprocessor(PreProcess):
    """
            PARSIVARPreprocessor
    """
    def __init__(self, config=None):
        super().__init__(config)
        self.model = parsivar

    def sent_tokenize(self):
        for paragraph in self.data:
            if paragraph != '\n':
                self.sentences.append(
                    self.model.Tokenizer().tokenize_sentences(paragraph))
            else:
                self.sentences.append([])
        return self.sentences

    def word_tokenize(self):
        for paragraph in self.sentences:
            temp_words = []
            for sent in paragraph:
                temp_words.append(self.model.Tokenizer().tokenize_words(sent))
            self.words.append(temp_words)
        return self.words

    def stem(self):
        """
        :return:
        """
        stemmer = FindStems()
        for paragraph in self.words:
            self._stem_chunk_words(paragraph, stemmer)
        return self.stem_words

    def _stem_chunk_words(self, paragraph, stemmer):
        temp_words = []
        for words in paragraph:
            temp = []
            [temp.append(stemmer.convert_to_stem(str(word))) for word in words]
            temp_words.append(temp)
        self.stem_words.append(temp_words)
