name='alusdmaya'
version='0.31.1'

requires=['usd-19.05', 'maya-2020pr102', 'gtest']

def commands():
    env.MAYA_PLUG_IN_PATH.append('{root}/plugin')
    env.PXR_PLUGINPATH_NAME.append('{root}/lib')
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append('{root}/lib/python')
