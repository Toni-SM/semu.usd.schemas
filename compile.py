from distutils.core import setup
from distutils.extension import Extension

from Cython.Distutils import build_ext


ext_modules = [
    Extension("_rosBridgeSchema",
              ["omni/add_on/RosBridgeSchema/rosBridgeSchema.py"],
              library_dirs=['/isaac-sim/kit/python/include']),
    Extension("_rosControlBridgeSchema",
              ["omni/add_on/RosControlBridgeSchema/rosControlBridgeSchema.py"],
              library_dirs=['/isaac-sim/kit/python/include']),
]

setup(
    name = 'omni.usd.schema.add_on',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
