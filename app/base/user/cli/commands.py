import asyncio
import typer
from app.container import container
from app.base.user.services import UserService

user_app = typer.Typer(help="User CLI for CRUD operations")

user_service: UserService = container.resolve(UserService)


@user_app.command("create")
def create_user(full_name: str):
    """Create a new user with the given full_name."""
    asyncio.run(_create_user_cmd(full_name))


async def _create_user_cmd(full_name: str):
    result = await user_service.create_user(full_name)
    typer.echo(result)


@user_app.command("get")
def get_user(user_id: int):
    """Get a user by ID."""
    asyncio.run(_get_user_cmd(user_id))


async def _get_user_cmd(user_id: int):
    result = await user_service.get_user(user_id)
    typer.echo(result)


@user_app.command("update")
def update_user(user_id: int, full_name: str):
    """Update an existing user's full_name."""
    asyncio.run(_update_user_cmd(user_id, full_name))


async def _update_user_cmd(user_id: int, full_name: str):
    result = await user_service.update_user(user_id, full_name)
    typer.echo(result)


@user_app.command("delete")
def delete_user(user_id: int):
    """Delete a user by ID."""
    asyncio.run(_delete_user_cmd(user_id))


async def _delete_user_cmd(user_id: int):
    result = await user_service.delete_user(user_id)
    typer.echo(result)
