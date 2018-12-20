import unittest
from part1 import solve

class Part1(unittest.TestCase):
    def test_task_dependency(self):
        input = [
            ('C', 'A'),
            ('C', 'F'),
            ('A', 'B'),
            ('A', 'D'),
            ('B', 'E'),
            ('D', 'E'),
            ('F', 'E')
            ]
        self.assertEqual('CABDFE', solve(input))

    def test_two_taks(self):
        input = [('A', 'B')]
        self.assertEqual('AB', solve(input))

    def test_two_taks_other_way_around(self):
        input = [('B', 'A')]
        self.assertEqual('BA', solve(input))

if __name__ == '__main__':
    unittest.main()
