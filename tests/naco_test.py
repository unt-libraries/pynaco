import os
import unittest

from pynaco import naco
from ddt import ddt, data, unpack

# Absolute path to the data directory
DATA_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')


def standard_data():
    """Data provider method for the normalize function."""
    script = open(os.path.join(DATA_PATH, 'NACO.script'))
    check = open(os.path.join(DATA_PATH, 'NACOstandard.check'))

    # Create a list of tuples in the form of
    # (data to be normalized, expected output)
    standard = zip(script.readlines(), check.read().splitlines())

    script.close()
    check.close()

    return standard


def simplified_data():
    """Data provider method for the normalizeSimplified function."""
    script = open(os.path.join(DATA_PATH, 'NACO.script'))
    check = open(os.path.join(DATA_PATH, 'NACOsimplified.check'))

    # Create a list of tuples in the form of
    # (data to be normalized, expected output)
    simplified = zip(script.readlines(), check.read().splitlines())

    script.close()
    check.close()

    return simplified


@ddt
class NACOTest(unittest.TestCase):

    def test_sending_bytes_not_string(self):
        self.assertEqual('texas', naco.normalize(b'Texas', True))

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

    def test_leading_and_commas_remove(self):
        self.assertEqual('a a',
                         naco.normalize("'\x1fa,,A,A'", 0))

    def test_leading_and_commas_retain(self):
        self.assertEqual(', a a',
                         naco.normalize("'\x1fa,,A,A'", 1))

    @unpack
    @data(*standard_data())
    def test_normalize(self, value, expected):
        """Test the normalize function with the using the
        standard_data parameters.
        """
        self.assertEqual(expected, naco.normalize(value, True))

    @unpack
    @data(*simplified_data())
    def test_normalizeSimplified(self, value, expected):
        """Test the normalizeSimplified function with the using the
        simplified_data parameters.
        """
        self.assertEqual(expected, naco.normalizeSimplified(value))


def suite():
    test_suite = unittest.makeSuite(NACOTest, 'test')
    return test_suite


if __name__ == '__main__':
    unittest.main()
