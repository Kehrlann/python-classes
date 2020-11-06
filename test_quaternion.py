import unittest
from quaternion import Quaternion
from random import randint


class TestQuaternion(unittest.TestCase):

    def test_repr(self):
        self.assertEqual(repr(Quaternion(1, 0, 0, 0)), "1")
        self.assertEqual(repr(Quaternion(0, 2, 0, 0)), "2i")
        self.assertEqual(repr(Quaternion(0, 0, 3, 0)), "3j")
        self.assertEqual(repr(Quaternion(0, 0, 0, 4)), "4k")
        self.assertEqual(
            repr(Quaternion(1.5, 2.5, 3.5, 4)), "1.5 + 2.5i + 3.5j + 4k"
        )
        self.assertEqual(repr(Quaternion(1, -1, 0, 0)), "1 + -1i")

    def test_equals(self):
        self.assertEqual(Quaternion(1, 0, 0, 0), Quaternion(1, 0, 0, 0))
        self.assertEqual(Quaternion(0, 2, 0, 0), Quaternion(0, 2, 0, 0))
        self.assertEqual(Quaternion(0, 0, 3, 0), Quaternion(0, 0, 3, 0))
        self.assertEqual(Quaternion(0, 0, 0, 4), Quaternion(0, 0, 0, 4))
        self.assertEqual(Quaternion(1, 2, 3, 4), Quaternion(1, 2, 3, 4))
        self.assertNotEqual(Quaternion(0, 0, 1, 4), Quaternion(0, 0, 1, 3))

    def test_add(self):
        a = Quaternion(0, 0, 1, 4)
        b = Quaternion(8, 0, -2, 0)
        self.assertEqual(repr(a + b), "8 + -1j + 4k")

    def test_multiply_simple(self):
        a = Quaternion(1, 0, 0, 0)
        b = Quaternion(0, 1, 0, 0)
        c = Quaternion(0, 0, 1, 0)
        d = Quaternion(0, 0, 0, 1)

        self.assertEqual(repr(a * a), "1")
        self.assertEqual(repr(b * b), "-1")
        self.assertEqual(repr(c * c), "-1")
        self.assertEqual(repr(d * d), "-1")
        self.assertEqual(repr(b * c * d), "-1")

    def test_multiply(self):
        self.assertEqual(
            repr(Quaternion(-4, 1, 4, 5) * Quaternion(4, -4, 2, 5)),
            "-45 + 30i + -17j + 18k"
        )
        self.assertEqual(
            repr(Quaternion(4, 4, -1, -1) * Quaternion(0, -1, -1, -2)),
            "1 + -3i + 5j + -13k"
        )
        self.assertEqual(
            repr(Quaternion(-1, -1, 5, 3) * Quaternion(2, -3, 2, -1)),
            "-12 + -10i + -2j + 20k"
        )
        self.assertEqual(
            repr(Quaternion(1, -5, 2, 1) * Quaternion(-2, -5, -2, -5)),
            "-18 + -3i + -36j + 13k"
        )
        self.assertEqual(
            repr(Quaternion(-5, 1, -2, -3) * Quaternion(-2, 1, 2, -3)),
            "4 + 5i + -6j + 25k"
        )
        self.assertEqual(
            repr(Quaternion(5, 4, 2, -3) * Quaternion(3, 0, 3, -3)),
            "15i + 33j + -12k"
        )
        self.assertEqual(
            repr(Quaternion(-1, -5, -3, -3) * Quaternion(-2, 4, -4, 4)),
            "22 + -18i + 18j + 34k"
        )
        self.assertEqual(
            repr(Quaternion(1, 1, 4, -1) * Quaternion(2, -3, 5, 1)),
            "-14 + 8i + 15j + 16k"
        )
        self.assertEqual(
            repr(Quaternion(-2, -1, -1, -5) * Quaternion(3, 0, 3, -4)),
            "-23 + 16i + -13j + -10k"
        )
        self.assertEqual(
            repr(Quaternion(1, 2, 3, 4) * Quaternion(2, -2, -3, -5)),
            "35 + -1i + 5j + 3k"
        )


if __name__ == '__main__':
    unittest.main()
