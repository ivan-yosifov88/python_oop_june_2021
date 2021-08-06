import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    def test_init_when_correct_and_courses_are_None__should_set(self):
        name = "Test"
        student = Student(name)
        self.assertEqual(name, student.name)
        self.assertEqual({}, student.courses)

    def test_init_when_correct_and_courses__should_set(self):
        name = "Test"
        courses = {"course_name": ["note"]}
        student = Student(name, courses)
        self.assertEqual(name, student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll__when_course_name_in_courses__should_return_message_and_append_note(self):
        name = "Test"
        courses = {"course_name": ["note"]}
        student = Student(name, courses)
        course_name = "course_name"
        note = ["note_one", "note_two"]
        add_course_note = "Y"
        expected_message = "Course already added. Notes have been updated."
        self.assertEqual(expected_message, student.enroll(course_name, note, add_course_note))
        courses = {"course_name": ["note", "note_one", "note_two"]}
        self.assertEqual(courses, student.courses)

    def test_enroll__when_course_name_not_in_courses_and_add_course_notes_is_Y__should_return_message_create_key_value(self):
        name = "Test"
        courses = {"course_name": ["note"]}
        student = Student(name, courses)
        course_name = "new_name"
        note = ["note_one", "note_two"]
        add_course_note = "Y"
        expected_message = "Course and course notes have been added."
        self.assertEqual(expected_message, student.enroll(course_name, note, add_course_note))
        courses = {"course_name": ["note"], "new_name": ["note_one", "note_two"]}
        self.assertEqual(courses, student.courses)

    def test_enroll__when_course_name_not_in_courses_and_add_course_notes_is_empty_string__should_return_message_create(self):
        name = "Test"
        courses = {"course_name": ["note"]}
        student = Student(name, courses)
        course_name = "new_name"
        note = ["note_one", "note_two"]
        add_course_note = ""
        expected_message = "Course and course notes have been added."
        self.assertEqual(expected_message, student.enroll(course_name, note, add_course_note))
        courses = {"course_name": ["note"], "new_name": ["note_one", "note_two"]}
        self.assertEqual(courses, student.courses)

    def test_enroll__when_course_name_not_in_courses_and_no_notes__should_return_message_create_key_with_empty_notes(self):
        name = "Test"
        courses = {"course_name": ["note"]}
        student = Student(name, courses)
        course_name = "new_name"
        note = ["note"]
        add_course_note = "N"
        expected_message = "Course has been added."
        self.assertEqual(expected_message, student.enroll(course_name, note, add_course_note))
        courses = {"course_name": ["note"], "new_name": []}
        self.assertEqual(courses, student.courses)

    def test_add_notes__when_course_name_not_in_courses__should_raise_Exception(self):
        course_name = "Not in"
        notes = ["note_one", "note_two"]
        expected_message = "Cannot add notes. Course not found."
        name = "Test"
        courses = {"course_name": ["note"]}
        student = Student(name, courses)
        with self.assertRaises(Exception) as message:
            student.add_notes(course_name, notes)
        self.assertEqual(expected_message, str(message.exception))

    def test_add_notes__when_course_name_in_courses__should_append_notes(self):
        course_name = "course_name"
        notes = ["note_one", "note_two"]
        expected_message = "Notes have been updated"
        name = "Test"
        courses = {"course_name": ["note"]}
        student = Student(name, courses)
        assert_message = student.add_notes(course_name, notes)
        self.assertEqual(expected_message, assert_message)
        expected_course = {"course_name": ["note", ["note_one", "note_two"]]}
        self.assertEqual(expected_course, student.courses)

    def test_leave_course__when__course_name_not_in_courses__should_raise_Exception(self):
        course_name = "Not in"
        expected_message = "Cannot remove course. Course not found."
        name = "Test"
        courses = {"course_name": ["note"]}
        student = Student(name, courses)
        with self.assertRaises(Exception) as message:
            student.leave_course(course_name)
        self.assertEqual(expected_message, str(message.exception))

    def test_leave_course__when__course_name_in_courses__should_pop_and_return_message(self):
        course_name = "course_name"
        expected_message = "Course has been removed"
        name = "Test"
        courses = {"course_name": ["note"]}
        student = Student(name, courses)
        assert_message = student.leave_course(course_name)
        self.assertEqual(expected_message, assert_message)
        self.assertEqual({}, student.courses)


if __name__ == "__main__":
    unittest.main()