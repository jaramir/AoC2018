import unittest
from part1 import parse, flatten

empty = {"child": [], "metadata": []}
node_with_child = {"child": [empty], "metadata": []}

class Part1TestCase(unittest.TestCase):
    def test_parse_empty_node(self):
        self.assertEqual(empty, parse([0, 0]))

    def test_parse_node_with_metadata(self):
        self.assertEqual({"child": [], "metadata": [4, 6]}, parse([0, 2, 4, 6]))

    def test_parse_node_with_child(self):
        self.assertEqual(node_with_child, parse([1, 0, 0, 0]))

    def test_flatten_empty_node(self):
        self.assertEqual([empty], flatten(empty))

    def test_flatten_node_with_child(self):
        self.assertEqual([node_with_child, empty], flatten(node_with_child))

if __name__ == '__main__':
    unittest.main()
