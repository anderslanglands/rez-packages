name='oiio'
version='2.0.7'

requires=['boost-1.61', 'ocio-1.1', 'openexr-2.2']

def commands():
    env.OIIO_ROOT='{root}'
    env.OIIO_ROOT_DIR='{root}'
    env.OPENIMAGEIO_ROOT_DIR='{root}'
    env.OIIO_HOME='{root}'
    env.OIIO_LOCATION='{root}'
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')
    # env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
