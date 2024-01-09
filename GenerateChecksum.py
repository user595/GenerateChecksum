"""
generate a MD5 checksum of the filename specified
i.e. /bin/python3 ~/Programming/Python/GenerateChecksum/GenerateChecksum.py GenerateChecksum.py 
MD5 checksum for GenerateChecksum.py: beec6281d78aad4a3c18d97dfad80518
"""
import hashlib
import sys

def generate_checksum(file_path):
    md5 = hashlib.md5()
    with open(file_path, 'rb') as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            md5.update(byte_block)
    return md5.hexdigest()

if len(sys.argv) != 2:
    print("Usage: python checksum_generator.py <file_path>     to generate a MD5 checksum")
    sys.exit(1)

file_path = sys.argv[1]
checksum = generate_checksum(file_path)
print(f"MD5 checksum for {file_path}: {checksum}")
