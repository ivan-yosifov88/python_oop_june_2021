from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def get_name(ll_of_obj, obj_name):
        return [obj for obj in ll_of_obj if obj.name == obj_name]

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        filtered_hardware_name = System.get_name(System._hardware, hardware_name)
        if not filtered_hardware_name:
            return "Hardware does not exist"

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            filtered_hardware_name[0].install(express_software)
        except Exception as message:
            return str(message)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        filtered_hardware_name = System.get_name(System._hardware, hardware_name)
        if not filtered_hardware_name:
            return "Hardware does not exist"

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            filtered_hardware_name[0].install(light_software)
        except Exception as message:
            return str(message)

        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        filtered_hardware = System.get_name(System._hardware, hardware_name)
        filtered_software = System.get_name(System._software, software_name)
        if not (filtered_hardware and filtered_software):
            return "Some of the components do not exist"

        filtered_hardware[0].uninstall(filtered_software[0])
        System._software.remove(filtered_software[0])

    @staticmethod
    def analyze():
        count_of_hardware_components = len(System._hardware)
        count_of_software_components = len(System._software)
        total_used_memory = sum([c.total_memory_of_components for c in System._hardware])
        total_memory = sum([c.memory for c in System._hardware])
        total_used_space = sum([c.total_capacity_of_components for c in System._hardware])
        total_capacity = sum([c.capacity for c in System._hardware])

        result = [
            "System Analysis",
            f"Hardware Components: {count_of_hardware_components}",
            f"Software Components: {count_of_software_components}",
            f"Total Operational Memory: {total_used_memory} / {total_memory}",
            f"Total Capacity Taken: {total_used_space} / {total_capacity}"
        ]

        return '\n'.join(result)

    @staticmethod
    def system_split():
        final_result = ''

        for hardware in System._hardware:
            total_memory_of_the_hardware = hardware.memory
            total_capacity_of_the_hardware = hardware.capacity
            names_of_all_software_components = ', '.join(component.name for component in hardware.software_components)\
                if hardware.software_components else "None"
            component_name = hardware.name
            number_of_the_installed_express_software_components = hardware.count_of_express_software
            number_of_the_installed_light_software_components = hardware.count_of_light_software
            total_memory_used_of_all_installed_software_components = hardware.total_memory_of_components
            total_capacity_used_of_all_installed_software_components = hardware.total_capacity_of_components

            result = [
                f"Hardware Component - {component_name}",
                f"Express Software Components: {number_of_the_installed_express_software_components}",
                f"Light Software Components: {number_of_the_installed_light_software_components}",
                f"Memory Usage: {total_memory_used_of_all_installed_software_components} / "
                f"{total_memory_of_the_hardware}",
                f"Capacity Usage: {total_capacity_used_of_all_installed_software_components} / "
                f"{total_capacity_of_the_hardware}",
                f"Type: {hardware.type}",
                f"Software Components: {names_of_all_software_components}"
            ]
            final_result += '\n'.join(result)
        return final_result


System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
print(System.register_express_software("HDD", "Test2", 100, 100))
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
print(System.analyze())
System.release_software_component("SSD", "Linux")
print(System.system_split())

