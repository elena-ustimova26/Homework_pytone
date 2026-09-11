import uuid
import pytest

from YougileApi import YougileApi


@pytest.fixture
def api():
    return YougileApi()


def unique_title(prefix: str = "project") -> str:
    #Уникальное название проекта, чтобы не пересекаться с уже существующими
    return f"{prefix}-{uuid.uuid4().hex}"


#POST /api-v2/projects

def test_create_project_positive(api):
    #Позитив: создаём проект и проверяем его через GET
    title = unique_title("create")

    # Создаём проект
    resp = api.create_project(title)
    assert resp.status_code in (200, 201), resp.text

    body = resp.json()
    assert "id" in body, "В ответе на POST нет id созданного проекта"
    project_id = body["id"]

    #POST возвращает только id — проверяем данные через GET
    check = api.get_project(project_id)
    assert check.status_code == 200, check.text

    project = check.json()
    assert project["id"] == project_id
    assert project["title"] == title


def test_create_project_negative_without_title(api):
    """Негатив: POST без обязательного поля title."""
    resp = api.create_project_raw({})

    # Ошибка валидации: 400 или 422
    assert resp.status_code in (400, 422), resp.text


#PUT /api-v2/projects/{id}

def test_update_project_positive(api):
    #Позитив: создаём проект, меняем название, проверяем через GET
    title = unique_title("before-update")
    created = api.create_project(title)
    assert created.status_code in (200, 201), created.text

    project_id = created.json()["id"]
    new_title = unique_title("after-update")

    # Обновляем
    updated = api.update_project(project_id, title=new_title)
    assert updated.status_code == 200, updated.text

    # PUT может вернуть только id — проверяем через GET
    got = api.get_project(project_id)
    assert got.status_code == 200, got.text
    assert got.json()["title"] == new_title


def test_update_project_negative_invalid_id(api):
    #Негатив: PUT с несуществующим id
    resp = api.update_project("invalid-id-123", title="new title")

    assert resp.status_code in (400, 404), resp.text


#GET /api-v2/projects/{id}

def test_get_project_positive(api):
    """Позитив: создаём проект и получаем его по id."""
    title = unique_title("get")
    created = api.create_project(title)
    assert created.status_code in (200, 201), created.text

    project_id = created.json()["id"]

    resp = api.get_project(project_id)
    assert resp.status_code == 200, resp.text

    body = resp.json()
    assert body["id"] == project_id
    assert body["title"] == title


def test_get_project_negative_invalid_id(api):
    #Негатив: GET с несуществующим id.
    resp = api.get_project("invalid-id-123")

    assert resp.status_code in (400, 404), resp.text
    