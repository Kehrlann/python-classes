import unittest
from student import Student
from testing_utils import BaseTestCase


def student_repr(*args):
    return repr(Student(*args))


class TestStudentName(BaseTestCase):

    def test_student_name(self):
        test_cases = [
            ("Achille", "Talon", "Achille Talon"),
            ("Lucky", "Luke", "Lucky Luke"),
        ]
        self.run_tests(test_cases, student_repr)

    def ok_message(self, args, expected):
        print(
            f"OK    : First name: \"{args[0]}\", last name: \"{args[1]}\" -> student \"{expected}\"")

    def error_message(self, args, expected, result):
        print(
            f"ERROR : First name: \"{args[0]}\", last name: \"{args[1]}\" -> should be \"{expected}\", but was \"{result}\"")


if __name__ == '__main__':
    unittest.main()
