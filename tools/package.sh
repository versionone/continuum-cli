#!/usr/bin/env bash
set -e

# create artifact
PRODUCT=client
FILENAME=${PRODUCT}-${BUILD_NUMBER}
mkdir -p artifact/${PRODUCT}
cp -R  README.md LICENSE bin cskcommands setup.py artifact/${PRODUCT}
cd artifact 
tar -czf ${FILENAME}.tar.gz ${PRODUCT}
find ${PRODUCT}/bin -type f -exec mv {} {}.py \;
tar -czf ${FILENAME}-win.tar.gz ${PRODUCT}
mkdir ${WORKSPACE}/${PRODUCT}
mv ${FILENAME}.tar.gz ${WORKSPACE}/${PRODUCT}/.
mv ${FILENAME}-win.tar.gz ${WORKSPACE}/${PRODUCT}/.
cd $WORKSPACE
. ~/.awscreds
s3put -b builds.clearcodelabs.com --grant public-read --prefix ${PWD}/ ${PRODUCT}/${FILENAME}.tar.gz
s3put -b builds.clearcodelabs.com --grant public-read --prefix ${PWD}/ ${PRODUCT}/${FILENAME}-win.tar.gz
set +x
echo "[CCLARTIFACT:{\"name\": \"${PRODUCT}\", \"location\": \"https://s3.amazonaws.com/builds.clearcodelabs.com/${PRODUCT}/${FILENAME}.tar.gz\"}]"
echo "[CCLARTIFACT:{\"name\": \"${PRODUCT}-win\", \"location\": \"https://s3.amazonaws.com/builds.clearcodelabs.com/${PRODUCT}/${FILENAME}-win.tar.gz\"}]"
echo "done"
