import example
import unittest


class testCases(unittest.TestCase):

    def test_add(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(example.sub(3, 2), 1)

    if __name__ == '__main__':
        unittest.main()
