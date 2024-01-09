import hashlib

def generate_checksum(file_path):
    md5 = hashlib.md5()
    with open(file_path, 'rb') as file:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: file.read(4096), b""):
            md5.update(byte_block)
    return md5.hexdigest()

# Example usage:
file_path = 'your_file_path_here.txt'
checksum = generate_checksum(file_path)
print(f"MD5 checksum for {file_path}: {checksum}")
