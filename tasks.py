# -*- coding: utf-8 -*-
import os
import glob
import shlex

from invoke import run, task
from setup import *

@task(default=True)
def help():
    """Invoked with no arguments."""
    run("invoke --help")
    run("invoke --list")
    print("Use 'invoke -h ‹taskname›' to get detailed help.")


@task
def clean(docs=False, backups=False, bytecode=False, dist=False, all=False, venv=False, extra=''):
    """Perform house-cleaning."""
    patterns = ['build']
    if docs or all:
        patterns.append('docs/_build')
    if dist or all:
        patterns.append('dist')
    if backups or all:
        patterns.extend(['*~', '**/*~'])
    if bytecode or all:
        patterns.extend(['*.py[co]', '**/*.py[co]'])

    if venv:
        patterns.extend(['bin', 'include', 'lib', 'share', 'local'])
    if extra:
        patterns.extend(shlex.split(extra))

    for pattern in patterns:
        for name in glob.iglob(pattern):
            run('rm -rf "{0}"'.format(name))


@task
def build(docs=False):
    """Build the project."""
    run("python setup.py build")
    if docs and os.path.exists(srcfile("docs", "conf.py")):
        run("sphinx-build docs docs/_build")


@task
def test():
    """Perform standard unittests."""
    run('python setup.py test')


@task
def check():
    """Perform source code checks."""
    run('pylint "{0}"'.format(srcfile('src', project['name'])))


@task
def ci():
    """Perform continuous integration tasks."""
    run("invoke clean --all build --docs check")

