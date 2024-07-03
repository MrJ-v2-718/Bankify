import random
import unittest
from bankify import deposit_math, withdrawal_math


class TestBankify(unittest.TestCase):

    def test_deposit_math_positive(self):
        # Generates deposit between 0 and 1000 dollars
        rounded_deposit = random.random() * 1000

        # Generates balance between 0 and 10,000 dollars
        current_balance = random.random() * 10000

        # Calls deposit_math() and stores result
        result = deposit_math(rounded_deposit, current_balance)

        # Calculates the expected result
        expected_result = current_balance + rounded_deposit

        # UnitTest Assertion
        self.assertEqual(result, expected_result)

    def test_deposit_math_negative(self):
        # Generates negative deposit between 0 and -1000 dollars
        rounded_deposit = random.random() * -1000

        # Generates balance between 0 and 10,000 dollars
        current_balance = random.random() * 10000

        # Calls deposit_math() and stores result
        result = deposit_math(rounded_deposit, current_balance)

        # Calculates the expected result
        expected_result = current_balance + rounded_deposit

        # UnitTest Assertion
        self.assertEqual(result, expected_result)

    def test_withdrawal_math_positive(self):
        # Generates withdrawal between 0 and 1000 dollars
        rounded_withdrawal = random.random() * 1000

        # Generates balance between 0 and 10,000 dollars
        current_balance = random.random() * 10000

        # Calls withdrawal_math() and stores result
        result = withdrawal_math(rounded_withdrawal, current_balance)

        # Calculates the expected result
        expected_result = current_balance - rounded_withdrawal

        # UnitTest Assertion
        self.assertEqual(result, expected_result)

    def test_withdrawal_math_negative(self):
        # Generates negative withdrawal between 0 and -1000 dollars
        rounded_withdrawal = random.random() * -1000

        # Generates balance between 0 and 10,000 dollars
        current_balance = random.random() * 10000

        # Calls withdrawal_math() and stores result
        result = withdrawal_math(rounded_withdrawal, current_balance)

        # Calculates the expected result
        expected_result = current_balance - rounded_withdrawal

        # UnitTest Assertion
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
