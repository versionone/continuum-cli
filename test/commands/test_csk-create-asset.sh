# THIS IS JUST AN IDEA I DIDN'T WANT TO FORGET

# We can do semi-intelligent manual testing on a number of these commands.

x=`../getrandomname.py asset-`
result=`ccl-create-asset -n$x | grep $x`

if [[ "$result" == "" ]]; then
    exit 1
else
    exit 0
fi
