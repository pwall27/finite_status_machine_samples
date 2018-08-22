import unittest
from string_pattern_FSM import match


class TestStringPattern(unittest.TestCase):
    def test_right_pattern(self):
        self.assertTrue(match("12@123#"))
        self.assertTrue(match("@3445#"))
        self.assertTrue(match("123@5363@968495#"))
        self.assertTrue(match("123@@968495#"))

    def test_wrong_pattern(self):
        self.assertFalse(match("12@2345"))
        self.assertFalse(match("122345#"))
        self.assertFalse(match("12@23f45#"))
