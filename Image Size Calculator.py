length = int(input("What is the length of the image in pixels?"))
width = int(input("What is the width of the image in pixels?"))
colour_depth = int(input("What is the colour depth in bits?"))
size = (width * length * colour_depth)
bytes = size / 8
kb = bytes / 1024
mb = kb / 1024
gb = mb / 1024
print(f"The file is {size} bits")
print(f"The file is {bytes} bytes")
print(f"The file is {kb} KB")
print(f"The file is {mb} MB")
print(f"The file is {gb} GB")
