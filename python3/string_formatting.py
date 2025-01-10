def print_formatted(number):
    # your code goes here
    padding = len("{0:b}".format(number))
    for i in range(1,number+1):
        print("{0:d}".format(i).rjust(padding),"{0:o}".format(i).rjust(padding),"{0:X}".format(i).rjust(padding),"{0:b}".format(i).rjust(padding))