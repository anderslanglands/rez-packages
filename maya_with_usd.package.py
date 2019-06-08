name='maya_with_usd'
version='0.1.0'

def commands():
    env.MAYA_PLUG_IN_PATH.append('/home/anders/packages/usd/19.05/third_party/maya/plugin')
    env.MAYA_SCRIPT_PATH.append('/home/anders/packages/usd/19.05/third_party/maya/lib/usd/usdMaya/resources')
    env.MAYA_SCRIPT_PATH.append('/home/anders/packages/usd/19.05/third_party/maya/plugin/pxrUsdPreviewSurface/resources')
    env.PYTHONPATH.append('/home/anders/packages/usd/19.05/lib/python')
    env.LD_LIBRARY_PATH.append('/home/anders/packages/openexr/2.2.1/lib')
    env.LD_LIBRARY_PATH.append('/home/anders/packages/ptex/2.2.1/lib')
