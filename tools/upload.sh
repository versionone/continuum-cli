#!/usr/bin/env bash
set -e
VERSION=$1
BUILD=$2
# branch will be nothing blank if master branch
BRANCH=$3
WORKSPACE=$PWD
OUTDIR=${WORKSPACE}/outputfiles

mv ${OUTDIR}/client-win.zip ${OUTDIR}/client/continuum-client-${VERSION}.${BUILD}${BRANCH}-windows.zip
mv ${OUTDIR}/client.tar.gz ${OUTDIR}/client/continuum-client-${VERSION}.${BUILD}${BRANCH}.tar.gz

aws s3 cp ${OUTDIR}/client/continuum-client-${VERSION}.${BUILD}${BRANCH}-windows.zip s3://versionone-builds/continuum/client/continuum-client-${VERSION}.${BUILD}${BRANCH}-windows.zip --acl public-read --quiet
aws s3 cp ${OUTDIR}/client/continuum-client-${VERSION}.${BUILD}${BRANCH}.tar.gz s3://versionone-builds/continuum/client/continuum-client-${VERSION}.${BUILD}${BRANCH}.tar.gz --acl public-read --quiet
