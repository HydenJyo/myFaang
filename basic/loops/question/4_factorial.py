#Write a program to find factorial of a number

def factorial(n):
    a = 0
    #Write the code here..
    return a

import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual = factorial(5)
        expected = 120
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual = factorial(4)
        expected = 24
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual = factorial(0)
        expected = 1
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = factorial(10)
        expected = 3628800
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)