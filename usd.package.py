name='usd'
version='19.05'

requires=['oiio-2.0', 'osl-1.11', 'alembic-1.7', 'osd-3.3', 'embree-2.17', 'tbb-maya2020', 'materialx-1.36', 'katana-3.1v4']
build_requires=['PySide']

def commands():
    env.USD_ROOT='{root}'
    env.PATH.append('{root}/bin')
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.MAYA_PLUG_IN_PATH.append('{root}/third_party/maya/plugin')
    env.MAYA_SCRIPT_PATH.append('{root}/third_party/maya/lib/usd/usdMaya/resources')
    env.MAYA_SCRIPT_PATH.append('{root}/third_party/maya/plugin/pxrUsdPreviewSurface/resources')
    env.PYTHONPATH.append('{root}/lib/python')
    env.XBMLANGPATH.append('{root}/third_party/maya/lib/usd/usdMaya/resources')
    env.KATANA_RESOURCES.append('{root}/third_party/katana/plugin')
    env.KATANA_POST_PYTHONPATH.append('{root}/third_party/katana/lib')
    env.HOUDINI_PATH = '{root}/third_party/houdini:&'
    env.HOUDINI_DSO_ERROR = '1'
    env.HOUDINI_DSO_PATH = '@/plugin:&'
    env.HOUDINI_SCRIPT_PATH = '@/scripts:{root}/lib:&'
    env.HOUDINI_PYTHON_LIB = '/usr/lib/python2.7/config-x86_64-linux-gnu/libpython2.7.so'

