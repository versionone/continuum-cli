#!/usr/bin/env bash
set -e
WORKSPACE=$PWD
OUTDIR=${WORKSPACE}/tmp
mkdir -p ${OUTDIR}

# CLIENT IS DIFFERENT ... we don't byte compile anything
cp -R README.md ${OUTDIR}
cp -R LICENSE ${OUTDIR}
cp -R bin ${OUTDIR}
cp -R ctmcommands ${OUTDIR}
cp -R setup.py ${OUTDIR}

# SPECIAL PACKAGING FOR THE CLIENT ONLY
cd ${OUTDIR}
mkdir -p ${WORKSPACE}/outputfiles
tar -czf ${WORKSPACE}/outputfiles/client.tar.gz .

# rearrange stuff for windows...
find bin -type f -exec mv {} {}.py \;

# -9 Indicates the slowest compression speed (optimal compression, ignores the suffix list)
# -y Store symbolic links as such in the zip archive, instead of compressing and storing the file referred to by the link
# -r Travel the directory structure recursively
# -q Quiet mode

zip -9 -y -r -q ${WORKSPACE}/outputfiles/client-win.zip .

rm -rf ${WORKSPACE}/tmp