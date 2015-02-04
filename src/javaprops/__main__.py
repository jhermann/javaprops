# -*- coding: utf-8 -*-
""" Command line interface.
"""
import click


@click.command()
def run():
    """Parse and work with Java property files."""
    click.echo('not implemented!')


if __name__ == "__main__": # imported via "python -m"?
    run()

