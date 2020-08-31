"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import unittest
from PartNLP.models.helper import configuration
from PartNLP.models.pre_processors.stanza_preprocessor import STANZAPreprocessor


class TestHazm(unittest.TestCase):
    """
        UnitTest
    """
    def setUp(self):
        super(TestHazm, self).__init__()
        self.config = configuration.get_config()
        self.stanza = None

    def test_sent_tokenize(self):
        """
        Returns:
            None
        """
        self.config['text'] = self.read('fixtures/test_sentence_tokenize.txt')
        self.stanza = STANZAPreprocessor(self.config)
        self.assertEqual(self.stanza.sent_tokenize(),
                         [' ما هم برای وصل کردن آمدیم !', ' ولی برای پردازش، جدا بهتر نیست ؟'])

    def test_word_tokenize(self):
        """
        Returns:
            None
        """
        self.config['text'] = self.read('fixtures/test_word_tokenize.txt')
        self.stanza = STANZAPreprocessor(self.config)
        self.stanza.sent_tokenize()
        self.assertEqual(self.stanza.word_tokenize(),
                         [['ولی', 'برای', 'پردازش،', 'جدا', 'بهتر', 'نیست', '؟']])

    def test_lemmatize(self):
        """
        Returns:
            None
        """
        self.config['text'] = self.read('fixtures/test_lemmatize.txt')
        self.stanza = STANZAPreprocessor(self.config)
        self.stanza.sent_tokenize()
        self.stanza.word_tokenize()
        self.stanza.pos()
        # self.assertEqual(self.stanza.lemmatize(), [['می\u200cروم']])

    def read(self, path):
        """
        Args:
            path:
        Returns:
            text:
        """
        with open(path, 'r') as file:
            text = file.read()
        return text


if __name__ == '__main__':
    unittest.main()
