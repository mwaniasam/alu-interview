import unittest
from min_operations import min_operations


class TestMinOperations(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(min_operations(21), 10)
        self.assertEqual(min_operations(19170307), 19170307)
        self.assertEqual(min_operations(972), 30)
        self.assertEqual(min_operations(1), 0)
        self.assertEqual(min_operations(0), 0)

    def test_invalid_inputs(self):
        self.assertEqual(min_operations(-12), 0)
        self.assertEqual(min_operations(2147483640), 2147483640)
        self.assertEqual(min_operations("string"), 0)
        self.assertEqual(min_operations(3.14), 0)


if __name__ == "__main__":
    unittest.main()
