name='openexr'
version='2.2.1'

def commands():
    env.ILMBASE_HOME='{root}'
    env.ILMBASE_ROOT='{root}'
    env.ILMBASE_ROOT_DIR='{root}'
    env.ILMBASE_LOCATION='{root}'
    env.OPENEXR_HOME='{root}'
    env.OPENEXR_ROOT='{root}'
    env.OPENEXR_ROOT_DIR='{root}'
    env.OPENEXR_LOCATION='{root}'
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')
