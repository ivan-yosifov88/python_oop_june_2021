from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    type = "Heavy"
    coefficient_changing_capacity = 2
    coefficient_changing_memory = 0.75

    def __init__(self, name, capacity, memory):
        super().__init__(name, self.type, int(capacity * self.coefficient_changing_capacity),
                         int(memory * self.coefficient_changing_memory))
