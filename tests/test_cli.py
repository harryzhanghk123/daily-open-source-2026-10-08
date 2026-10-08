import unittest

from planmaker.cli import prioritize


class PrioritizeTests(unittest.TestCase):
    def test_urgent_tasks_come_first(self):
        self.assertEqual(prioritize(["read", "! deploy"])[0], (1, "! deploy"))

    def test_ties_preserve_input_order(self):
        self.assertEqual(prioritize(["aa", "bb"]), [(0, "aa"), (1, "bb")])


if __name__ == "__main__":
    unittest.main()
