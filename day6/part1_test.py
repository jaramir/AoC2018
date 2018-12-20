import unittest
from part1 import step

class Part1(unittest.TestCase):
    #                               A
    #                  A           AAA
    #     A     ->    AAA    ->   AAAAA
    #                  A           AAA
    #                               A
    def test_cells_expand_each_step(self):
        cells1 = [
            [(0, 0)]
        ]
        cells2 = step(cells1)
        cells3 = step(cells2)
        self.assertItemsEqual([
            ( 0,  0),
            (-1,  0),
            ( 1,  0),
            ( 0,  1),
            ( 0, -1)
        ], cells2[0])
        self.assertItemsEqual([
            ( 0,  0),
            (-1,  0),
            ( 1,  0),
            ( 0,  1),
            ( 0, -1),
            (-2,  0),
            ( 2,  0),
            ( 0,  2),
            ( 0, -2),
            (-1, -1),
            (-1,  1),
            ( 1, -1),
            ( 1,  1)
        ], cells3[0])

    #                              A B
    #                 A B         AA BB
    #    A B    ->   AA BB   ->  AAA BBB
    #                 A B         AA BB
    #                              A B
    def test_two_cells_of_different_familes_expand(self):
        cells1 = [
            [(0, 0)],
            [(2, 0)]
        ]
        cells2 = step(cells1)
        self.assertItemsEqual([
            ( 0,  0),
            (-1,  0),
            ( 0,  1),
            ( 0, -1)
        ], cells2[0])
        self.assertItemsEqual([
            ( 2,  0),
            ( 2,  1),
            ( 2, -1),
            ( 3,  0)
        ], cells2[1])

if __name__ == '__main__':
    unittest.main()
