import asyncio
import typer

from app.base.user.storage.base.base import UserRepository
from app.base.user.model.user_model import UserCreate, UserUpdate
from app.container import container
from app.base.user.storage.base.session_factory import SessionFactory

app = typer.Typer(help="User CLI for CRUD operations")


@app.command("create")
def create_user(full_name: str):
    """
    Create a new user with the given full_name.
    """
    asyncio.run(create_user_command(full_name))


async def create_user_command(full_name: str):
    user_repository: UserRepository = container.resolve(UserRepository)
    user = await user_repository.create_user(UserCreate(full_name=full_name))
    typer.echo(f"User created: ID={user.id}, FullName={user.full_name}")

    # Dispose the engine after operation to clean up properly
    session_factory: SessionFactory = container.resolve(SessionFactory)
    await session_factory.engine.dispose()


@app.command("get")
def get_user(user_id: int):
    """
    Get a user by ID.
    """
    asyncio.run(get_user_command(user_id))


async def get_user_command(user_id: int):
    user_repository: UserRepository = container.resolve(UserRepository)
    user = await user_repository.get_user(user_id)
    if user:
        typer.echo(f"User found: ID={user.id}, FullName={user.full_name}")
    else:
        typer.echo("User not found")

    # Clean up
    session_factory: SessionFactory = container.resolve(SessionFactory)
    await session_factory.engine.dispose()


@app.command("update")
def update_user(user_id: int, full_name: str):
    """
    Update an existing user's full_name.
    """
    asyncio.run(update_user_command(user_id, full_name))


async def update_user_command(user_id: int, full_name: str):
    user_repository: UserRepository = container.resolve(UserRepository)
    user = await user_repository.update_user(user_id, UserUpdate(full_name=full_name))
    if user:
        typer.echo(f"User updated: ID={user.id}, FullName={user.full_name}")
    else:
        typer.echo("User not found")

    # Clean up
    session_factory: SessionFactory = container.resolve(SessionFactory)
    await session_factory.engine.dispose()


@app.command("delete")
def delete_user(user_id: int):
    """
    Delete a user by ID.
    """
    asyncio.run(delete_user_command(user_id))


async def delete_user_command(user_id: int):
    user_repository: UserRepository = container.resolve(UserRepository)
    success = await user_repository.delete_user(user_id)
    if success:
        typer.echo("User deleted")
    else:
        typer.echo("User not found")

    # Clean up
    session_factory: SessionFactory = container.resolve(SessionFactory)
    await session_factory.engine.dispose()


if __name__ == "__main__":
    app()
