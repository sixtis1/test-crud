from typer import Typer
from app.base.user.cli.commands import (
    create_user_command,
    get_user_command,
    update_user_command,
    delete_user_command,
)
from app.base.user.services import UserService
from app.container import container


class UserCLIInitializer:
    def __init__(self):
        self.name = "user"
        self.user_service: UserService = container.resolve(UserService)
        self.app = Typer(help="User CLI for CRUD operations")

    def register_commands(self):
        self.app.command("create")(create_user_command(self.user_service))
        self.app.command("get")(get_user_command(self.user_service))
        self.app.command("update")(update_user_command(self.user_service))
        self.app.command("delete")(delete_user_command(self.user_service))
