import unittest
from problem_session_1 import LinkedList

class TestCases(unittest.TestCase):
    def setUp(self):
        """This runs BEFORE each test method"""
        print("Setting up test...")
        self.ll = LinkedList()  # Available in all test methods
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)

    def tearDown(self):  # ← Runs AFTER each test method  
        """Clean up after tests"""
        pass  # Usually for closing files, DB connections, etc.
    
    def test_length(self):  # ← Test method (must start with 'test_')
        """Test the __len__ method"""
        self.assertEqual(len(self.ll), 3)  # ← Assertion

    def test_string_representation(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.ll), "1 -> 2 -> 3")

if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)