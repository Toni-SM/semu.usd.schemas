##  USD schemas for external extensions (under the `semu` namespace, for NVIDIA Omniverse Isaac Sim

> This extension enables the **USD schemas** for the external extensions under the `semu` namespace

<br>

**Target applications:** NVIDIA Omniverse Isaac Sim

**Supported OS:** Linux

**Changelog:** [CHANGELOG.md](src/semu.usd.schemas/docs/CHANGELOG.md)

**Table of Contents:**

- [Extension setup](#setup)
- [Supported schemas](#schemas)
  - [semu.usd.schemas.RosBridgeSchema module](#RosBridgeSchema)
    - [```RosAttribute```](#RosAttribute)
  - [semu.usd.schemas.RosControlBridgeSchema module](#RosControlBridgeSchema)
    - [```RosControlFollowJointTrajectory```](#RosControlFollowJointTrajectory)
    - [```RosControlGripperCommand```](#RosControlGripperCommand)

<br>

![showcase](src/semu.usd.schemas/data/preview.png)

<hr>

<a name="setup"></a>
### Extension setup

1. Add the extension using the [Extension Manager](https://docs.omniverse.nvidia.com/prod_extensions/prod_extensions/ext_extension-manager.html) or by following the steps in [Extension Search Paths](https://docs.omniverse.nvidia.com/py/kit/docs/guide/extensions.html#extension-search-paths)

    * Git url (git+https) as extension search path
    
        ```
        git+https://github.com/Toni-SM/semu.usd.schemas.git?branch=main&dir=exts
        ```

        To install the source code version use the following url

        ```
        git+https://github.com/Toni-SM/semu.usd.schemas.git?branch=main&dir=src
        ```

    * Compressed (.zip) file for import

        [semu.usd.schemas.zip](https://github.com/Toni-SM/semu.usd.schemas/releases)

2. Enable the extension using the [Extension Manager](https://docs.omniverse.nvidia.com/prod_extensions/prod_extensions/ext_extension-manager.html) or by following the steps in [Extension Enabling/Disabling](https://docs.omniverse.nvidia.com/py/kit/docs/guide/extensions.html#extension-enabling-disabling)

<hr>

<a name="schemas"></a>
### Supported schemas

The following USD Schemas are supported:

<a name="RosBridgeSchema"></a>
**semu.usd.schemas.RosBridgeSchema module**

<a name="RosAttribute"></a>
* **RosAttribute:** USD scheme to create a ROS service to get or set prim attributes
    
    ```python
    class RosAttribute

    Bases: omni.isaac.RosBridgeSchema.RosBridgeComponent

    CreatePrimsSrvTopicAttr()
    CreateAttributesSrvTopicAttr()
    CreateGetAttrSrvTopicAttr()
    CreateSetAttrSrvTopicAttr()

    static Define()
    static Get()

    GetPrimsSrvTopicAttr()
    GetAttributesSrvTopicAttr()
    GetGetAttrSrvTopicAttr()
    GetSetAttrSrvTopicAttr()

    static GetSchemaAttributeNames()
    ```

<a name="RosControlBridgeSchema"></a>
**semu.usd.schemas.RosControlBridgeSchema module**

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
    CreateGripperJointsRel()
    
    static Define()
    static Get()
    
    GetActionNamespaceAttr()
    GetArticulationPrimRel()
    GetControllerNameAttr()
    GetGripperJointsRel()

    static GetSchemaAttributeNames()
    ```
