# -*- coding: utf-8 -*-
# pylint: disable=bad-whitespace
""" javaprops - Read and write Java property files.

    This libary allows you to read Java property files including all the
    lesser known formatting details, like Unicode escaping. What sets it
    apart from similar projects are these requirements:

    * Modification of property files with minimal differences due to normalization.
    * Comments are parsed and associated with their property key.
    * Location information is available, mostly to improve diagnostics for humans.
    * The property set can be exposed as a dict-like object with attribute semantics,
      mainly for use in template engines; stemmed values are supported.
    * Provide an optional inclusion mechanism via special comments.

    Copyright ⓒ  2015 1&1 Group

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
__url__             = 'https://github.com/Feed-The-Web/javaprops'
__version__         = '0.1.0'
__license__         = 'Apache 2.0'
__author__          = 'Jürgen Hermann'
__author_email__    = 'jh@web.de'

#from javaprops.mapper import PropertyMapper
#from javaprops.templates import PropertyFilter, PropertyLogger


__all__ = [
    #'',
    #'PropertyMapper',
    #'PropertyFilter',
    #'PropertyLogger',
]
