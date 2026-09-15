from uuid import uuid4

from db_utils import get_student


def test_add_student(student_factory):
    """Тест добавления студента."""
    name = f"Student_{uuid4().hex}"
    student_id = student_factory(name)

    student = get_student(student_id)

    assert student is not None
    assert student["user_id"] == student_id
    assert student["name"] == name
    