"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import unittest
from PartNLP.models.helper import configuration
from PartNLP.models.pre_processors.hazm_preprocessor import HAZMPreprocessor


class TestHazm(unittest.TestCase):
    """
            UnitTest
    """
    def setUp(self):
        """
        Returns:
            None
        """
        super(TestHazm, self).__init__()
        self.config = configuration.get_config()
        self.hazm = None

    def test_normalize(self):
        """
        Returns:
            None
        """
        self.config['text'] = self.read('fixtures/test_normalize.txt')
        self.hazm = HAZMPreprocessor(self.config)
        self.assertEqual(' '.join(self.hazm.normalize()),
                         'اصلاح نویسه‌ها و استفاده از نیم‌فاصله پردازش را آسان می‌کند')

    def test_sent_tokenize(self):
        """
        Returns:
            None
        """
        self.config['text'] = self.read('fixtures/test_sentence_tokenize.txt')
        self.hazm = HAZMPreprocessor(self.config)
        self.assertEqual(self.hazm.sent_tokenize(),
                         ['ما هم برای وصل کردن آمدیم!', 'ولی برای پردازش، جدا بهتر نیست؟'])

    def test_word_tokenize(self):
        """
        Returns:
            None
        """
        self.config['text'] = self.read('fixtures/test_word_tokenize.txt')
        self.hazm = HAZMPreprocessor(self.config)
        self.hazm.sent_tokenize()
        self.assertEqual(self.hazm.word_tokenize(),
                         [['ولی', 'برای', 'پردازش', '،', 'جدا', 'بهتر', 'نیست', '؟']])

    def test_stem(self):
        """
        Returns:
            None
        """
        self.config['text'] = self.read('fixtures/test_stem.txt')
        self.hazm = HAZMPreprocessor(self.config)
        self.hazm.sent_tokenize()
        self.hazm.word_tokenize()
        self.assertEqual(self.hazm.stem(), [['کتاب']])

    def test_lemmatize(self):
        """
        Returns:
            None
        """
        self.config['text'] = self.read('fixtures/test_lemmatize.txt')
        self.hazm = HAZMPreprocessor(self.config)
        self.hazm.sent_tokenize()
        self.hazm.word_tokenize()
        self.assertEqual(self.hazm.lemmatize(), [['رو']])

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
