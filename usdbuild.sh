#! /bin/sh

rez-build --install -- \
      -DPXR_ENABLE_OSL_SUPPORT=ON \
      -DPXR_BUILD_DOCUMENTATION=ON \
      -DPXR_BUILD_OPENIMAGEIO_PLUGIN=ON \
      -DPXR_BUILD_OPENCOLORIO_PLUGIN=ON \
      -DPXR_BUILD_EMBREE_PLUGIN=ON \
      -DPXR_BUILD_ALEMBIC_PLUGIN=ON \
      -DPXR_ENABLE_HDF5_SUPPORT=OFF \
      -DPXR_BUILD_MAYA_PLUGIN=ON \
      -DMAYA_LOCATION=/usr/autodesk/maya2020 \
      -DMAYA_tbb_LIBRARY=/usr/autodesk/maya2020/lib/libtbb.so \
      -DPXR_BUILD_KATANA_PLUGIN=ON \
      -DPXR_BUILD_MATERIALX_PLUGIN=ON \
      -DTBB_tbb_LIBRARY=/usr/autodesk/maya2020/lib/libtbb.so \
      -DMAYA_tbb_LIBRARY=/usr/autodesk/maya2020/lib/libtbb.so \
      -DPXR_BUILD_HOUDINI_PLUGIN=ON \
      -DHOUDINI_ROOT=$HOME/packages/houdini/17.5.229
