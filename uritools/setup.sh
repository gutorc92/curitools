#!/bin/sh

problem=$1;
gityes=1
if [ "$#" -eq 2 ];
then
    echo $@ > /tmp/checkoptions
    result=$(egrep -o "(-s)" /tmp/checkoptions)
    if [ $result = "-s" ];
    then
        gityes=0
    fi
    rm /tmp/checkoptions
fi

if [ $gityes -eq 1 ];
then
    git checkout -b "$problem";
fi 

if [ ! -d "$problem" ];
then
	mkdir "$problem";
	cp base.cpp "$problem/$problem.cpp";
	sed s/namefile/$problem.cpp/g Makefile >> $problem/Makefile
else
	echo "File already exists";	
fi
 
	

