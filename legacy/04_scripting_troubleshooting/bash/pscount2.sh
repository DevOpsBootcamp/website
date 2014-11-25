#!/bin/bash

while getopts "n:" opt ; do # : means that the -n flag is required; loop
    case $opt in
        n)
            NAME="$OPTARG"
            ;;
        *)
            ;;
    esac # end of case statement
done

# second grep pulls out the first grep process from the list
ps aux | grep $NAME | grep -v "grep.*${NAME}" | wc -l 
