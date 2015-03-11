import unittest
from pynaco import naco


class NACOTest(unittest.TestCase):

    def test_capitalization_first_letter(self):
        self.assertEqual('title', naco.normalize("Title", True))

    def test_capitalization_last_letter(self):
        self.assertEqual('title', naco.normalize("titlE", True))

    def test_capitalization_mixed_letters(self):
        self.assertEqual('title', naco.normalize("TiTlE", True))

    def test_hyphen(self):
        self.assertEqual('texas history',
                         naco.normalize("Texas-History", True))

    def test_double_hypen(self):
        self.assertEqual('texas history',
                         naco.normalize("Texas--History", True))

    def test_triple_hypen(self):
        self.assertEqual('texas history',
                         naco.normalize("Texas---History", True))

    def test_double_hypen_spaces(self):
        self.assertEqual('texas history',
                         naco.normalize("Texas -- History", True))

    def test_trailing_period(self):
        self.assertEqual('texas history',
                         naco.normalize("Texas -- History.", True))


def suite():
    test_suite = unittest.makeSuite(NACOTest, 'test')
    return test_suite

if __name__ == '__main__':
    unittest.main()
