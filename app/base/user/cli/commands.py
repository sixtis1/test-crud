import asyncio
import typer
from app.container import container
from app.base.user.services import UserService

app = typer.Typer(help="User CLI for CRUD operations")


class UserCommands:
    def __init__(self):
        self.service: UserService = container.resolve(UserService)

    @app.command("create")
    def create_user(self, full_name: str):
        """Create a new user with the given full_name."""
        asyncio.run(self._create_user_cmd(full_name))

    async def _create_user_cmd(self, full_name: str):
        result = await self.service.create_user(full_name)
        typer.echo(result)

    @app.command("get")
    def get_user(self, user_id: int):
        """Get a user by ID."""
        asyncio.run(self._get_user_cmd(user_id))

    async def _get_user_cmd(self, user_id: int):
        result = await self.service.get_user(user_id)
        typer.echo(result)

    @app.command("update")
    def update_user(self, user_id: int, full_name: str):
        """Update an existing user's full_name."""
        asyncio.run(self._update_user_cmd(user_id, full_name))

    async def _update_user_cmd(self, user_id: int, full_name: str):
        result = await self.service.update_user(user_id, full_name)
        typer.echo(result)

    @app.command("delete")
    def delete_user(self, user_id: int):
        """Delete a user by ID."""
        asyncio.run(self._delete_user_cmd(user_id))

    async def _delete_user_cmd(self, user_id: int):
        result = await self.service.delete_user(user_id)
        typer.echo(result)


UserCommands()
