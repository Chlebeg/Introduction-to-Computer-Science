from zadanie_7 import  line_checker
import unittest
import pytest

class Test_program(unittest.TestCase):
    def test_line_checker(self):
        self.assertTrue(line_checker(2, [[1,0],[0,1]]))
        self.assertFalse(line_checker(2, [[0, 1], [0, 1]]))

        self.assertFalse(line_checker(3, [[0, 1, 1], [0, 1, 1], [0, 1, 1]]))
        self.assertTrue(line_checker(3, [[0, 1, 1], [1, 0, 1], [1, 1, 0]]))
        self.assertTrue(line_checker(3, [[0, 1, 1], [1, 1, 0], [1, 0, 1]]))

        self.assertTrue(line_checker(7, [[0, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1],[1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 0]]))

def test_line_checker():
    assert line_checker(2, [[1,0],[0,1]])
    assert not line_checker(2, [[0, 1], [0, 1]])

    assert not line_checker(3, [[0, 1, 1], [0, 1, 1], [0, 1, 1]])
    assert line_checker(3, [[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    assert line_checker(3, [[0, 1, 1], [1, 1, 0], [1, 0, 1]])

    assert line_checker(7, [[0, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1],[1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 0]]) == True

if __name__ == '__main__':
    unittest.main()