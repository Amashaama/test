from string_utils import reverse_string
from string_utils import capitalize_string
from string_utils import is_capitalized
import unittest

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string('mochi'),'ihcom')
    def test_cappitalize_string(self):
        self.assertEqual(capitalize_string('hello'),'Hello')
    def test_is_capitalized(self):
        self.assertTrue(is_capitalized('Hello'))

if __name__ =='__main__':
    unittest.main()