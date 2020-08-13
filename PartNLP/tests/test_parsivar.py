"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
import unittest
from PartNLP.models.pre_processors.parsivar_preprocessor import PARSIVARPreprocessor
from PartNLP.models.helper import configuration


class TestHazm(unittest.TestCase):
    """
            UnitTest
    """
    def setUp(self):
        super(TestHazm, self).__init__()
        self.config = configuration.get_config()

    def test_normalize(self):
        """
        Returns:
            None
        """
        self.config['text'] = self.read('fixtures/test_normalize.txt')
        self.parsivar = PARSIVARPreprocessor(self.config)
        self.assertEqual(' '.join(self.parsivar.normalize()),
                         'اصلاح نویسه‌ها و استفاده از نیم‌فاصله پردازش را آسان می‌کند')

    def test_sent_tokenize(self):
        """
        Returns:
            None
        """
        self.config['text'] = self.read('fixtures/test_sentence_tokenize.txt')
        self.parsivar = PARSIVARPreprocessor(self.config)
        self.assertEqual(self.parsivar.sent_tokenize(),
                         ['ما هم برای وصل کردن آمدیم !', ' ولی برای پردازش، جدا بهتر نیست ؟'])

    def test_word_tokenize(self):
        """
        Returns:
            None
        """
        self.config['text'] = self.read('fixtures/test_word_tokenize.txt')
        self.parsivar = PARSIVARPreprocessor(self.config)
        self.parsivar.sent_tokenize()
        self.assertEqual(self.parsivar.word_tokenize(),
                         [['ولی', 'برای', 'پردازش،', 'جدا', 'بهتر', 'نیست', '؟']])

    def test_stem(self):
        """
        Returns:
            None
        """
        self.config['text'] = self.read('fixtures/test_stem.txt')
        self.parsivar = PARSIVARPreprocessor(self.config)
        self.parsivar.sent_tokenize()
        self.parsivar.word_tokenize()
        self.assertEqual(self.parsivar.stem(), [['کتاب']])

    def read(self, path):
        """
        Args:
            path:
        Returns:
            text
        """
        with open(path, 'r') as file:
            text = file.read()
        return text


if __name__ == '__main__':
    unittest.main()
