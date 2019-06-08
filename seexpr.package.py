name='seexpr'
version='2.11'

def commands():
    env.SEEXPR_ROOT='{root}'
    env.LD_LIBRARY_PATH.append('{root}/lib')
