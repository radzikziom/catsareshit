import unittest

from Catdetect import replaceChar


class TestCat(unittest.TestCase):
    def test_replace1(self):
        source = "A\B\C\D\E"
        result = replaceChar(source)
        self.assertEqual(result, "A/B/C/D/E")

    def test_replace2(self):
        source = "a\\b\\c\\d\\e"
        result = replaceChar(source)
        self.assertEqual(result, "a/b/c/d/e")


if __name__ == '__main__':
    unittest.main()
