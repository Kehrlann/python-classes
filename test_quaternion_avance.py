import unittest
from quaternion import Quaternion


class TestQuaternionAvance(unittest.TestCase):

    def test_add_entiers_complexes_floats(self):
        self.assertEqual(repr(Quaternion(1, 0, -1, 0) + 3.5), "4.5 + -1j")
        self.assertEqual(repr(Quaternion(1, 0, -1, 0) + 3), "4 + -1j")
        self.assertEqual(
            repr(Quaternion(1., 1., 0, 6.) + 2. + 3.j),
            "3.0 + 4.0i + 6.0k"
        )

    def test_equals_entiers_complexes_floats(self):
        self.assertEqual(Quaternion(1, 0, 0, 0), 1)
        self.assertEqual(Quaternion(1.5, 0, 0, 0), 1.5)
        self.assertEqual(Quaternion(1, 0, 0, 0), 1.0)
        self.assertEqual(Quaternion(1, -1, 0, 0), 1 - 1j)

    def test_multiply_entiers_complexes_floats(self):
        self.assertEqual(repr(Quaternion(1, 1, 1, 1) * 2), "2 + 2i + 2j + 2k")
        self.assertEqual(
            repr(Quaternion(1, 1, 1, 1) * 2.), "2.0 + 2.0i + 2.0j + 2.0k"
        )
        self.assertEqual(
            repr(Quaternion(1, 2., 3., 4.) * 5 + 6j),
            "5.0 + 16.0i + 15.0j + 20.0k"
        )


if __name__ == '__main__':
    unittest.main()
