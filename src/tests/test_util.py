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


class ToStrTests(unittest.TestCase):

    def test_unscathed(self):
        unscathed = ('', u'', 'abc', u'äöü€')
        for text in unscathed:
            assert util.to_str(text) is text

    def test_none(self):
        assert util.to_str(None) == 'None'

    def test_int(self):
        assert util.to_str(1) == '1'


class EscapedTests(unittest.TestCase):
        #def util.escaped(text, docstr=False):

    def test_docstr(self):
        for char in '\\:=#':
            assert util.escaped(char) == '\\' + char
            assert util.escaped(char, docstr=True) == char
        assert util.escaped('\r') == r'\r'
        assert util.escaped('\n') == r'\n'
        assert util.escaped('\r\n', docstr=True) == '\r\n'

    def test_nostrip(self):
        assert util.escaped('a b') == 'a b'
        assert util.escaped(' a b') == '\\u0020a\\u0020b'
        assert util.escaped('a b ') == 'a\\u0020b\\u0020'
        assert util.escaped(' a b ') == '\\u0020a\\u0020b\\u0020'

    def test_ascii(self):
        assert util.escaped('abc') == 'abc'
        assert util.escaped(u'abc') == 'abc'

    def test_latin1(self):
        assert util.escaped(u'äöü') == u'äöü'.encode('iso-8859-1')

    def test_unicode(self):
        assert util.escaped(u'€') == '\\u20ac'


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
