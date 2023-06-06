#!/bin/bash

# Download Brick nightly
pushd ontologies/brick
curl -LO https://github.com/BrickSchema/Brick/releases/download/nightly/imports.zip
curl -LO https://github.com/BrickSchema/Brick/releases/download/nightly/Brick.ttl
unzip imports.zip
mv imports/*.ttl .
rmdir imports
rm imports.zip
popd

## TODO: 223P

## TODO: RealEstateCore
