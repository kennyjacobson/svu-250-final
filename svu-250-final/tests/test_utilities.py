import unittest
from utilities import greet, get_average

class test_greet(unittest.TestCase):
    def test_greet_kenny(self):
        """
        GIVEN the greet function from utilites
        WHEN the greet function is called with the parameter "Jake"
        THEN the function should return the string "Hello, Jake!"
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
        name = ""
        expected_result = "Hello, stranger."
        result = greet(name)
        self.assertEqual(result, expected_result)
       
        #ASSIGNMENT: you will write the code to test the GIVEN/WHEN/THEN above.
        #TESTING the REPO's new config - another test - 3rd test.

        #self.assertEqual(0, 1) #comment this out after you write the test.

class test_get_average(unittest.TestCase):
    def test_get_average(self):
        num1 = 2
        num2 = 4
        result = get_average(num1, num2)
        expected_result = 3.0
        self.assertEqual(result, expected_result) 


        """
        GIVEN the greet get_average from utilites
        WHEN the greet get_average is called with the parameters 2 and 4
        THEN the function should return the float 3.0
        """
        #ASSIGNMENT: you will write the code to test the GIVEN/WHEN/THEN above.
        
        #self.assertEqual(0, 1) #comment this out after you write the test.


        
