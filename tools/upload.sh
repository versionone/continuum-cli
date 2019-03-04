#!/usr/bin/env bash
set -e
# branch will be nothing blank if master branch
BRANCH=$1
WORKSPACE=$PWD
OUTDIR=${WORKSPACE}/outputfiles

VERSION=${CI_PROJECT_VERSION}.${CI_JOB_NUMBER}${BRANCH}

mv ${OUTDIR}/client-win.zip ${OUTDIR}/continuum-client-${VERSION}-windows.zip
mv ${OUTDIR}/client.tar.gz ${OUTDIR}/continuum-client-${VERSION}.tar.gz

aws s3 cp ${OUTDIR}/continuum-client-${VERSION}-windows.zip s3://versionone-builds/continuum/client/continuum-client-${VERSION}-windows.zip --acl public-read --quiet
aws s3 cp ${OUTDIR}/continuum-client-${VERSION}.tar.gz s3://versionone-builds/continuum/client/continuum-client-${VERSION}.tar.gz --acl public-read --quiet
