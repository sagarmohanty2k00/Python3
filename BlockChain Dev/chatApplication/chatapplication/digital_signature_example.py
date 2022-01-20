from nacl import encoding, signing


# Process
# 1. First, our unencrypted, plaintext data is hashed(prevents tampering).
# 2. Then the hash is encrypted using the private key.
# 3. Then we attach (concatenate) the encrypted hash to the data.

# Generating keys
bitu_private_key= signing.SigningKey.generate()
bitu_public_key = bitu_private_key.verify_key

# creating hex of public key
bitu_public_key_hex = bitu_public_key.encode(encoder=encoding.HexEncoder)

# now sign a document
signed = bitu_private_key.sign(b"Send $37 to Mama")

verify_key = signing.VerifyKey(bitu_public_key_hex, encoder=encoding.HexEncoder)

try:
    print(f"Signed document : {signed}")
    print(verify_key.verify(signed).decode('utf-8'))
except:
    print("document is altered")
