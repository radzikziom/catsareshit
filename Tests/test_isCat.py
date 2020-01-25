import unittest
from Catdetect import is_cat


class MyTestCase(unittest.TestCase):
    def test_falseCat(self):
        source = []
        result = is_cat(source)
        self.assertEqual(result, False)

    def test_trueCat(self):
        source = [[91, 57, 55, 55]]
        result = is_cat(source)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
