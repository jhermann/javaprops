# -*- coding: utf-8 -*-
""" Command line interface.
"""
import sys

import click


@click.group()
@click.option('-q', '--quiet', is_flag=True, default=False, help='Be quiet (show only errors).')
@click.option('-v', '--verbose', is_flag=True, default=False, help='Create extra verbose output.')
def cli(quiet=False, verbose=False):
    """Parse and work with Java property files."""


@cli.command()
@click.option('-o', '--output', metavar='FILE', nargs=1, type=click.File(mode='w', lazy=True),
    help='Write output to <file> instead of stdout.')
@click.argument('file-or-url')
def normalize(file_or_url, output=None):
    """Load properties and write a normalized, deduplicated, include-free copy."""
    click.echo('normalize - not implemented! args={0}'.format((output, file_or_url)))
    output = output or sys.stdout


if __name__ == "__main__": # imported via "python -m"?
    cli()

