from pxr import Sdf
import omni.isaac.RosBridgeSchema as ROSSchema


class RosAttribute(ROSSchema.RosBridgeComponent):
    def __init__(self, prim):
        # RosBridgeComponent:
        # __init__(_object*, pxrInternal_v0_20__pxrReserved__::UsdSchemaBase schemaObj)
        # __init__(_object*, pxrInternal_v0_20__pxrReserved__::UsdPrim prim)
        # __init__(_object*)
        super().__init__(prim)
        
    def __bool__(self):
        return self.GetPrim().IsDefined()

    @staticmethod
    def Define(stage, path):
        prim = stage.DefinePrim(path, "RosAttribute")
        return RosAttribute(prim)
    
    def CreateSetAttrSrvTopicAttr(self, value):
        self.GetPrim().CreateAttribute("setAttrSrvTopic", Sdf.ValueTypeNames.String, True).Set(value)

    def CreateGetAttrSrvTopicAttr(self, value):
        self.GetPrim().CreateAttribute("getAttrSrvTopic", Sdf.ValueTypeNames.String, True).Set(value)

    def CreateAttributesSrvTopicAttr(self, value):
        self.GetPrim().CreateAttribute("attributesSrvTopic", Sdf.ValueTypeNames.String, True).Set(value)

    def CreatePrimsSrvTopicAttr(self, value):
        self.GetPrim().CreateAttribute("primsSrvTopic", Sdf.ValueTypeNames.String, True).Set(value)

    @staticmethod
    def Get(stage, path):
        # Get(pxrInternal_v0_19__pxrReserved__::TfWeakPtr<pxrInternal_v0_19__pxrReserved__::UsdStage> stage, pxrInternal_v0_19__pxrReserved__::SdfPath path)
        prim = stage.GetPrimAtPath(path)
        return RosAttribute(prim)

    def GetSetAttrSrvTopicAttr(self):
        return self.GetPrim().GetAttribute("setAttrSrvTopic")

    def GetGetAttrSrvTopicAttr(self):
        return self.GetPrim().GetAttribute("getAttrSrvTopic")

    def GetAttributesSrvTopicAttr(self):
        return self.GetPrim().GetAttribute("attributesSrvTopic")

    def GetPrimsSrvTopicAttr(self):
        return self.GetPrim().GetAttribute("primsSrvTopic")

    @staticmethod
    def GetSchemaAttributeNames(includeInherited=True):
        names = []
        if includeInherited: 
            names = ROSSchema.RosBridgeComponent.GetSchemaAttributeNames(includeInherited)
        return names + ["setAttrSrvTopic", "getAttrSrvTopic" ,"attributesSrvTopic" , "primsSrvTopic"]
