from pxr import Tf

try:
    from . import _rosBridgeSchema
except:
    print(">>>> [DEVELOPMENT] import rosBridgeSchema")
    from . import rosBridgeSchema as _rosBridgeSchema

Tf.PrepareModule(_rosBridgeSchema, locals())
del Tf
