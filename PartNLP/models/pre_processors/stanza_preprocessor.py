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
        self.data = '\n\n &&new document&& \n\n'.join(self.data)
        doc = nlp(self.data)
        rest_sent, rest_words = self._get_sent_tokenize_words(doc)
        if rest_sent:
            self.sentences.append(rest_sent)
            self.words.append(rest_words)
        return self.sentences

    def _get_sent_tokenize_words(self, doc):
        temp_sent, temp_words = [], []
        for sentence in doc.sentences:
            if sentence.text != '&&new document&&':
                sent, words = self._handle_paragraph(sentence)
                temp_words.append(words)
                temp_sent.append(sent)
            else:
                self.sentences.append(temp_sent)
                self.words.append(temp_words)
                temp_sent, temp_words = [], []
        return temp_sent, temp_words

    def _handle_paragraph(self, sentence):
        temp_word = []
        for token in sentence.tokens:
            temp_word.append(token.text)
        return sentence.text, temp_word

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
        for chunk in self.words:
            if chunk:
                doc = nlp(chunk)
                self.lemmatized_words.append(self._get_words_lemma(doc))
            else:
                self.lemmatized_words.append([])

    def _get_words_lemma(self, doc):
        temp_lemma = []
        for sentence in doc.sentences:
            temp = []
            for word in sentence.words:
                if word.lemma is not None:
                    temp.append(word.lemma)
            temp_lemma.append(temp)
        return temp_lemma

    def lemmatize(self):
        return self.lemmatized_words
