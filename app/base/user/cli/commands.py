# app/base/user/cli/commands.py

import asyncio
import typer
from app.base.user.cli.services import (
    create_user_service,
    get_user_service,
    update_user_service,
    delete_user_service,
)

app = typer.Typer(help="User CLI for CRUD operations")

@app.command("create")
def create_user(full_name: str):
    """Create a new user with the given full_name."""
    asyncio.run(_create_user_cmd(full_name))

async def _create_user_cmd(full_name: str):
    result = await create_user_service(full_name)
    typer.echo(result)

@app.command("get")
def get_user(user_id: int):
    """Get a user by ID."""
    asyncio.run(_get_user_cmd(user_id))

async def _get_user_cmd(user_id: int):
    result = await get_user_service(user_id)
    typer.echo(result)

@app.command("update")
def update_user(user_id: int, full_name: str):
    """Update an existing user's full_name."""
    asyncio.run(_update_user_cmd(user_id, full_name))

async def _update_user_cmd(user_id: int, full_name: str):
    result = await update_user_service(user_id, full_name)
    typer.echo(result)

@app.command("delete")
def delete_user(user_id: int):
    """Delete a user by ID."""
    asyncio.run(_delete_user_cmd(user_id))

async def _delete_user_cmd(user_id: int):
    result = await delete_user_service(user_id)
    typer.echo(result)
