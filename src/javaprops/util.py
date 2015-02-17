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

