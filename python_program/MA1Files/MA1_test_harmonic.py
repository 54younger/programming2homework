# https://docs.python.org/3/library/unittest.html
import unittest
import importlib
import MA1

importlib.reload(MA1)


class Test(unittest.TestCase):

    def test_harmonic(self):
        print('\nTests harmonic')
        self.assertAlmostEqual(MA1.harmonic(1), 1.)
        self.assertAlmostEqual(MA1.harmonic(2), 1.5)
        self.assertAlmostEqual(MA1.harmonic(3), 1.5 + 1/3)
        self.assertAlmostEqual(MA1.harmonic(4), 1.5 + 1/3 + 1/4)


if __name__ == "__main__":
    unittest.main()
