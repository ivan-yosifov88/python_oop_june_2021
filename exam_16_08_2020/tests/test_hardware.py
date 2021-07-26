import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):

    def test_hardware_init(self):
        test_hardware = Hardware("Test Hardware", "Test", 100, 100)
        self.assertEqual(test_hardware.name, "Test Hardware")
        self.assertEqual(test_hardware.type, "Test")
        self.assertEqual(test_hardware.capacity, 100)
        self.assertEqual(test_hardware.memory, 100)
        self.assertEqual(test_hardware.software_components, [])

    def test_install__when_there_is_not_enough_space__expect_raise_Exception(self):
        test_hardware = Hardware("Test Hardware", "Test", 100, 100)
        software = Software("Test Software", "Software", 200, 200)
        with self.assertRaises(Exception) as message:
            test_hardware.install(software)
        self.assertEqual("Software cannot be installed", str(message.exception))

    def test_install__when_input_is_valid__expect_append_in_software_components_list(self):
        test_hardware = Hardware("Test Hardware", "Test", 100, 100)
        software = Software("Test Software", "Software", 5, 5)
        test_hardware.install(software)
        self.assertEqual(test_hardware.software_components, [software])

    def test_uninstall__when_input_is_valid__expect_remove_element_from_software_components_list(self):
        test_hardware = Hardware("Test Hardware", "Test", 100, 100)
        software = Software("Test Software", "Software", 5, 5)
        test_hardware.install(software)
        test_hardware.uninstall(software)
        self.assertEqual(test_hardware.software_components, [])



if __name__ == '__main__':
    unittest.main()
