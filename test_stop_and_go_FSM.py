import unittest
from stop_and_go_FSM import doing_pollution


class TestStopAndGoFSM(unittest.TestCase):
    def test_keep_stop_without_trucks_waiting(self):
        state, pollution = doing_pollution("stop", False, 0)
        self.assertFalse(pollution)
        self.assertEqual(state, "stop")

    def test_keep_going_without_trucks_waiting(self):
        state, pollution = doing_pollution("go", False, 0)
        self.assertFalse(pollution)
        self.assertEqual(state, "go")

    def test_keep_stop_with_trucks_waiting(self):
        state, pollution = doing_pollution("stop", True, 0)
        self.assertTrue(pollution)
        self.assertEqual(state, "stop")

    def test_keep_going_with_trucks_waiting(self):
        state, pollution = doing_pollution("go", True, 0)
        self.assertFalse(pollution)
        self.assertEqual(state, "go")

    def test_stop_turn_to_go_without_trucks_waiting(self):
        state, pollution = doing_pollution("stop", False, 1)
        self.assertFalse(pollution)
        self.assertEqual(state, "go")

    def test_go_turn_to_stop_without_trucks_waiting(self):
        state, pollution = doing_pollution("go", False, 1)
        self.assertFalse(pollution)
        self.assertEqual(state, "stop")

    def test_stop_turn_to_go_with_trucks_waiting(self):
        state, pollution = doing_pollution("stop", True, 1)
        self.assertFalse(pollution)
        self.assertEqual(state, "go")

    def test_go_turn_to_stop_with_trucks_waiting(self):
        state, pollution = doing_pollution("go", True, 1)
        self.assertFalse(pollution)
        self.assertEqual(state, "stop")
