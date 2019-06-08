name='alembic'
version='1.7.9'

requires=['boost-1.61', 'openexr-2.2']

def commands():
    env.ALEMBIC_ROOT='{root}'
    env.ALEMBIC_ROOT_DIR='{root}'
    env.ALEMBIC_DIR='{root}'
    env.ALEMBIC_HOME='{root}'
    env.ALEMBIC_LOCATION='{root}'
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')
