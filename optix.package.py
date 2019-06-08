name='optix'
version='6.0.0'

requires=['cuda-9+']

def commands():
    env.OPTIX_ROOT='{root}'
    env.OPTIXHOME='{root}'
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib64')
