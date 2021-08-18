class Suitcase:
    _valid_figure_types = {"Circle", "Rectangle", "Triangle", "Square"}

    def __init__(self):
        self.repository = []

    def __repr__(self):
        return [{', '.join(str(figure))}for figure in self.repository]

    @staticmethod
    def _get_figure_name(name, list_of_obj):
        return [obj for obj in list_of_obj if obj.__class__.__name__ == name]

    def add(self, figure):
        name = figure.__class__.__name__
        if name not in self._valid_figure_types:
            raise TypeError("The type of Figure is incorrect!")
        current_figure = self._get_figure_name(figure.name, self.repository)
        if current_figure:
            raise KeyError("Figure name already exist!")

        self.repository.append(figure)
        return f"Figure: {name} added."

    def remove(self, figure_name):
        current_figure = self._get_figure_name(figure_name, self.repository)
        if not current_figure:
            raise KeyError(f"Figure: {figure_name} not exist!")

        figure_to_remove = current_figure[0]
        self.repository.remove(figure_to_remove)
        return f"Figure: {figure_name} removed"

    def get_figure(self, figure_name):
        current_figure = self._get_figure_name(figure_name, self.repository)
        if current_figure:
            return current_figure[0]

