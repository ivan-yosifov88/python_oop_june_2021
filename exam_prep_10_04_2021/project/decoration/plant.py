from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    _default_comfort = 5
    _default_price = 10

    def __init__(self):
        super().__init__(self._default_comfort, self._default_price)