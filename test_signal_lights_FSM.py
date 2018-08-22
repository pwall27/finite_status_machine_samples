import unittest
from signal_lights_FSM import run_fsm


class TestSignalLightsFSM(unittest.TestCase):
    def test_keep_red(self):
        self.assertEqual(run_fsm("red", 0), "red")

    def test_keep_green(self):
        self.assertEqual(run_fsm("green", 0), "green")

    def test_keep_yellow(self):
        self.assertEqual(run_fsm("yellow", 0), "yellow")

    def test_red_turn_into_green(self):
        self.assertEqual(run_fsm("red", 1), "green")

    def test_green_turn_into_yellow(self):
        self.assertEqual(run_fsm("green", 1), "yellow")

    def test_yellow_turn_into_red(self):
        self.assertEqual(run_fsm("yellow", 1), "red")
