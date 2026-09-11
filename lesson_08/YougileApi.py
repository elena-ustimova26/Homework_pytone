import os
import requests


class YougileApi:
    def __init__(
            self, base_url: str = "https://ru.yougile.com/api-v2"):
        self.base_url = base_url.rstrip("/")
        self.token = "TOKEN"  # УКАЗАТЬ ТОКЕН

        if not self.token:
            raise RuntimeError(
                "Не задан токен Yougile. "
                "Установите переменную окружения YOUGILE_TOKEN."
            )

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def create_project(self, title: str, **extra):
        #POST /api-v2/projects
        payload = {"title": title}
        payload.update(extra)
        return requests.post(
            f"{self.base_url}/projects",
            headers=self.headers,
            json=payload,
        )

    def create_project_raw(self, payload: dict):
        #POST /api-v2/projects с произвольным телом — негативный тест
        return requests.post(
            f"{self.base_url}/projects",
            headers=self.headers,
            json=payload,
        )

    def update_project(self, project_id: str, **fields):
        #PUT /api-v2/projects/{id}
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
            json=fields,
        )

    def get_project(self, project_id: str):
        #GET /api-v2/projects/{id}
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
        )
