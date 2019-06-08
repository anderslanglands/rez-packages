name='ocio'
version='1.1.1'

def commands():
    env.OCIO_ROOT='{root}'
    env.OCIO_ROOT_DIR='{root}'
    env.OCIO_HOME='{root}'
    env.OCIO_PATH='{root}'
    env.OCIO_LOCATION='{root}'
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
