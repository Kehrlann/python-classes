from unittest import TestCase


class BaseTestCase(TestCase):

    def setUp(self):
        print("\n")

    def tearDown(self):
        print()

    def run_tests(self, test_cases, test_function):
        errors = 0
        for *args, expected in test_cases:
            result = test_function(*args)
            if result == expected:
                self.ok_message(args, expected)
            else:
                self.error_message(args, expected, result)
                errors += 1

        if errors:
            self.fail(f"{errors} errors / {len(test_cases)} total")

    def ok_message(self, args, expected):
        print(f"OK    : args {args}, result {expected}")

    def error_message(self, args, expected, result):
        print(
            f"ERROR : args {args}, result should be {expected}, but was {result}")
