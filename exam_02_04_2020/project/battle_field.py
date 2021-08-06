from project.player.player import Player


class BattleField:

    @staticmethod
    def is_beginner(player):
        return type(player).__name__ == "Beginner"

    @staticmethod
    def increase_health_points(player, points):
        player.health += points

    @staticmethod
    def increase_card_points(player):
        increase_card_points = 30
        for card in player.card_repository.cards:
            card.damage_points += increase_card_points

    @staticmethod
    def players_fight(attacker: Player, enemy: Player):
        for card in attacker.card_repository.cards:
            attack_points = card.damage_points
            if enemy.is_dead or attacker.is_dead:
                return
            enemy.take_damage(attack_points)

        for card in enemy.card_repository.cards:
            attack_points = card.damage_points
            if attacker.is_dead or attacker.is_dead:
                return
            enemy.take_damage(attack_points)

        # players = [attacker, enemy]
        # someone_is_dead = False
        # while not (attacker.is_dead or enemy.is_dead):
        #     first_player = players[0]
        #     second_player = players[1]
        #     if first_player.card_repository.cards:
        #         for card in first_player.card_repository.cards:
        #             attack_points = card.damage_points
        #             try:
        #                 second_player.take_damage(attack_points)
        #             except ValueError:
        #                 if second_player.is_dead:
        #                     someone_is_dead = True
        #                     break
        #     if someone_is_dead:
        #         break
            #     current_card = first_player.card_repository.cards[0]
            #     attack_points = current_card.damage_points
            #     first_player.card_repository.remove(current_card.name)
            #     second_player.take_damage(attack_points)

            # players[0], players[1] = players[1], players[0]

    def increase_player_status_if_beginner(self, player):
        increase_health_points = 40
        if not self.is_beginner(player):
            return
        self.increase_health_points(player, increase_health_points)
        self.increase_card_points(player)

    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        self.increase_player_status_if_beginner(attacker)
        self.increase_player_status_if_beginner(enemy)

        self.increase_health_points(attacker, attacker.card_repository.sum_of_cards_damage)
        self.increase_health_points(enemy, enemy.card_repository.sum_of_cards_damage)

        self.players_fight(attacker, enemy)






