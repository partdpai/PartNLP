"""Using Stanza to preprocessing documents.
"""
from PartNLP.models.pre_processors.preprocess import PreProcess
from PartNLP.models.helper.color import Color
import stanza


class STANZAPreprocessor(PreProcess):
    def __init__(self, config):
        # Initialize its constructor using parent constructor.
        super().__init__(config)
        self.model = stanza

    def sent_tokenize(self):
        """
        Returns:
        """
        nlp = self.model.Pipeline(lang=self.language, processors='tokenize')
        doc = nlp(self.data)
        for sentence in doc.sentences:
            temp_sent = ''
            tem_word = []
            for token in sentence.tokens:
                temp_sent += (' ' + token.text)
                tem_word.append(token.text)
            self.sentences.append(temp_sent)
            self.words.append(tem_word)
        return self.sentences

    def word_tokenize(self):
        """
        Because of the word's dependency and also because of
        the stanza structure word_tokenize uses sent tokenize
        """
        return self.words

    def pos(self):
        nlp = stanza.Pipeline(lang=self.language, processors='tokenize, pos, lemma', tokenize_pretokenized=True)
        doc = nlp(self.words)
        for sentence in doc.sentences:
            temp = []
            for word in sentence.words:
                if word.lemma is not None:
                    if '#' in word.lemma:
                        temp.append(word.lemma.split('#')[1])
                    else:
                        temp.append(word.lemma)
            self.lemmatized_words.append(temp)
        # return lemmatized_words

    def lemmatize(self):
        return self.lemmatized_words
