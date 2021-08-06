from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    type = "Power"
    coefficient_changing_capacity = 0.25
    coefficient_changing_memory = 1.75

    def __init__(self, name, capacity, memory):
        super().__init__(name, self.type, int(capacity * self.coefficient_changing_capacity),
                         int(memory * self.coefficient_changing_memory))
