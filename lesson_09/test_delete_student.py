from uuid import uuid4

from db_utils import get_student, delete_student


def test_delete_student(student_factory):
    """Тест удаления студента."""
    name = f"Student_{uuid4().hex}"
    student_id = student_factory(name)

    delete_student(student_id)

    student = get_student(student_id)

    assert student is None