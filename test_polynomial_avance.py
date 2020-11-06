
import unittest
from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):
    def test_derivative(self):
        P = Polynomial(1, 2, 3)
        self.assertEqual(P.derivative(), Polynomial(2, 2))
        self.assertEqual(P.derivative().derivative(), Polynomial(2))

    def test_add(self):
        self.assertEqual(
            Polynomial(1, 2, 3) + Polynomial(3, 2, 1),
            Polynomial(4, 4, 4)
        )

        self.assertEqual(
            Polynomial(1, 2, 3) + Polynomial(4, 4),
            Polynomial(1, 6, 7)
        )

    def test_multiply(self):
        self.assertEqual(
            Polynomial(3, 2, 1) * Polynomial(3, 1, 2),
            Polynomial(9, 9, 11, 5, 2)
        )
        self.assertEqual(
            Polynomial(3, 2, 1) * Polynomial(1, 2),
            Polynomial(3, 8, 5, 2)
        )

    def test_call(self):
        P = Polynomial(1, 2, 3)
        self.assertEqual(P(10), 123)
        self.assertEqual(P(100), 10203)


if __name__ == '__main__':
    unittest.main()
