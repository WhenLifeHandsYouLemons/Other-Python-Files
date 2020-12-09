"""
For IGCSE Computer Science course
"""

import hashlib

original = input("Message: ")

# Convert string to array of bytes
byte_array = original.encode('utf-8')

md5 = hashlib.md5(byte_array).digest()
sha1 = hashlib.sha1(byte_array).digest()
sha3_256 = hashlib.sha256(byte_array).digest()

print("md5 = "+md5.hex())
print("sha1 = "+sha1.hex())
print("sha3_256 = "+sha3_256.hex())
