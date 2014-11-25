file = 'irclog.txt'

def find_factoids(file):
    # Define a dictionary to hold keys and values
    names = {}
    # File opened for use in this block
    with open(file, "r") as fil:
        # Go through each line of the file
        for line in fil:
            # Get rid of timestamps (Look up slices to understand this better)
            line = line[20:]
            # Split by tab character so we can get the names of a user
            segments = line.split('\t')
            # Get the name on current line
            name = segments[0]
            # Define names to ignore.
            ignored_names = ['--', '<--', '-->', ' *', '']
            # Only record names we haven't defined to ignore
            if name not in ignored_names:
                # If the name exists in the dictionary, update its value
                if name in names:
                    names[name] += 1
                # Otherwise put it into the dictionary
                else:
                    names.update({name : 1})

    # Sort the names by their values (# of text entries)
    names = sorted(names.items(), key=lambda x: x[1])
    # Reverse the order so we have the highest first
    names = reversed(names)
    # Iterate over our reversed list of sorted names
    for n in names:
        # print the key (n[0]) and value (n[1]) for each
        print n[0] + " : " + str(n[1])

# If we are the program that was run to begin with, run the following code.
if __name__ == "__main__":
    # Use the find_factoids function with file as an argument
    find_factoids(file)    
