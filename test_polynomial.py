
import unittest
from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):

    def test_repr(self):
        self.assertEqual(repr(Polynomial()), '0')
        self.assertEqual(repr(Polynomial(4)), '4')
        self.assertEqual(repr(Polynomial(0, 2, 0, 1, 0)), '2X^3 + X')

    def test_degree(self):
        self.assertEqual(Polynomial().degree, 0)
        self.assertEqual(Polynomial(4).degree, 0)
        self.assertEqual(Polynomial(0, 2, 0, 1, 0).degree, 3)

    def test_equals(self):
        self.assertEqual(Polynomial(), Polynomial(0))
        self.assertEqual(Polynomial(1, 0, 3), Polynomial(0, 0, 1, 0, 3))


if __name__ == '__main__':
    unittest.main()
