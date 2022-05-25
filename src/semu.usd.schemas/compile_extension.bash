#!/bin/bash

export LIBRARY_PATH=~/.local/share/ov/pkg/code-2022.1.0/kit/python/include

# delete old files
. clean_extension.bash

# compile code
~/.local/share/ov/pkg/code-2022.1.0/kit/python/bin/python3 compile_extension.py build_ext --inplace

# move compiled files
mv _rosBridgeSchema*.so semu/usd/schemas/RosBridgeSchema/
mv _rosControlBridgeSchema*.so semu/usd/schemas/RosControlBridgeSchema/

# delete temporal data
rm -r build
rm semu/usd/schemas/*/*.c
