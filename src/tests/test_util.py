# -*- coding: utf-8 -*-
# pylint: disable=
""" Tests for `javaprops.util`.
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
import unittest

from javaprops import util


class GetTermsizeTests(unittest.TestCase):

    def test_named_tuple(self):
        ts = util.get_termsize()
        assert len(ts) == 4
        assert type(ts.rows) is int
        assert type(ts.cols) is int
        assert type(ts.x_pixels) is int
        assert type(ts.y_pixels) is int

    def test_non_posix(self):
        if os.name != "posix":
            assert util.get_termsize() == util.termsize(0, 0, 0, 0)

    def test_posix_tty(self):
        if os.name != "posix":
            return
        sys_stdout = sys.stdout
        try:
            sys.stdout = open("/dev/tty", "wb")
            ts = util.get_termsize()
            assert ts.rows >= 1
            assert ts.cols >= 40
        finally:
           sys.stdout = sys_stdout

    def test_posix_non_tty(self):
        if os.name != "posix":
            return
        sys_stdout = sys.stdout
        try:
            sys.stdout = open("/dev/null", "wb")
            ts = util.get_termsize()
            assert util.get_termsize() == util.termsize(0, 0, 0, 0)
        finally:
           sys.stdout = sys_stdout
