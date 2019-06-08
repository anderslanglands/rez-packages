name='osd'
version='3.3.3'

requires=['openexr-2.2', 'cuda-10', 'ptex-2.2']

def commands():
    env.OPENSUBDIV_ROOT='{root}'
    env.OPENSUBDIV_ROOT_DIR='{root}'
    env.OPENSUBDIV_HOME='{root}'
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')
