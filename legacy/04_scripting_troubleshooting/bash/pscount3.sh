#!/bin/bash

usage() {
    echo "Usage: $0 -n NAME"
    echo
    echo "Count number of processes given a name"
    echo
    echo "-n NAME   Name of the process to filter from"
    exit 0
}

while getopts "hn:" opt ; do # h does not require an argument, so no colon
    case $opt in
        n)
            NAME="$OPTARG" # $OPTARG is an environment variable set by getopts
            ;;
        h)
            usage
            ;;
        *)
            ;;
    esac
done

[ -z "$NAME" ] && usage # -z part means "if $name is empty"

# Long version of the above statement.
# if [ -z "$NAME" ] ; then
#     usage
# fi

ps aux | grep "$NAME" | grep -v "grep.*${NAME}" | grep -v "${0}.*${NAME}"
echo -n "Number of matches: " # -n means no newline at the end
ps aux | grep "$NAME" | grep -v "grep.*${NAME}" | grep -v "${0}.*${NAME}" | wc -l
# quotes around $NAME allow multi-word names
# curly-braces prevent interference from special characters such as / in directory paths
# look up parameter expansion for more information
