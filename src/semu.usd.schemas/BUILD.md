## Building form source

### Linux

```bash
cd src/semu.usd.schemas
bash compile_extension.bash
```
 
## Removing old compiled files

Get a fresh clone of the repository and follow the next steps

```bash
# remove compiled files _rosBridgeSchema.cpython-37m-x86_64-linux-gnu.so, _rosControlBridgeSchema.cpython-37m-x86_64-linux-gnu.so
git filter-repo --invert-paths --path exts/semu.usd.schemas/semu/usd/schemas/RosBridgeSchema/_rosBridgeSchema.cpython-37m-x86_64-linux-gnu.so
git filter-repo --invert-paths --path exts/semu.usd.schemas/semu/usd/schemas/RosControlBridgeSchema/_rosControlBridgeSchema.cpython-37m-x86_64-linux-gnu.so

# add origin
git remote add origin git@github.com:Toni-SM/semu.usd.schemas.git

# push changes
git push origin --force --all
git push origin --force --tags
```

## Packaging the extension

```bash
cd src/semu.usd.schemas
bash package_extension.bash
```