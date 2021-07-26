import unittest

from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def test_room_init(self):
        room = Room("Family name", 100, 1)
        self.assertEqual(room.family_name, "Family name")
        self.assertEqual(room.budget, 100)
        self.assertEqual(room.members_count, 1)
        self.assertEqual(room.children, [])
        self.assertEqual(room.expenses, 0)

    def test_calculate_expenses__when_no_args__expect__expenses_property_to_be_zero(self):
        room = Room("Family name", 100, 1)
        room.calculate_expenses()
        self.assertEqual(room.expenses, 0)

    def test_expenses__when_value_is_less_then_zero__expect_raise_Value_Error(self):
        room = Room("Family name", 100, 1)
        with self.assertRaises(ValueError) as message:
            room.expenses = -1
        self.assertEqual("Expenses cannot be negative", str(message.exception))

    if __name__ == "__main__":
        unittest.main()
