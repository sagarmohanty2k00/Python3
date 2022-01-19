from nacl.public import PrivateKey, Box


# suppose characters are Bitu and Mama
# let's create private_key for both
bitu_private_key = PrivateKey.generate()
mama_private_key = PrivateKey.generate()


# let's create public_key for both
bitu_public_key = bitu_private_key.public_key
mama_public_key = mama_private_key.public_key


# Bitu will send a message to Mama
# So first Bitu will first create a box with his private_key and Mama's public_key
bitu_box = Box(bitu_private_key, mama_public_key)


message = "Hi mama, It's a encrypted message"
message = bitu_box.encrypt(message.encode())
# print(message)

# For decrypting the message Mama will also create a box
mama_box = Box(mama_private_key, bitu_public_key)
message = mama_box.decrypt(message)
print(message.decode('utf-8'))