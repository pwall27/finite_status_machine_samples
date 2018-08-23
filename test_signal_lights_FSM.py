import unittest
from signal_lights_FSM import state_yellow, state_red, state_green
from state_machine import StateMachine


class TestSignalLightsFSM(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSignalLightsFSM, self).__init__(*args, **kwargs)
        self.m = StateMachine()
        self.m.add_state("red", state_red)
        self.m.add_state("green", state_green)
        self.m.add_state("yellow", state_yellow)

    def test_keep_red(self):
        handler = self.m.get_handler("red")
        next_state, next_input = handler(0)
        self.assertEqual(next_state, "red")

    def test_keep_green(self):
        handler = self.m.get_handler("green")
        next_state, next_input = handler(0)
        self.assertEqual(next_state, "green")

    def test_keep_yellow(self):
        handler = self.m.get_handler("yellow")
        next_state, next_input = handler(0)
        self.assertEqual(next_state, "yellow")

    def test_red_turn_into_green(self):
        handler = self.m.get_handler("red")
        next_state, next_input = handler(1)
        self.assertEqual(next_state, "green")

    def test_green_turn_into_yellow(self):
        handler = self.m.get_handler("green")
        next_state, next_input = handler(1)
        self.assertEqual(next_state, "yellow")

    def test_yellow_turn_into_red(self):
        handler = self.m.get_handler("yellow")
        next_state, next_input = handler(1)
        self.assertEqual(next_state, "red")
