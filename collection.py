"""
Code to request and download data for use in Ocean 506

"""


# Import Modules
try:
    import os, sys
    import argparse
    # Do we really want to use this? 
    sys.path.append(os.path.abspath('shared'))
    import directory
except ImportError:
    print(ImportError)
    sys.exit()

# Directory management
main_dir = os.path.abspath('.').split('/')[-1]
input_dir = f"../{main_dir}_input/"
output_dir = f"../{main_dir}_output/"
directory.make_dir(input_dir)
directory.make_dir(output_dir)


# Argument Parser
parser = argparse.ArgumentParser(description="Collector of data from the Ocean Gene Database")
parser.add_argument('-f', '--filename',  type=str,
                    help="Input filename to iterate sequences with")
args = parser.parse_args()

# Check to make sure file exists and parse inputs.
try:
    f = open(args.filename)
    lines = f.readlines()
    sequences = []
    sequence = ""
    for line in lines:
        if "END OF SEQUENCE" in line:
            sequences.append(sequence)
            sequence = ""
        else:
            sequence = sequence + line
    f.close()
except FileNotFoundError:
    print(f"File: {args.filename} does not exist")
    sys.exit()
except IOError:
    print(f"File: {args.filename} is not accessible")
    sys.exit()


