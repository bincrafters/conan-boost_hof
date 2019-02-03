#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostHOFConan(base.BoostBaseConan):
    name = "boost_hof"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_hof"
    lib_short_names = ["hof"]
    header_only_libs = ["hof"]
