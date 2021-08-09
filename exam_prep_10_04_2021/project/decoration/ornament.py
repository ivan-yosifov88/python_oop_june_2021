from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    _default_comfort = 1
    _default_price = 5

    def __init__(self):
        super().__init__(self._default_comfort, self._default_price)
