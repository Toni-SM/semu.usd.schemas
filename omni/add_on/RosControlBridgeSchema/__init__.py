from pxr import Tf

try:
    from . import _rosControlBridgeSchema
except:
    from . import rosControlBridgeSchema as _rosControlBridgeSchema

Tf.PrepareModule(_rosControlBridgeSchema, locals())
del Tf
