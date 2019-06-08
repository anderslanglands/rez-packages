name='mtoh'
version='2019.04.09'

requires=['alusdmaya-0.31']

def commands():
    env.MAYA_PLUG_IN_PATH.append('{root}/plug-ins')
    env.PXR_PLUGINPATH_NAME.append('{root}/lib')
