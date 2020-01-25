import unittest
from Catdetect import main

class MyTestCase(unittest.TestCase):
    def test_noCat(self):
        source = "images\cat_7.jpg"
        result = main(source)
        self.assertEqual(result, False)

    def test_Cat(self):
        source = "images\cat_4.jpg"
        result = main(source)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
