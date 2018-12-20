import unittest
from part2 import value

six = {"child": [], "metadata": [1, 2, 3]}
one = {"child": [], "metadata": [1]}

class Part2TestCase(unittest.TestCase):
    def test_value_leaf_node_is_metadata_sum(self):
        self.assertEqual(value(six), 6)

    def test_value_node_with_single_child_referred_once(self):
        node = {
            "child": [six],
            "metadata": [1]
        }
        self.assertEqual(6, value(node))

    def test_value_node_with_multiple_child_references(self):
        node = {
            "child": [six, one],
            "metadata": [1, 1, 2]
        }
        self.assertEqual(13, value(node))

    def test_value_node_with_broken_references(self):
        node = {
            "child": [six, one],
            "metadata": [0, 3, 4, 5]
        }
        self.assertEqual(0, value(node))

if __name__ == '__main__':
    unittest.main()
