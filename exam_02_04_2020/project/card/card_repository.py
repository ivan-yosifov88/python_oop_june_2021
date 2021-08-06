from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    @staticmethod
    def get_card(name, list_of_obj):
        return [obj for obj in list_of_obj if obj.name == name]

    def add(self, card: Card):
        current_card = self.get_card(card.name, self.cards)
        if current_card:
            raise ValueError(f"Card {card.name} already exists!")

        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        filtered_cards = self.get_card(card, self.cards)
        if filtered_cards:
            card_to_remove = filtered_cards[0]
            self.cards.remove(card_to_remove)
            self.count -= 1

    def find(self, name: str):
        filtered_cards = self.get_card(name, self.cards)
        if filtered_cards:
            return filtered_cards[0]

    @property
    def sum_of_cards_damage(self):
        return sum([card.health_points for card in self.cards])