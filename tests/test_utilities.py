import unittest
from utilities import greet, get_average

class test_greet(unittest.TestCase):
    def test_greet_kenny(self):
        """
        GIVEN the greet function from utilites
        WHEN the greet function is called with the parameter "Kenny"
        THEN the function should return the string "Hello, Kenny!"
        """

        name = "Kenny"
        expected_result = "Hello, Kenny!"
        result = greet(name)
        self.assertEqual(result, expected_result)

    def test_greet_emptystring(self):
        """
        GIVEN the greet function from utilites
        WHEN the greet function is called with the parameter "" (empty string)
        THEN the function should return the string "Hello, stranger."
        """
        #ASSIGNMENT: you will write the code to test the GIVEN/WHEN/THEN above.

        self.assertEqual(0, 1) #comment this out after you write the test.

class test_get_average(unittest.TestCase):
    def test_get_average(self):
        """
        GIVEN the greet get_average from utilites
        WHEN the greet get_average is called with the parameters 2 and 4
        THEN the function should return the float 3.0
        """
        #ASSIGNMENT: you will write the code to test the GIVEN/WHEN/THEN above.
        
        self.assertEqual(0, 1) #comment this out after you write the test.


        
