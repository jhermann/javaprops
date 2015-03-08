# -*- coding: utf-8 -*-
# pylint: disable=bad-continuation
""" Command line interface.
"""
# Copyright ⓒ  2015 1&1 Group
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import click

__app_name__ = 'javaprops'
CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help'],
)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('-q', '--quiet', is_flag=True, default=False, help='Be quiet (show only errors).')
@click.option('-v', '--verbose', is_flag=True, default=False, help='Create extra verbose output.')
def cli(quiet=False, verbose=False): # pylint: disable=unused-argument
    """Parse and work with Java property files."""
    appdir = click.get_app_dir(__app_name__)
    #click.secho('appdir = {0}'.format(appdir), fg='yellow')


@cli.command()
@click.option('-o', '--output', metavar='FILE', nargs=1, type=click.File(mode='w', lazy=True),
    help='Write output to <file> instead of stdout.')
@click.argument('file-or-url')
def normalize(file_or_url, output=None):
    """Load properties and write a normalized, deduplicated, include-free copy."""
    click.echo('normalize - not implemented! args={0}'.format((output, file_or_url)))
    output = output or click.get_text_stream('stdout')


if __name__ == "__main__": # imported via "python -m"?
    cli()
