def make_dir(dirname, clean=False):
    """
    Make a directory if it does not exist.
    Use clean=True to clobber the existing directory.
    """
    import shutil, os
    if clean == True:
        shutil.rmtree(dirname, ignore_errors=True)
        os.mkdir(dirname)
    else:
        try:
            os.mkdir(dirname)
        except OSError:
            pass # assume OSError was raised because directory already exists


def search(dirname, searchKey):
    """
    Searches for files in a given directory,
        can use regex wildcards or be given an explicit filepath to look for.
    Wildcard examples:
        *, returns every file.
        *.ext, returns every file of given extension
        [range], searches for numbers in range
    Returns:
        files: list of file paths
    """
    import glob
    files = glob.glob(f'{dirname}{searchKey}')
    return files


def autodelete(filename):
    """
    Checks to see if a file exists.
    If it does it attempts to remove it, if it can't it prints the error.
    """
    import os, sys
    if os.path.exists(filename):
        try:
            os.remove(filename)
        except Exception as e:
            print(f"Auto-delete had error: {e}")
            sys.exit()
    else:
        pass
