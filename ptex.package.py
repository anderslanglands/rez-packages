name='ptex'
version='2.2.1'

def commands():
    env.PTEX_ROOT='{root}'
    env.PTEX_HOME='{root}'
    env.PTEX_ROOT_DIR='{root}'
    env.PTEX_LOCATION='{root}'
    env.PATH.append('{root}/bin')
