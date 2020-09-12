"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import hazm
from hazm import Stemmer, Normalizer, Lemmatizer
from PartNLP.models.pre_processors.preprocess import PreProcess


class HAZMPreprocessor(PreProcess):
    """
    Initialize its constructor using parent constructor.
    """
    def __init__(self, config=None):
        super().__init__(config)
        self.model = hazm

    def stem(self):
        """
        :return:
        """
        stemmer = Stemmer()
        for chunk in self.words:
            self._get_stem_words(chunk, stemmer)
        return self.stem_words

    def _get_stem_words(self, chunk, stemmer):
        temp_words = []
        for words in chunk:
            temp = []
            [temp.append(stemmer.stem(str(word))) for word in words]
            temp_words.append(temp)
        self.stem_words.append(temp_words)

    def lemmatize(self):
        """
        :return:
        """
        lemmatizer = Lemmatizer()
        for paragraph in self.words:
            temp_lemma = []
            for words in paragraph:
                temp_lemma.append(self._lemmatize_words(words, lemmatizer))
            self.lemmatized_words.append(temp_lemma)
        return self.lemmatized_words

    def _lemmatize_words(self, words, lemmatizer):
        temp = []
        for word in words:
            word_lemma = lemmatizer.lemmatize(word)
            if word_lemma is not None:
                temp.append(word_lemma)
            else:
                temp.append(word)
        return temp
