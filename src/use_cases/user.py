from src.interfaces import user
from src.entities import users

class UserUseCases:
    def __init__(self, repo: user.UserRepository) -> None:
        self.repo = repo

    async def create_user(self, name: str, email: str, password: str) -> None:
        pass

    async def get_user_by_id(self, id: int) -> users.User:
        return await self.repo.get_user_by_id(id=id)

    async def get_all_users(self) -> typing.List[users.User]:
        return await self.repo.get_all_users()
    async def delete_user(self, id: int) -> None: ...
