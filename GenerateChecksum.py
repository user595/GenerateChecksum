"""
scan folders for duplicate files
generate a MD5 checksum of the filename specified
i.e. /bin/python3 ~/Programming/Python/GenerateChecksum/GenerateChecksum.py .
MD5 checksum for GenerateChecksum.py: beec6281d78aad4a3c18d97dfad80518
"""
import hashlib
import sys
import glob
import os


def generate_checksum(pfile_path):
    """ parameter pfile_path used for input to MD5 generator """
    md5 = hashlib.md5()
    with open(pfile_path, 'rb') as file:  # with handles closing file
        for byte_block in iter(lambda: file.read(4096), b""):
            # read in by blocks of 4096 bytes until end of file
            md5.update(byte_block)  # update md5 object
    return md5.hexdigest()  # generate and return the hashcode


def add_to_data(pfile_path):
    """ store the file path and checksum, find duplicates """
    checksum = generate_checksum(pfile_path)

    if checksum in data:
        # Duplicate checksum found, print the existing and new file paths
        existing_file_path = data[checksum]
        print("Duplicate checksum found:")
        print(f"Checksum: {checksum}")
        print(f"Existing File Path: {existing_file_path}")
        print(f"New File Path: {pfile_path}")
    else:
        # Add the new file path to the dictionary
        data[checksum] = pfile_path


def process_files(pfolder_path):
    """ Use glob to get a list of all files matching the pattern
        in the specified folder and its sub-folders """
    file_list = glob.glob(os.path.join(pfolder_path, '**', '*'), recursive=True)

    for file_path in file_list:
        if os.path.isfile(file_path):
            # If the path points to a file (not a directory), generate and print the checksum
            # checksum = generate_checksum(file_path)
            # print(f"MD5 checksum for {file_path}: {checksum}")
            add_to_data(file_path)


if len(sys.argv) != 2:
    print("Usage: python checksum_generator.py <file_path> \
         to generate a MD5 checksum")
    sys.exit(1)


data = {}  # initialize dictionary for file path and checksum

folder_path = sys.argv[1]
process_files(folder_path)
