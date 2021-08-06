import unittest

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def test_init_method_when_all_correct__should_set(self):
        repo = PlayerRepository()
        self.assertEqual(0, repo.count)
        self.assertEqual([], repo.players)

    def test_add__when_player_name_in_player_list__should_raise_ValueError(self):
        beginner = Beginner("Test")
        repo = PlayerRepository()
        repo.players.append(beginner)
        with self.assertRaises(ValueError) as message:
            repo.add(beginner)
        self.assertEqual(f"Player {beginner.username} already exists!", str(message.exception))

    def test_add__when_player_name_not_in_player_list__should_append_player(self):
        beginner = Beginner("Test")
        repo = PlayerRepository()
        repo.add(beginner)
        self.assertEqual([beginner], repo.players)

    def test_add__when_player_name_not_in_player_list__should_append_increase_count(self):
        beginner = Beginner("Test")
        repo = PlayerRepository()
        repo.add(beginner)
        self.assertEqual([beginner], repo.players)
        self.assertEqual(1, repo.count)

    def test_remove__when_player_name_is_empty_string__should_raise_ValueError(self):
        repo = PlayerRepository()
        player_to_remove = ""
        with self.assertRaises(ValueError) as message:
            repo.remove(player_to_remove)
        self.assertEqual("Player cannot be an empty string!", str(message.exception))

    def test_remove__when_player_name_is_in_list_of_players__should_remove_and_reduce_count(self):
        repo = PlayerRepository()
        player_to_remove = "Test"
        beginner = Beginner(player_to_remove)
        repo.add(beginner)
        self.assertEqual([beginner], repo.players)
        self.assertEqual(1, repo.count)
        repo.remove(player_to_remove)
        self.assertEqual([], repo.players)
        self.assertEqual(0, repo.count)

    def test_find__when_username__should_return_obj(self):
        repo = PlayerRepository()
        player_to_be_found = "Test"
        beginner = Beginner(player_to_be_found)
        repo.add(beginner)
        result = repo.find(player_to_be_found)
        self.assertEqual(beginner,result)


if __name__ == "__main__":
    unittest.main()

