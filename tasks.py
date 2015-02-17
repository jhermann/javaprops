# -*- coding: utf-8 -*-
import os
import re
import sys
import glob
import shlex
import itertools

from invoke import run, task
from setup import *

# https://raw.githubusercontent.com/zacherates/fileset.py/e3a512f457c9b52953bed1932448762a7e0c9c71/fileset.py
# MIT licensed, has no PyPI release :(
# modified to allow [charset]s
# TODO: allow '?'
# TODO: prune excluded directories during walk()
class Pattern(object):
    def __init__(self, spec, inclusive):
        self.compiled = self.compile(spec)
        self.inclusive = inclusive

    def __str__(self):
        return self.compiled.pattern

    def compile(self, spec):
        parse = "".join(self.parse(spec))
        regex = "^{0}$".format(parse)
        return re.compile(regex)

    def parse(self, pattern):
        def globify(part):
            return "[^/]*".join(re.escape(bit).replace(r'\[', '[').replace(r'\]', ']') for bit in part.split("*"))

        if not pattern:
            raise StopIteration

        bits = pattern.split("/")
        dirs, file = bits[:-1], bits[-1]

        for dir in dirs:
            if dir == "**":
                yield  "(|.+/)"

            else:
                yield globify(dir) + "/"

        yield globify(file)

    def matches(self, path):
        return self.compiled.match(path) is not None


class FileSet(object):
    """ Ant style file matching.

        Produces an iterator of all of the files that match the provided pattern.

        Directory specifiers:
            **          matches zero or more directories.
            *           matches any directory name.
            /           path separator.

        File specifiers:
            *           glob style wildcard.
            [chars]     character sets.

        Examples:
            **/*.py         recursively match all python files.
            foo/**/*.py     recursively match all python files in the foo/ directory.
            *.py            match all the python files in the current diretory.
            */*.txt         match all the text files in child directories.
    """

    def __init__(self, root, patterns):
        self.root = root
        self.patterns = patterns

    def included(self, path):
        """Check patterns in order, last match that includes or excludes `path` wins."""
        inclusive = False
        for pattern in self.patterns:
            if pattern.matches(path):
                inclusive = pattern.inclusive

        #print '+++' if inclusive else '---', path, pattern
        return inclusive

    def __iter__(self):
        for path in self.walk():
            yield path

    def __or__(self, other):
        return set(self) | set(other)

    def __ror__(self, other):
        return self | other

    def __and__(self, other):
        return set(self) & set(other)

    def __rand__(self, other):
        return self & other

    def walk(self, **kwargs):
        for base, dirs, files in os.walk(self.root, **kwargs):
            prefix = base[len(self.root):].lstrip(os.sep)
            bits = prefix.split(os.sep) if prefix else []

            for filename in files:
                path = '/'.join(bits + [filename])
                if self.included(path):
                    yield path

def includes(pattern):
    return Pattern(pattern, inclusive=True)

def excludes(pattern):
    return Pattern(pattern, inclusive=False)

# end of zacherates/fileset.py


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
        patterns.extend(['*.py[co]', '**/*.py[co]', '**/__pycache__'])

    venv_dirs = ['bin', 'include', 'lib', 'share', 'local']
    if venv:
        patterns.extend(venv_dirs)
    if extra:
        patterns.extend(shlex.split(extra))

    patterns = [includes(i) for i in patterns]
    if not venv:
        patterns.extend([excludes(i + '/**/*') for i in venv_dirs])
    fileset = FileSet(project_root, patterns)
    for name in fileset:
        print('rm {0}'.format(name))
        os.unlink(os.path.join(project_root, name))


@task
def build(docs=False):
    """Build the project."""
    os.chdir(project_root)
    run("python setup.py build")
    if docs and os.path.exists(srcfile("docs", "conf.py")):
        run("sphinx-build docs docs/_build")


@task
def test():
    """Perform standard unittests."""
    os.chdir(project_root)
    run('python setup.py test')


@task
def check():
    """Perform source code checks."""
    os.chdir(project_root)
    run('pylint "{0}"'.format(srcfile('src', project['name'])))


@task
def ci():
    """Perform continuous integration tasks."""
    run("invoke clean --all build --docs test check")

