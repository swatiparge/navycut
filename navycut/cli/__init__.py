import click as c
from ._exec_cli import _create_boiler_project
from navycut import get_version

@c.group()
def _execute_from_command_line():
    """execute navycut commands from command line."""
    pass

@c.command()
@c.argument('name')
def createproject(name):
    """Create the navycut project at the specified directory."""
    _create_boiler_project(name)

@c.command()
def version():
    c.echo(get_version())




_execute_from_command_line.add_command(createproject)
_execute_from_command_line.add_command(version)