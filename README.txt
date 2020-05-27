Project to download and analyze data from the Ocean Gene Atlas
Skills used.
    Shell scripting.
    argparse.
    subprocesses.
    local modules.
    Github repository management.
===============================================================================
Access
clone using: git clone https://github.com/delasislas/TARAOcean.git

NOTICE:
Navigate to the shared folder.
Type chmod +x OGArequest.sh
This lets python run the shell script as an executable.
===============================================================================
*collection.py
Usage: python collection.py -j jobname -f filename
Example: python collection.py -j test -f search.txt

filename refers to the list of sequences to search for.
filename can refered to with an absolute or relative path.

This file also creates the input and output directories for the project.
===============================================================================
*search.txt
Example format of sequences to search for.
NOTE: sequences need to be in FASTA format to be able to be run.
NOTE: include "END OF SEQUENCE" at the end of every sequence.
===============================================================================
*shared/directory.py
Module for directory management help.
===============================================================================
*shared/TARA.py
Module to call the Ocean Gene Atlas request.
===============================================================================
*shared/OGArequest.sh
Shell script to request data for each sequence asked for.
Sends request as a query to OGA.
Returns with the data from the server and stores in output as jobname_uniqueid.
Displays an error, that doesn't affect the outcome.
===============================================================================