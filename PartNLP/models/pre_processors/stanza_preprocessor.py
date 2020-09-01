"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import stanza
from PartNLP.models.pre_processors.preprocess import PreProcess


class STANZAPreprocessor(PreProcess):
    """
            STANZA
    """
    def __init__(self, config):
        super().__init__(config)
        self.model = stanza

    def sent_tokenize(self):
        """
        Returns:
        """
        nlp = self.model.Pipeline(lang=self.language, processors='tokenize',
                                  logging_level='WARNING', use_gpu=True)
        for paragraph in self.data:
            doc = nlp(paragraph)
            temp_sent, temp_words = [], []
            for sentence in doc.sentences:
                temp_word = []
                for token in sentence.tokens:
                    temp_word.append(token.text)
                temp_words.append(temp_word)
                temp_sent.append(sentence.text)
            self.sentences.append(temp_sent)
            self.words.append(temp_words)
        return self.sentences

    def word_tokenize(self):
        """
        Because of the word's dependency and also because of
        the stanza structure word_tokenize uses sent tokenize
        """
        self.sentences = []
        return self.words

    def pos(self):
        nlp = stanza.Pipeline(lang=self.language, processors='tokenize, pos, lemma',
                              tokenize_pretokenized=True, logging_level='WARNING')
        for paragraph in self.words:
            if paragraph:
                doc = nlp(paragraph)
                temp_lemma = []
                for sentence in doc.sentences:
                    temp = []
                    for word in sentence.words:
                        if word.lemma is not None:
                            temp.append(word.lemma)
                    temp_lemma.append(temp)
                self.lemmatized_words.append(temp_lemma)
            else:
                self.lemmatized_words.append([])

    def lemmatize(self):
        return self.lemmatized_words
