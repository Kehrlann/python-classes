import unittest
from student import Student
from testing_utils import BaseTestCase

achille = Student("Achille", "Talon")


def topics(student, *args):
    for topic, grade in args:
        student.add_grade(topic, grade)
    return set(student.followed_topics())


class TestStudentTopics(BaseTestCase):

    def test_student_topics(self):
        self.__preflight_checks()
        one = Student("one", "one")
        two = Student("two", "two")

        test_cases = [
            (one, ("History", 10.), ("History", 12.),
             ("Math", 10.), {"History", "Math"}),
            (two, ("French", 10.), {"French"}),
        ]
        self.run_tests(test_cases, topics)

    def ok_message(self, args, expected):
        print(
            f"OK    : For grades {args[1:]} -> topics \"{expected}\"")

    def error_message(self, args, expected, result):
        _, *grades = args
        print(
            f"ERROR: For grades {args[1:]} -> topics should be \"{expected}\", but were \"{result}\"")

    def __preflight_checks(self):
        # Add grade exists
        if "add_grade" not in Student.__dict__:
            print("ERROR: there is no 'add_grade' method in class 'Student'")
            self.fail("ERROR: there is no 'add_grade' method in class 'Student'")

        # Add grade does not throw
        try:
            sample_student = Student("Sample", "Student")
            sample_student.add_grade("topic", 10.)
        except Exception as error:
            print("ERROR: 'add_grade' does not work ... Error was:")
            print(error)
            self.fail(
                f"ERROR: 'add_grade' does not work ... Error was: {error}")

        # Followed topics exists
        if "followed_topics" not in Student.__dict__:
            print("ERROR: there is no 'followed_topics' method in class 'Student'")
            self.fail(
                "ERROR: there is no 'followed_topics' method in class 'Student'")

        # Followed topics does not throw
        sample_student = Student("Sample", "Student")
        sample_student.add_grade("topic", 10.)
        try:
            sample_student.followed_topics()
        except Exception as error:
            print("ERROR: 'followed_topics' does not work ... Error was:")
            print(error)
            self.fail(
                f"ERROR: 'followed_topics' does not work ... Error was: {error}")

        # Followed topics returns something
        if not sample_student.followed_topics():
            print(
                "ERROR: 'followed_topics' should return an iterable, not something False")
            self.fail(
                "ERROR: 'followed_topics' should return an iterable, not something False")


if __name__ == '__main__':
    unittest.main()
