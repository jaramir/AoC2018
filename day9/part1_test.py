import unittest

from part1 import Game


class Part1TestCase(unittest.TestCase):
    def test_game_start_with_marble_zero(self):
        self.assertItemsEqual([0], Game().get_marbles())

    def test_marbles_are_added_one_place_after_current_and_become_current(self):
        game = Game()
        game.turn()
        self.assertItemsEqual([1, 0], game.get_marbles())
        game.turn()
        self.assertItemsEqual([2, 1, 0], game.get_marbles())
        game.turn()
        self.assertItemsEqual([3, 0, 2, 1], game.get_marbles())
        game.turn()
        self.assertItemsEqual([4, 2, 1, 3, 0], game.get_marbles())

    def test_marbles_divisible_by_23_are_different(self):
        game = Game()
        game.play_until(22)
        self.assertItemsEqual([22, 11, 1, 12, 6, 13, 3, 14, 7, 15, 0, 16, 8, 17, 4, 18, 9, 19, 2, 20, 10, 21, 5], game.get_marbles())
        game.turn()
        self.assertItemsEqual([19, 2, 20, 10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15, 0, 16, 8, 17, 4, 18], game.get_marbles())

    def test_23th_turns_score_points_to_current_player(self):
        game = Game(players=9)
        game.play_until(23)
        self.assertEqual([0, 0, 0, 0, 32, 0, 0, 0, 0], game.points)

    def test_real_world_examples(self):
        self.assertEqual(2764, max(Game(players=17).play_until(1104).points))
        self.assertEqual(8317, max(Game(players=10).play_until(1618).points))
        self.assertEqual(37305, max(Game(players=30).play_until(5807).points))
        self.assertEqual(54718, max(Game(players=21).play_until(6111).points))
        self.assertEqual(146373, max(Game(players=13).play_until(7999).points))
        self.assertEqual(384205, max(Game(players=476).play_until(71431).points))


if __name__ == '__main__':
    unittest.main()
