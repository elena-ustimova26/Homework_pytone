from uuid import uuid4

from db_utils import get_student, update_student_name


def test_update_student(student_factory):
    """Тест изменения студента."""
    old_name = f"Student_{uuid4().hex}"
    new_name = f"Student_{uuid4().hex}"

    student_id = student_factory(old_name)
    update_student_name(student_id, new_name)

    student = get_student(student_id)

    assert student is not None
    assert student["name"] == new_name
    