import pytest
import script

def test_valid_person():
    person = script.Person(name="John", age=20)
    assert person.get_name() == "John"
    assert person.get_age() == 20

def test_valid_student():
    student = script.Student(name="John", age=20, grade=10)
    assert student.get_name() == "John"
    assert student.get_age() == 20
    assert student.get_grade() == 10

def test_valid_classroom():
    classroom = script.Classroom(name="John", age=20, grade=10, class_name="classroom")
    assert classroom.get_name() == "John"
    assert classroom.get_age() == 20
    assert classroom.get_grade() == 10
    assert classroom.get_class_name() == "classroom"
    # add student
    classroom.add_student(name="Bob", age=30, grade=20, class_name="classroom")
    student1 = script.Student(name="Bob", age=30, grade=20)
    student2 = script.Student(name="John", age=20, grade=10)
    assert classroom.get_number_students() == 3
    # remove student
    classroom.remove_student(name="Bob", age=30, grade=20, class_name="classroom")
    assert classroom.get_number_students() == 3

def test_invalid():
    with pytest.raises(TypeError):
        script.Person(name="John", age="age")
    with pytest.raises(TypeError):
        script.Student(name="John", age=20, grade="age")
