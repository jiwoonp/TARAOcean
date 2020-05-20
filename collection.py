"""
Code to request and download data for use in Ocean 506

"""


# Import Modules
try:
    import os, sys
    import argparse
except ImportError:
    print(ImportError)
    sys.exit()

# Directory management
main_dir = os.path.abspath('.').split('/')[-1]
input_dir = f"../{main_dir}_input"
output_dir = f"../{main_dir}_output"



# Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='null', type=str)
args = parser.parse_args()

if args.filename == 'null':
    print("You need to input the sequences into a textfile.")
else:
    # Run code to read jobs from text file.
    pass
