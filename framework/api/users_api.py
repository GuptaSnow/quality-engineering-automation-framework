from framework.api.client import APIClient


class UsersAPI:

    def __init__(self, client: APIClient):
        self.client = client

    def get_user(self, user_id: int):
        return self.client.get(
            f"/users/{user_id}"
        )

    def create_user(self, payload: dict):
        return self.client.post(
            "/users",
            json=payload
        )

    def update_user(
        self,
        user_id: int,
        payload: dict
    ):
        return self.client.put(
            f"/users/{user_id}",
            json=payload
        )

    def delete_user(self, user_id: int):
        return self.client.delete(
            f"/users/{user_id}"
        )