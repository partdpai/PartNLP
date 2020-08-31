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

    def normalize(self):
        """
        :return:
        """
        normalizer = Normalizer()
        for line in self.data.split('\n'):
            self.normalize_text.append(normalizer.normalize(line)) \
                if line != "" else None
        return self.normalize_text

    def stem(self):
        """
        :return:
        """
        stemmer = Stemmer()
        for words in self.words:
            temp = []
            [temp.append(stemmer.stem(str(word))) for word in words]
            self.stem_words.append(temp)
        return self.stem_words

    def lemmatize(self):
        """
        :return:
        """
        lemmatizer = Lemmatizer()
        for words in self.words:
            temp = []
            for word in words:
                word_lemma = lemmatizer.lemmatize(word)
                if word_lemma is not None:
                    temp.append(word_lemma.split("#")[1]) if "#" in word_lemma \
                        else temp.append(word_lemma)
                else:
                    temp.append(word)
            self.lemmatized_words.append(temp)
        return self.lemmatized_words
