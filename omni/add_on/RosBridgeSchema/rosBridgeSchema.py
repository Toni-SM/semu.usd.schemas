from pxr import Sdf
import omni.isaac.RosBridgeSchema as ROSSchema


class RosCompressedCamera(ROSSchema.RosBridgeComponent):
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
        prim = stage.DefinePrim(path, "RosCompressedCamera")
        return RosCompressedCamera(prim)

    def CreateCameraPrimRel(self):
        self.GetPrim().CreateRelationship("cameraPrim")

    def CreateResolutionAttr(self, value):
        self.GetPrim().CreateAttribute("resolution", Sdf.ValueTypeNames.Int2, True).Set(value)
    
    def CreateRgbPubTopicAttr(self, value):
        self.GetPrim().CreateAttribute("rgbPubTopic", Sdf.ValueTypeNames.String, True).Set(value)
    
    def CreateDepthPubTopicAttr(self, value):
        self.GetPrim().CreateAttribute("depthPubTopic", Sdf.ValueTypeNames.String, True).Set(value)
    
    def CreateFrameIdAttr(self, value):
        self.GetPrim().CreateAttribute("frameId", Sdf.ValueTypeNames.String, True).Set(value)
    
    def CreateRgbEnabledAttr(self, value):
        self.GetPrim().CreateAttribute("rgbEnabled", Sdf.ValueTypeNames.Bool, True).Set(value)
    
    def CreateDepthEnabledAttr(self, value):
        self.GetPrim().CreateAttribute("depthEnabled", Sdf.ValueTypeNames.Bool, True).Set(value)
    
    def CreateQueueSizeAttr(self, value):
        self.GetPrim().CreateAttribute("queueSize", Sdf.ValueTypeNames.Int, True).Set(value)

    @staticmethod
    def Get(stage, path):
        # Get(pxrInternal_v0_19__pxrReserved__::TfWeakPtr<pxrInternal_v0_19__pxrReserved__::UsdStage> stage, pxrInternal_v0_19__pxrReserved__::SdfPath path)
        prim = stage.GetPrimAtPath(path)
        return RosCompressedCamera(prim)

    def GetArticulationPrimRel(self):
        return self.GetPrim().GetRelationship("cameraPrim")

    def GetResolutionAttr(self):
        return self.GetPrim().GetAttribute("resolution")

    def GetRgbPubTopicAttr(self):
        return self.GetPrim().GetAttribute("rgbPubTopic")

    def GetDepthPubTopicAttr(self):
        return self.GetPrim().GetAttribute("depthPubTopic")

    def GetFrameIdAttr(self):
        return self.GetPrim().GetAttribute("frameId")

    def GetRgbEnabledAttr(self):
        return self.GetPrim().GetAttribute("rgbEnabled")

    def GetDepthEnabledAttr(self):
        return self.GetPrim().GetAttribute("depthEnabled")

    def GetQueueSizeAttr(self):
        return self.GetPrim().GetAttribute("queueSize")

    @staticmethod
    def GetSchemaAttributeNames(includeInherited=True):
        names = []
        if includeInherited: 
            names = ROSSchema.RosBridgeComponent.GetSchemaAttributeNames(includeInherited)
        return names + ["resolution", "rgbPubTopic", "depthPubTopic", "frameId", "rgbEnabled", "depthEnabled", "queueSize"]


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
