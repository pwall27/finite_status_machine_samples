import unittest

from state_machine import StateMachine
from string_pattern_FSM import state_zero, state_one, state_two, state_three


class TestStringPattern(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestStringPattern, self).__init__(*args, **kwargs)

        self.m = StateMachine()
        self.m.add_state("start_state", state_zero)
        self.m.add_state("first_state", state_one)
        self.m.add_state("second_state", state_two)
        self.m.add_state("third_state", state_three)
        self.m.add_state("last_state", None, end_state=1)
        self.m.add_state("error_state", None, end_state=1)
        self.m.set_start("start_state")

    def test_right_pattern(self):
        self.assertEqual(self.m.run("12@123#"), "reached last_state which is an end state")
        self.assertEqual(self.m.run("@3445#"), "reached last_state which is an end state")
        self.assertEqual(self.m.run("123@5363@968495#"), "reached last_state which is an end state")
        self.assertEqual(self.m.run("123@@968495#"), "reached last_state which is an end state")

    def test_wrong_pattern(self):
        self.assertEqual(self.m.run("12@2345"), "reached error_state which is an end state")
        self.assertEqual(self.m.run("122345#"), "reached error_state which is an end state")
        self.assertEqual(self.m.run("12@23f45#"), "reached error_state which is an end state")
