import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from use_cases.CU09_create_user_screen import CreateUserScreen

class TestCreateUserScreenPasswordValidation(unittest.TestCase):
    def setUp(self):
        self.screen = CreateUserScreen()

    def test_valid_passwords(self):
        valid_passwords = [
            "Abcd#1234",
            "X1!abcdef",
            "Secure$Pass9",
            "HELLO1@you"
        ]
        for pwd in valid_passwords:
            with self.subTest(pwd=pwd):
                self.assertIsNotNone(self.screen._validate_password(pwd), f"Expected valid: {pwd}")

    def test_invalid_passwords(self):
        invalid_passwords = [
            "short1!",         # too short
            "nouppercase1!",   # no uppercase
            "NOLOWERCASE!",    # no digit
            "NoSpecialChar1",  # no special character
            "12345678!",       # no letter
            "        ",        # only spaces
            "",                # empty
        ]
        for pwd in invalid_passwords:
            with self.subTest(pwd=pwd):
                self.assertIsNone(self.screen._validate_password(pwd), f"Expected invalid: {pwd}")

if __name__ == "__main__":
    unittest.main()
