from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    _default_capacity = 50

    def __init__(self, name):
        super().__init__(name, self._default_capacity)