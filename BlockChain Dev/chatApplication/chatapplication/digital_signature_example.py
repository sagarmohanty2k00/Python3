from nacl import encoding, signing


# Process
# 1. First, our unencrypted, plaintext data is hashed(prevents tampering).
# 2. Then the hash is encrypted using the private key.
# 3. Then we attach (concatenate) the encrypted hash to the data.

# Generating keys
bitu_private_key= signing.SigningKey.generate()
bitu_poblic_key = bitu_private_key.verify_key