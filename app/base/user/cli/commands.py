import asyncio
import typer
from app.base.user.services import UserService


def create_user_command(user_service: UserService):
    def _create_user(full_name: str):
        """Create a new user with the given full_name."""
        asyncio.run(_create_user_cmd(full_name))

    async def _create_user_cmd(full_name: str):
        result = await user_service.create_user(full_name)
        typer.echo(result)

    return _create_user


def get_user_command(user_service: UserService):
    def _get_user(user_id: int):
        """Get a user by ID."""
        asyncio.run(_get_user_cmd(user_id))

    async def _get_user_cmd(user_id: int):
        result = await user_service.get_user(user_id)
        typer.echo(result)

    return _get_user


def update_user_command(user_service: UserService):
    def _update_user(user_id: int, full_name: str):
        """Update an existing user's full_name."""
        asyncio.run(_update_user_cmd(user_id, full_name))

    async def _update_user_cmd(user_id: int, full_name: str):
        result = await user_service.update_user(user_id, full_name)
        typer.echo(result)

    return _update_user


def delete_user_command(user_service: UserService):
    def _delete_user(user_id: int):
        """Delete a user by ID."""
        asyncio.run(_delete_user_cmd(user_id))

    async def _delete_user_cmd(user_id: int):
        result = await user_service.delete_user(user_id)
        typer.echo(result)

    return _delete_user
