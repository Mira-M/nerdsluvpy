import unittest, sample.fibber as fib


class FibberTest(unittest.TestCase):

    def test_first_10(self):
        self.assertEqual(fib.fibber(0), 0)
        self.assertEqual(fib.fibber(1), 1)
        self.assertEqual(fib.fibber(2), 1)
        self.assertEqual(fib.fibber(3), 2)
        self.assertEqual(fib.fibber(4), 3)
        self.assertEqual(fib.fibber(5), 5)
        self.assertEqual(fib.fibber(6), 8)
        self.assertEqual(fib.fibber(7), 13)


if __name__ == '__main__':
    unittest.main()