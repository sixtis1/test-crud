from typer import Typer
from app.base.user.cli.commands import user_app


class UserCLIInitializer:
    @staticmethod
    def register_commands(main_app: Typer):
        main_app.add_typer(user_app, name="user")