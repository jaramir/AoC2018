import unittest
from part1 import react

class Part1(unittest.TestCase):
    def test_two_opposite_units_annihilate(self):
        self.assertEqual("", react("aA"))

    def test_two_same_units_remain(self):
        self.assertEqual("aa", react("aa"))

    def test_two_different_units_remain(self):
        self.assertEqual("ab", react("ab"))
        self.assertEqual("Ab", react("Ab"))

    def test_two_chain_reactions(self):
        self.assertEqual("", react("bAaB"))

    def test_a_more_complex_example(self):
        self.assertEqual("dabCBAcaDA", react("dabAcCaCBAcCcaDA"))

    def test_wrap_around_reaction_not_allowed(self):
        self.assertEqual("Bxxxb", react("AaBxxxb"))

if __name__ == '__main__':
    unittest.main()
