# -*- coding: utf-8 -*-

name = 'embree'

version = '2.17.7'

requires = [
    'tbb-maya2020',
    'ispc-1.11'
]

def commands():
    env.EMBREE_LOCATION='{root}'
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')

timestamp = 1555794525

format_version = 2
