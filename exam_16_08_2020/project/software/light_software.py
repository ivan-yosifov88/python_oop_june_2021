from project.software.software import Software


class LightSoftware(Software):
    type = "Light"
    coefficient_changing_capacity = 1.5
    coefficient_changing_memory = 0.5

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, self.type, int(capacity_consumption * self.coefficient_changing_capacity),
                         int(memory_consumption * self.coefficient_changing_memory))

