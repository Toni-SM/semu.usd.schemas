#!/bin/bash

extension_dir=../../exts/semu.usd.schemas
extension_tree=semu/usd/schemas

# delete old files
rm -r $extension_dir

mkdir -p $extension_dir/$extension_tree/RosBridgeSchema
mkdir -p $extension_dir/$extension_tree/RosControlBridgeSchema

cp -r config $extension_dir
cp -r data $extension_dir
cp -r docs $extension_dir

# fill folder
cp $extension_tree/RosBridgeSchema/__init__.py $extension_dir/$extension_tree/RosBridgeSchema
cp $extension_tree/RosBridgeSchema/*.so $extension_dir/$extension_tree/RosBridgeSchema
cp $extension_tree/RosControlBridgeSchema/__init__.py $extension_dir/$extension_tree/RosControlBridgeSchema
cp $extension_tree/RosControlBridgeSchema/*.so $extension_dir/$extension_tree/RosControlBridgeSchema
