#!/usr/bin/env bash

version=$1

if [ "$version" = "" ] ; then
    echo "usage: $0 <release>"
    exit 1
fi
git pull
echo $version > VERSION

git add VERSION
git commit -m "bump release to $release"
git push
git tag -a $version -m "Version $version"
git push --tags
