import unittest
from generate import getRandomCountry 
class TestScript(unittest.TestCase):
    pass
class TestScript(unittest.TestCase):
    def test_getRandomCountry(self):
        # Call the getRandomCountry function
        country = getRandomCountry()

        # Assert that the country is one of the expected values
        expected_values = ["Sverige", "Norge", "Finland", "Danmark"]
        self.assertIn(country, expected_values)