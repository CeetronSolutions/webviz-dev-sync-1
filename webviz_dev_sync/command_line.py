import argparse

from webviz_dev_sync._editor import open_editor

from .webviz_dev_sync import start_webviz_dev_sync
from .webviz_dev_sync import open_config
from .webviz_dev_sync import print_config


def main() -> None:

    parser = argparse.ArgumentParser(prog=("Start the Webviz development syncer tool"))

    subparsers = parser.add_subparsers(
        metavar="SUBCOMMAND",
        help="Below are the available subcommands listed. "
        "Type e.g. 'webviz-dev-sync start --help' "
        "to get help on one particular "
        "subcommand.",
    )

    parser_start = subparsers.add_parser(
        "start", help="Start the Webviz development syncer tool"
    )

    parser_start.set_defaults(func=start_webviz_dev_sync)

    parser_config = subparsers.add_parser("config", help="Opens the config file")

    parser_config.set_defaults(func=open_config)

    args = parser.parse_args()

    args.func(args)
