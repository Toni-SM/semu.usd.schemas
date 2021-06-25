## USD Add-on schemas for NVIDIA Omniverse Isaac Sim

> This extension enables the **USD schemas** for the add-ons.

<br>

### Table of Contents

- [Add the extension to NVIDIA Omniverse Isaac Sim and enable it](#extension)
- [Supported schemas](#schemas)

<br>

<a name="extension"></a>
### Add the extension to NVIDIA Omniverse Isaac Sim and enable it

1. Download the latest [release](https://github.com/Toni-SM/omni.usd.schema.add_on/releases), or any release according to your Isaac Sim version, and unzip it into the Isaac Sim's extension path (```/isaac-sim/exts```)
2. Enable the extension in the menu *Window > Extensions* under the same name

<br>

<a name="schemas"></a>
### Supported schemas

The following USD Schemas are supported:

**omni.add_on.RosBridgeSchema**

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

**omni.add_on.RosControlBridgeSchema**

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