import  hashlib

# hash functions expect the input to be in bytes so we convert srting to bytes
input_bytes = b"hello my name is sagar"
# here the selected function in sha256() which takes bytes as input and returns bytes as output
output_bytes = hashlib.sha256(input_bytes)

# we convert the byte code to hex code for better readabiliy
print(output_bytes.hexdigest())