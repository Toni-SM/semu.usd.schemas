from pxr import Tf

try:
    from . import _rosControlBridgeSchema
except:
    print(">>>> [DEVELOPMENT] import rosControlBridgeSchema")
    from . import rosControlBridgeSchema as _rosControlBridgeSchema

Tf.PrepareModule(_rosControlBridgeSchema, locals())
del Tf
