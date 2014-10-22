#!/usr/bin/env bash
set -e

# create artifact
PRODUCT=client
FILENAME=${PRODUCT}-${BUILD_NUMBER}
mkdir -p artifact/${PRODUCT}
cp -R  README.md LICENSE bin cskcommands setup.py artifact/${PRODUCT}
cd artifact 
tar -czf ${FILENAME}.tar.gz ${PRODUCT}
. ~/.awscreds
s3put -b jenkinsbuilds.cloudsidekick.com --grant public-read --prefix ${PWD}/ ${FILENAME}.tar.gz
set +x
echo "[CSKARTIFACT:{\"name\": \"${PRODUCT}\", \"location\": \"https://s3.amazonaws.com/jenkinsbuilds.cloudsidekick.com/${FILENAME}.tar.gz\"}]"
