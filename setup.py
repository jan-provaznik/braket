#!/usr/bin/env python3
#
# 2021 - 2022 Jan Provaznik (jan@provaznik.pro)

import setuptools

VERSION = '0.1'
DESCRIPTION = 'Dirac formalism: kets and bras.'

# Yes, yes, yes!

setuptools.setup(
    name = 'braket',
    version = VERSION,
    description = DESCRIPTION,
    author = 'Jan Provaznik',
    author_email = 'jan@provaznik.pro',
    url = 'https://provaznik.pro/braket',
    license = 'LGPL',
    packages = [ 'braket' ]
)

