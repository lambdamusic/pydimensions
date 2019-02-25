#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import click
from pprint import pprint
# from .console.lib import *
from .console import repl
from .console.utils import open_multi_platform
# from .console import credentials

from .VERSION import *
from .dimensions import *

# HOW TO SET UP A CONFIGURATION FILE:

# Add a '.dimcli.config.json' file to your home folder ('~').
# The file should have the following structure:

#     {
#         "usr": "your-username",
#         "psw" : "your-password",
#         "service" : "https://app.dimensions.ai/api/"   # default
#     }


@click.command()
@click.argument("instance_name", nargs=1, default="live")
@click.option(
    "--config",
    is_flag=True,
    help="Open config init file with default editor.")
@click.option(
    "--history", is_flag=True, help="Open history file with default editor.")
@click.pass_context
def main_cli(ctx, instance_name=None, config=False, history=False):
    """
    Python client for the Dimensions DSL.
    More info: https://github.com/lambdamusic/dimcli
    """

    click.secho("Dimcli - dimensions console (" + VERSION + ")", dim=True)
    # click.secho("------------", fg="white")

    if not os.path.exists(USER_CONFIG_FILE):
        click.secho(
            "Credentials file not found - please set one up first: %s" %
            USER_CONFIG_FILE,
            fg="red",
        )
        click.secho(
            "HowTo: https://github.com/lambdamusic/dimcli#credentials-file",
            fg="blue",
        )
        return

    if config:
        open_multi_platform(USER_CONFIG_FILE)
        return

    if history:
        if os.path.exists(USER_HISTORY_FILE):
            open_multi_platform(USER_HISTORY_FILE)
        return

    # launch REPL
    repl.run(instance_name)

    # dsl = Dsl(instance)
    # dsl.query("search grants return grants", True)
    # print(res)


if __name__ == "__main__":
    main_cli()
