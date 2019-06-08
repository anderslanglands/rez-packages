name='osl'
version='1.11.0'
requires=['oiio-2.0']

def commands():
    env.OSL_ROOT='{root}'
    env.OSL_LOCATION='{root}'
    env.OSL_ROOT_DIR='{root}'
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')

