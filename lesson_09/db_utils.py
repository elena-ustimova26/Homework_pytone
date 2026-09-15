from sqlalchemy import create_engine, text

DB_CONNECTION_STRING = (
    "postgresql://postgres:postgres@localhost:5432/DZ"
)

engine = create_engine(DB_CONNECTION_STRING)


def create_student(name: str) -> int:
    """Создаёт студента и возвращает его user_id."""
    with engine.begin() as conn:
        result = conn.execute(
            text(
                "INSERT INTO student (user_id, name) "
                "VALUES ("
                "  (SELECT COALESCE(MAX(user_id), 0) + 1 FROM student), "
                "  :name"
                ") "
                "RETURNING user_id"
            ),
            {"name": name},
        )
        return result.scalar_one()


def get_student(student_id: int):
    """Возвращает студента по user_id или None."""
    with engine.connect() as conn:
        result = conn.execute(
            text(
                "SELECT user_id, name FROM student "
                "WHERE user_id = :id"
            ),
            {"id": student_id},
        )
        return result.mappings().first()


def update_student_name(student_id: int, new_name: str) -> None:
    """Обновляет имя студента по user_id."""
    with engine.begin() as conn:
        conn.execute(
            text(
                "UPDATE student SET name = :name "
                "WHERE user_id = :id"
            ),
            {"name": new_name, "id": student_id},
        )


def delete_student(student_id: int) -> None:
    """Удаляет студента по user_id."""
    with engine.begin() as conn:
        conn.execute(
            text("DELETE FROM student WHERE user_id = :id"),
            {"id": student_id},
        )
        