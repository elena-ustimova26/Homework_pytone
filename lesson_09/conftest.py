import pytest

from db_utils import create_student, delete_student


@pytest.fixture
def student_factory():
    """Создаёт студентов и удаляет их после теста."""
    created_ids = []

    def create(name: str) -> int:
        student_id = create_student(name)
        created_ids.append(student_id)
        return student_id

    yield create

    for student_id in created_ids:
        delete_student(student_id)
        