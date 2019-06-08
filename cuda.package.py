name='cuda'
version='10.1'

def commands():
    env.CUDA_TOOLKIT_ROOT_DIR='{root}'
    env.CUDA_ROOT='{root}'
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib64')
