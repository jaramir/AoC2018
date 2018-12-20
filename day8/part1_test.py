import unittest
from part1 import parse, flatten

empty = {"child": [], "metadata": []}
node_with_child = {"child": [empty], "metadata": []}

class Part1TestCase(unittest.TestCase):
    def test_parse_empty_node(self):
        self.assertEqual(parse([0, 0]), empty)

    def test_parse_node_with_metadata(self):
        self.assertEqual(parse([0, 2, 4, 6]), {"child": [], "metadata": [4, 6]})

    def test_parse_node_with_child(self):
        self.assertEqual(parse([1, 0, 0, 0]), node_with_child)

    def test_flatten_empty_node(self):
        self.assertEqual(flatten(empty), [empty])

    def test_flatten_node_with_child(self):
        self.assertEqual(flatten(node_with_child), [node_with_child, empty])

if __name__ == '__main__':
    unittest.main()
