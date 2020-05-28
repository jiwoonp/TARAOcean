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
rawData_dir = f"{raw_dir}request/"
rawUnzip_dir = f"{raw_dir}unzip/"
directory.make_dir(rawUnzip_dir)

# Find each instance of data. So that you could run a big batch job.
rawData_dirs = glob.glob(f"{rawData_dir}*")

for rawRequest_dir in rawData_dirs:
    # Verify that zip files are closed
    try: zip.close()
    except: pass
    zip = ZipFile(rawRequest_dir+'/abun_enviro_data.zip','r')
    zip.extractall(rawUnzip_dir)
    # Clean up zip files
    zip.close()
    





    # TO DO: 
    # Then do all manipulation within this FOR loop
    # Clean up. zip raw request data. delete unzip folder. save output to pickle