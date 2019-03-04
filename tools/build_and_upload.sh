#!/usr/bin/env bash
VERSION=$1
BUILD=$2
BRANCH=$3

tools/build.sh
tools/upload.sh ${VERSION} ${BUILD} ${BRANCH}