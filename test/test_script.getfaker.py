import unittest
from generate import getFaker
class TestScript(unittest.TestCase):
    pass
class TestScript(unittest.TestCase):
    def test_getFaker(self):
        fake, current = getFaker()
        self.assertIsNotNone(fake)
        self.assertIsNotNone(current)
