# -*- coding: utf-8 -*-
# pylint: disable=bad-continuation
""" Miscellaneous helpers.
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

import os
import sys
from collections import namedtuple

termsize = namedtuple("termsize", ("rows", "cols", "x_pixels", "y_pixels")) # pylint: disable=invalid-name


class LoggableError(RuntimeError):
    """Errors that should be presented to a human."""


def to_str(val):
    """ Convert a property value to a text string, if it isn't already.
        Used when dumping property values to console or streams.
    """
    return val if isinstance(val, basestring) else str(val)


def escaped(text, docstr=False):
    """ Handle essential subset of Java property file escaping.

        @param text: Unescaped text.
        @param docstr: Is `text` a comment?
        @return: Escaped text.
    """
    if not docstr:
        text = (text
            .replace('\\', r'\\')
            .replace(':', r'\:')
            .replace('=', r'\=')
            .replace('#', r'\#')
            .replace('\r', r'\r')
            .replace('\n', r'\n')
        )

    if text.startswith(' ') or text.endswith(' '):
        text = text.replace(' ', "\\u0020")

    # Handle unicode data, without wasting time on pure ASCII
    if isinstance(text, unicode):
        try:
            text = text.encode("ascii")
        except UnicodeError:
            text = u''.join([r"\u%04x" % ord(i) if ord(i) > 255 else i for i in text]).encode('iso-8859-1')

    return text


def get_termsize():
    """ Return a termsize tuple, with 0 for unknown values.
    """
    if os.name != "posix":
        return termsize(0, 0, 0, 0)

    try:
        fd_stdout = sys.stdout.fileno()

        if not os.isatty(fd_stdout):
            raise EnvironmentError("not a tty") # effectively returns 0, 0, 0, 0

        import termios, fcntl, struct # import here, when system is POSIX

        sizes = struct.pack("HHHH", 0, 0, 0, 0)
        sizes = fcntl.ioctl(fd_stdout, termios.TIOCGWINSZ, sizes) #@UndefinedVariable

        return termsize(*struct.unpack("HHHH", sizes))
    except (AttributeError, EnvironmentError):
        return termsize(0, 0, 0, 0)

