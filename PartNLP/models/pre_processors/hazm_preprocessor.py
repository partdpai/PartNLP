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
        for paragraph in self.data:
            self.normalize_text.append(normalizer.normalize(paragraph)) \
                if paragraph != "" else None
        return self.normalize_text

    def stem(self):
        """
        :return:
        """
        stemmer = Stemmer()
        for paragraph in self.words:
            temp_words = []
            for words in paragraph:
                temp = []
                [temp.append(stemmer.stem(str(word))) for word in words]
                temp_words.append(temp)
            self.stem_words.append(temp_words)
        return self.stem_words

    def lemmatize(self):
        """
        :return:
        """
        lemmatizer = Lemmatizer()
        for paragraph in self.words:
            temp_lemma = []
            for words in paragraph:
                temp = []
                for word in words:
                    word_lemma = lemmatizer.lemmatize(word)
                    if word_lemma is not None:
                        temp.append(word_lemma)
                    else:
                        temp.append(word)
                temp_lemma.append(temp)
            self.lemmatized_words.append(temp_lemma)
        return self.lemmatized_words
