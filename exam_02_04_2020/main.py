from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository

magic_card = MagicCard("Magic Card")
trap_card = TrapCard("Trap Card")

first_user_beginner = Beginner("Beginner first")
second_user_beginner = Beginner("Beginner second")
first_user_advanced = Advanced("Advanced first")
second_user_advanced = Advanced("Advanced second")

player_repo = PlayerRepository()
player_repo.add(first_user_beginner)
player_repo.add(second_user_beginner)
player_repo.add(first_user_advanced)
player_repo.add(second_user_advanced)
player_repo.remove("Advanced second")
player_repo.add(second_user_advanced)
print(player_repo.find("Beginner first"))

card_repo = CardRepository()
card_repo.add(magic_card)
card_repo.add(trap_card)
card_repo.remove("Trap Card")
card_repo.add(trap_card)
print(card_repo.find("Trap Card"))


controller = Controller()
controller.add_player("Beginner", "beginner")
print(controller.add_player("Advanced", "advanced"))
controller.add_card("Magic", "magic")
controller.add_card("Trap", "trap2")
controller.add_card("Trap", "trap3")
print(controller.add_card("Trap", "trap"))
controller.add_player_card("beginner", "magic")
controller.add_player_card("advanced", "magic")
print(controller.add_player_card("beginner", "trap"))
print(controller.add_player_card("beginner", "trap2"))
print(controller.add_player_card("beginner", "trap3"))
print(controller.fight("beginner", "advanced"))
print(controller.report())
