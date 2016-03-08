#!/usr/bin/env python3
# Copyright (C) Ivo Slanina <ivo.slanina@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

import mqreceive

setup(
    name = "mqreceive",
    url = 'https://github.com/buben19/mqreceive',
    version = mqreceive.__version__,
    packages = find_packages(exclude = ['doc']),
    install_requires = ['paho-mqtt>=1.1'],
    author = mqreceive.__author__,
    author_email = mqreceive.__email__,
    description = "MQTT receive wrapper library",
    license = "GPLv3",
    classifiers = [
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
    ]
)
