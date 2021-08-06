from project.software.software import Software


class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @property
    def count_of_light_software(self):
        return len([component for component in self.software_components
                   if component.type == "Light"])

    @property
    def count_of_express_software(self):
        return len([component for component in self.software_components
                    if component.type == "Express"])

    @property
    def total_memory_of_components(self):
        return sum([component.memory_consumption for component in self.software_components])

    @property
    def total_capacity_of_components(self):
        return sum([component.capacity_consumption for component in self.software_components])

    def is_enough_space_to_install(self, memory, capacity):
        return self.total_memory_of_components + memory <= self.memory and\
               self.total_capacity_of_components + capacity <= self.capacity

    def install(self, software: Software):
        if not self.is_enough_space_to_install(software.memory_consumption, software.capacity_consumption):
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)



