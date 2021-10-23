## USD Add-on schemas for NVIDIA Omniverse Isaac Sim

> This extension enables the **USD schemas** for the add-ons

<br>

### Table of Contents

- [Add the extension to an NVIDIA Omniverse app and enable it](#extension)
- [Supported schemas](#schemas)
  - [omni.add_on.RosBridgeSchema module](#RosBridgeSchema)
    - [```RosCompressedCamera```](#RosCompressedCamera)
    - [```RosAttribute```](#RosAttribute)
  - [omni.add_on.RosControlBridgeSchema module](#RosControlBridgeSchema)
    - [```RosControlFollowJointTrajectory```](#RosControlFollowJointTrajectory)
    - [```RosControlGripperCommand```](#RosControlGripperCommand)

<br>

<a name="extension"></a>
### Add the extension to an NVIDIA Omniverse app and enable it

1. Add the the extension by following the steps described in [Extension Search Paths](https://docs.omniverse.nvidia.com/py/kit/docs/guide/extensions.html#extension-search-paths) or simply download and unzip the latest [release](https://github.com/Toni-SM/omni.usd.schema.add_on/releases) in one of the extension folders such as ```PATH_TO_OMNIVERSE_APP/exts```

    Git url as extension search path: ```git+https://github.com/Toni-SM/omni.usd.schema.add_on.git?branch=main&dir=exts```

2. Enable the extension by following the steps described in [Extension Enabling/Disabling](https://docs.omniverse.nvidia.com/py/kit/docs/guide/extensions.html#extension-enabling-disabling)
<br>

<a name="schemas"></a>
### Supported schemas

The following USD Schemas are supported:

<a name="RosBridgeSchema"></a>
**omni.add_on.RosBridgeSchema module**

<a name="RosCompressedCamera"></a>
* **RosCompressedCamera:** USD schema to publish ROS compressed images ([CompressedImage](https://docs.ros.org/en/api/sensor_msgs/html/msg/CompressedImage.html))
    
    ```python
    class RosCompressedCamera

    Bases: omni.isaac.RosBridgeSchema.RosBridgeComponent

    CreateCameraPrimRel()
    CreateDepthEnabledAttr()
    CreateDepthPubTopicAttr()
    CreateFrameIdAttr()
    CreateQueueSizeAttr()
    CreateResolutionAttr()
    CreateRgbEnabledAttr()
    CreateRgbPubTopicAttr()

    static Define()
    static Get()

    GetArticulationPrimRel()
    GetDepthEnabledAttr()
    GetDepthPubTopicAttr()
    GetFrameIdAttr()
    GetQueueSizeAttr()
    GetResolutionAttr()
    GetRgbEnabledAttr()
    GetRgbPubTopicAttr()
    static GetSchemaAttributeNames()
    ```

<a name="RosAttribute"></a>
* **RosAttribute:** USD scheme to create a ROS service to get or set a prim attribute
    
    ```python
    class RosAttribute

    Bases: omni.isaac.RosBridgeSchema.RosBridgeComponent

    CreateSetterSrvTopicAttr()
    CreateGetterSrvTopicAttr()

    static Define()
    static Get()

    GetSetterSrvTopicAttr()
    GetGetterSrvTopicAttr()
    static GetSchemaAttributeNames()
    ```

<a name="RosControlBridgeSchema"></a>
**omni.add_on.RosControlBridgeSchema module**

<a name="RosControlFollowJointTrajectory"></a>
* **RosControlFollowJointTrajectory:** USD schema to support ROS [FollowJointTrajectory](http://docs.ros.org/en/api/control_msgs/html/action/FollowJointTrajectory.html) action services
    
    ```python
    class RosControlFollowJointTrajectory

    Bases: omni.isaac.RosBridgeSchema.RosBridgeComponent

    CreateActionNamespaceAttr()
    CreateArticulationPrimRel()
    CreateControllerNameAttr()
    
    static Define()
    static Get()
    
    GetActionNamespaceAttr()
    GetArticulationPrimRel()
    GetControllerNameAttr()
    static GetSchemaAttributeNames()
    ```

<a name="RosControlGripperCommand"></a>
* **RosControlGripperCommand:** USD schema to support ROS [GripperCommand](http://docs.ros.org/en/api/control_msgs/html/action/GripperCommand.html) action services
    
    ```python
    class RosControlGripperCommand

    Bases: omni.isaac.RosBridgeSchema.RosBridgeComponent

    CreateActionNamespaceAttr()
    CreateArticulationPrimRel()
    CreateControllerNameAttr()
    
    static Define()
    static Get()
    
    GetActionNamespaceAttr()
    GetArticulationPrimRel()
    GetControllerNameAttr()
    static GetSchemaAttributeNames()
    ```