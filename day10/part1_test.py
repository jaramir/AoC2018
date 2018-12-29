import unittest
from part1 import parse, render, find_smallest_evolution

class Part1TestCase(unittest.TestCase):
    def test_run(self):
        state = parse("test.input")
        evo = find_smallest_evolution(state)
        render(evo)

if __name__ == '__main__':
    unittest.main()
