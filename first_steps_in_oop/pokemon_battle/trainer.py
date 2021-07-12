from pokemon_battle.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return "Caught " + pokemon.pokemon_details()

    def release_pokemon(self, pokemon_name):
        pokemon_available = [pokemon for pokemon in self.pokemons if pokemon.name == pokemon_name]
        if not pokemon_available:
            return "Pokemon is not caught"

        current_pokemon = pokemon_available[0]
        self.pokemons.remove(current_pokemon)
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        pokemon_caught = len(self.pokemons)
        result = ""
        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {pokemon_caught}\n"
        for pokemon in self.pokemons:
            result += f"- {pokemon.pokemon_details()}\n"

        return result


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())

