# “javaprops” Python Package

![logo](https://raw.githubusercontent.com/Feed-The-Web/javaprops/master/static/img/javaprops-128.png)

Read and write Java property files, including comments and location info.

![Apache 2.0 licensed](http://img.shields.io/badge/license-Apache_2.0-red.svg)


## Project Goals

This libary allows you to read Java property files including all the lesser known formatting details,
like Unicode escaping. What sets it apart from similar projects are these requirements:

* Modification of property files with minimal differences due to normalization.
* Comments are parsed and associated with their property key.
* Location information is available, mostly to improve diagnostics for humans.
* The property set can be exposed as a dict-like object with attribute semantics, mainly for use in template engines; stemmed values are supported.
* Provide an optional inclusion mechanism via special comments.


## Installation

To create a development environment, use these commands:

```sh
git clone https://github.com/Feed-The-Web/javaprops.git
cd javaprops; deactivate; /usr/bin/virtualenv .; . ./bin/activate
./bin/pip install -r dev-requirements.txt
invoke build --docs
```


## Usage

### Reading
**TODO**

### Writing
**TODO**

### Property Mapper
**TODO**

### Includes
**TODO**


## `javaprops` command line tool
**TODO**


## Similar Projects

* [jprops](https://github.com/mgood/jprops)
* [java-props-in-python](https://github.com/hackorama/java-props-in-python)
* [pyjavaproperties](https://bitbucket.org/jnoller/pyjavaproperties/)


## Contributing
**TODO**


## Acknowledgements

[![1&1](https://raw.githubusercontent.com/1and1/1and1.github.io/master/images/1and1-logo-42.png)](https://github.com/1and1)  Project sponsored by [1&1](https://github.com/1and1).
