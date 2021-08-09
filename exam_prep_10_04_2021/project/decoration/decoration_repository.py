from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration not in self.decorations:
            return False

        self.decorations.remove(decoration)
        return True

    @staticmethod
    def _get_decoration(obj_type, list_of_obj):
        return [obj for obj in list_of_obj if obj.__class__.__name__ == obj_type]

    def find_by_type(self, decoration_type):
        filtered_decoration = self._get_decoration(decoration_type, self.decorations)
        if not filtered_decoration:
            return "None"

        return filtered_decoration[0]


# plant = Plant()
# ornament = Ornament()
# test_ornament = Ornament()
# repo = DecorationRepository()
# repo.add(plant)
# repo.add(ornament)
# repo.remove(ornament)
# repo.add(ornament)
# print(repo.remove(test_ornament))
# print(repo.find_by_type("Ornament"))
# print(repo.find_by_type("Bads"))


