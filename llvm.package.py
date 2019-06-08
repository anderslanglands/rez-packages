# -*- coding: utf-8 -*-

name = 'llvm'

version = '8.0.0'

def commands():
    env.LLVM_ROOT='{root}'
    env.LLVM_DIR='{root}'
    env.LLVM_DIRECTORY='{root}'
    env.PATH.append('{root}/bin')

timestamp = 1555565216

format_version = 2
