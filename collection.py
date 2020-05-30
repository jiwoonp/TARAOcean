"""
Code to request and download data for use in Ocean 506

"""


# Import Modules
try:
    import os, sys
    import argparse
    import time
    # Do we really want to use this? 
    sys.path.append(os.path.abspath('shared'))
    import directory, TARA
except ImportError:
    print(ImportError)
    sys.exit()

# Directory management
main_dir = os.path.abspath('.').split('/')[-1]
input_dir = f"../{main_dir}_input/"
output_dir = f"../{main_dir}_output/"
raw_dir = f"{input_dir}raw/"
rawData_dir = f"{raw_dir}request/"

print("Making directories")
directory.make_dir(input_dir)
directory.make_dir(output_dir)
directory.make_dir(raw_dir)
directory.make_dir(rawData_dir)

# Argument Parser
parser = argparse.ArgumentParser(description="Collector of data from the Ocean Gene Database")
parser.add_argument('-j', '--job', default = "Temp", type=str,
                    help="Job to associate data collection with")
parser.add_argument('-f', '--filename', type=str,
                    help="Input filename to iterate sequences with")
args = parser.parse_args()

# Check to make sure file exists and parse inputs.
print("Parsing sequences")
try:
    f = open(args.filename)
    lines = f.readlines()
    sequences = []
    sequence = ""
    for line in lines:
        if "END OF SEQUENCE" in line:
            sequences.append(sequence)
            sequence = ""
            print("End of sequence")
        else:
            sequence = sequence + line
    f.close()
except FileNotFoundError:
    print(f"File: {args.filename} does not exist")
    sys.exit()
except IOError:
    print(f"File: {args.filename} is not accessible")
    sys.exit()
print(f"Count of Sequences: {len(sequences)}")
print("="*80)
# Send request
for sequence in sequences:
    print(sequence)
    TARA.OGArequest(f"{args.job}", f"{sequence}")
    # Sleep as a default to prevent accidentally DDOSing the OGA server.
    time.sleep(30)
