export LIBRARY_PATH=/isaac-sim/kit/python/include

# delete old data
rm -r build
rm _ros*.so
rm omni/add_on/RosBridgeSchema/*.so
rm omni/add_on/RosBridgeSchema/*.c
rm omni/add_on/RosControlBridgeSchema/*.so
rm omni/add_on/RosControlBridgeSchema/*.c

# compile code
/isaac-sim/kit/python/bin/python3 compile.py build_ext --inplace

# # move compiled file
mv _rosBridgeSchema.cpython-37m-x86_64-linux-gnu.so omni/add_on/RosBridgeSchema/
mv _rosControlBridgeSchema.cpython-37m-x86_64-linux-gnu.so omni/add_on/RosControlBridgeSchema/

# delete temporal data
rm -r build
rm omni/add_on/RosBridgeSchema/*.c
rm omni/add_on/RosControlBridgeSchema/*.c
