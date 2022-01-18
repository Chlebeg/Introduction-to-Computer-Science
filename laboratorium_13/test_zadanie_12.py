import unittest

from unittest.mock import patch, MagicMock

from zadanie_12 import solve_Hanoi_Tower

class Test_program(unittest.TestCase):
    @patch('builtins.print')
    def test_Hanoi_tower_size_3(self, mock_print: MagicMock):
        solve_Hanoi_Tower(3, "A", "B", "C")
        self.assertEqual(mock_print.call_count, 7)

        self.assertEqual(mock_print.mock_calls[3].args[1], 3)
        self.assertEqual(mock_print.mock_calls[3].args[3], 'A')
        self.assertEqual(mock_print.mock_calls[3].args[5], 'C')

    @patch('builtins.print')
    def test_Hanoi_tower_size_5(self, mock_print: MagicMock):
        solve_Hanoi_Tower(5, "A", "B", "C")
        self.assertEqual(mock_print.call_count, 31)

        self.assertEqual(mock_print.mock_calls[15].args[1], 5)
        self.assertEqual(mock_print.mock_calls[15].args[3], 'A')
        self.assertEqual(mock_print.mock_calls[15].args[5], 'C')

if __name__ == '__main__':
    unittest.main()