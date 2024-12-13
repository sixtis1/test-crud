import typer
from app.base.user.cli.user_initializer import UserCLIInitializer


app = typer.Typer()

initializers = [UserCLIInitializer()]

for initializer in initializers:
    initializer.register_commands(app)

if __name__ == "__main__":
    app()
