import unittest
from student import Student
from testing_utils import BaseTestCase

achille = Student("Achille", "Talon")


def average(student, topic):
    return student.compute_average(topic)


class TestStudentTopics(BaseTestCase):

    def test_student_topics(self):
        self.__preflight_checks()

        one = Student("one", "one")
        one.add_grade("History", 10.)
        one.add_grade("History", 12.)
        two = Student("two", "two")
        two.add_grade("Math", 12.)

        test_cases = [
            (one, "History", 11.),
            (one, "French", -1.),
            (two, "Math", 12.)
        ]
        self.run_tests(test_cases, average)

    def ok_message(self, args, expected):
        print(
            f"OK    : For grades {args[1:]} -> topics \"{expected}\"")

    def error_message(self, args, expected, result):
        _, *grades = args
        print(
            f"ERROR: For grades {args[1:]} -> topics should be \"{expected}\", but were \"{result}\"")

    def __preflight_checks(self):
        # Add grade exists
        if "compute_average" not in Student.__dict__:
            print("ERROR: there is no 'compute_average' method in class 'Student'")
            self.fail(
                "ERROR: there is no 'compute_average' method in class 'Student'")


if __name__ == '__main__':
    unittest.main()
