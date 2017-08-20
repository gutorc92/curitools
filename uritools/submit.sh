#!/bin/sh

jarFile="$HOME/Documents/uri/"
oldPWD=$PWD
problem=$(basename $PWD)

file="$PWD/$problem.cpp"
echo "You will submit the problem $problem"
echo "The file $file will be used"

cd "$jarFile"
echo " Actual $PWD"

if [ -e "$file" ];
then
   java -jar "$jarFile/urisubmit-1.0-SNAPSHOT.jar" "$file" "$problem"
else
    echo "There is no a cpp file"
fi
 
cd "$oldPWD"
echo "New $PWD"

