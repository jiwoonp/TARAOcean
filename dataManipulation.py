# Import Modules
try:
    import os, sys
    from zipfile import ZipFile
    import glob
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
raw_dir = f"{input_dir}raw/"

# Find each instance of data. So that you could run a big batch job.
rawData_dirs = glob.glob(f"{raw_dir}*")

for rawData_dir in rawData_dirs:
    zip = ZipFile(rawData_dir+'/abun_enviro_data.zip','r')
    # TO DO: Extract .csv files. Could put them to a separate folder.
    # Then do all manipulation within this FOR loop