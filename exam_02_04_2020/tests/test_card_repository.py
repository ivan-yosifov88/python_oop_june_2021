import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def test_init_method_when_all_correct__should_set(self):
        repo = CardRepository()
        self.assertEqual(0, repo.count)
        self.assertEqual([], repo.cards)

    def test_add__when_card_name_in_card_list__should_raise_ValueError(self):
        magic_card = MagicCard("Test")
        repo = CardRepository()
        repo.cards.append(magic_card)
        with self.assertRaises(ValueError) as message:
            repo.add(magic_card)
        self.assertEqual(f"Card {magic_card.name} already exists!", str(message.exception))

    def test_add__when_card_name_not_in_card_list__should_append_card(self):
        magic_card = MagicCard("Test")
        repo = CardRepository()
        repo.add(magic_card)
        self.assertEqual([magic_card], repo.cards)

    def test_add__when_card_name_not_in_card_list__should_append_increase_count(self):
        magic_card = MagicCard("Test")
        repo = CardRepository()
        repo.add(magic_card)
        self.assertEqual([magic_card], repo.cards)
        self.assertEqual(1, repo.count)

    def test_remove__when_card_name_is_empty_string__should_raise_ValueError(self):
        repo = CardRepository()
        card_to_remove = ""
        with self.assertRaises(ValueError) as message:
            repo.remove(card_to_remove)
        self.assertEqual("Card cannot be an empty string!", str(message.exception))

    def test_remove__when_card_name_is_in_list_of_card__should_remove_and_reduce_count(self):
        repo = CardRepository()
        card_to_remove = "Test"
        magic_card = MagicCard(card_to_remove)
        repo.add(magic_card)
        self.assertEqual([magic_card], repo.cards)
        self.assertEqual(1, repo.count)
        repo.remove(card_to_remove)
        self.assertEqual([], repo.cards)
        self.assertEqual(0, repo.count)

    def test_find__when_name__should_return_obj(self):
        repo = CardRepository()
        card_to_be_found = "Test"
        magic_card = MagicCard(card_to_be_found)
        repo.add(magic_card)
        result = repo.find(card_to_be_found)
        self.assertEqual(magic_card, result)


if __name__ == "__main__":
    unittest.main()