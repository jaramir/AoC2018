import unittest
from part2 import solve

class Part2Test(unittest.TestCase):
    def test_duration(self):
        input = [
            ('C', 'A'),
            ('C', 'F'),
            ('A', 'B'),
            ('A', 'D'),
            ('B', 'E'),
            ('D', 'E'),
            ('F', 'E')
        ]
        self.assertEqual(15, solve(input, base_cost=0, workers=2))
