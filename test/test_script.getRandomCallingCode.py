import unittest
from generate import getRandomCallingCode
class TestScript(unittest.TestCase):
    pass
class TestScript(unittest.TestCase):
    def test_getRandomCallingCode(self):
        # Call the getRandomCallingCode function
        calling_code = getRandomCallingCode()

        # Assert that the calling code is one of the expected values
        expected_values = ["+46", "+47", "+358", "+45"]
        self.assertIn(calling_code, expected_values)