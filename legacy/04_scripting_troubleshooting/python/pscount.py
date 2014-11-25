import subprocess
import sys


# Define correct usage
def usage():
    print "Usage: -n NAME"
    print ""
    print "Count number of processes given a name"
    print ""
    print "-n NAME   Name of the process to filter from"


def count_processes():
    # Initialize count
    count = 0

    # Assign the input to a more readable variable
    name = sys.argv[2]

    # Get the output from running the bash command "ps aux"
    # The \ allows a statement to span over more than 1 line.
    output = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE) \
                .communicate()[0]

    # Go through each line of output
    for line in output.split("\n"):

        # If the correct name was found, show it and increment count
        if name in line:
            print line
            count += 1

    print "Number of matches: " + str(count)

# If this was called from the command line, do the following:
if __name__ == "__main__":

    # Check for correct args and number of args
    if len(sys.argv) < 3 or sys.argv[1] != "-n":
        usage()
    else:
        count_processes()
