name='partio'
version='1.7.3'
requires=['seexpr-2.11']

def commands():
    env.PARTIO_ROOT='{root}'
    env.PARTIO_HOME='{root}'
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
    env.PATH.append('{root}/bin')
