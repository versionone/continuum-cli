#!/bin/bash

# this tests commands against a known set of test data
OUTFMT=$1

if [ "$1" == "text" ]
then
	OUTFMT="$1 -L$2"
fi

# ./cato-list-cloud-accounts -F$OUTFMT
# echo "#####"
# ./cato-list-clouds -F$OUTFMT
# echo "#####"
# ./cato-list-deployments -F$OUTFMT
# echo "#####"
# ./cato-list-processes -F$OUTFMT
# echo "#####"
# ./cato-list-tasks -F$OUTFMT
# echo "#####"

./cato-get-task -t"All Commands" -F$OUTFMT
echo "#####"
./cato-describe-task-parameters -t"All Commands" -F$OUTFMT
echo "#####"

./cato-get-task-instances -F$OUTFMT -r10
echo "#####"

./cato-get-task-instance -F$OUTFMT -i"4929"
echo "#####"
./cato-get-task-instance-status -F$OUTFMT -i"4929"
echo "#####"
./cato-get-task-log -F$OUTFMT -i"4929"
echo "#####"

# ./cato-get-deployment -F$OUTFMT -n"Test Deployment"
# echo "#####"
# ./cato-get-deployment-services -F$OUTFMT -n"Test Deployment"
# echo "#####"
# ./cato-get-deployment-service-states -F$OUTFMT -n"Test Deployment" -v"Service A"
# echo "#####"
# ./cato-get-deployment-steps -F$OUTFMT -n"Test Deployment"
# echo "#####"



