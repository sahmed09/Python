import hashlib

"""SHA ( Secure Hash Algorithms )- Base Of BlockChain
SHA256 : This hash function belong to hash class SHA-2, the internal block size of it is 32 bits.
SHA512 : This hash function belong to hash class SHA-2, the internal block size of it is 64 bits.
SHA384 : This hash function belong to hash class SHA-2, the internal block size of it is 32 bits.
        This is one of the truncated version.
SHA224 : This hash function belong to hash class SHA-2, the internal block size of it is 32 bits.
        This is one of the truncated version.
SHA1 : The 160 bit hash function that resembles MD5 hash in working and was discontinued to be used seeing
        its security vulnerabilities.

Blockchain Demo: https://github.com/anders94/blockchain-demo
https://andersbrownworth.com/blockchain/hash"""

message = 'Shihab Ahmed'

# Process of Hashing
# First step is to encode. Then Apply hashing Algorithms.

# SHA256
hash_val_256 = hashlib.sha256(message.encode())
print(hash_val_256)
# convert this value to hexadecimal
hash_val_256 = hash_val_256.hexdigest()
print('SHA256 - length {}: {}'.format(len(hash_val_256), hash_val_256))

# SHA512
hash_val_512 = hashlib.sha512(message.encode())
hash_val_512 = hash_val_512.hexdigest()
print('SHA512 - length {}: {}'.format(len(hash_val_512), hash_val_512))

# SHA384
hash_val_384 = hashlib.sha384(message.encode())
hash_val_384 = hash_val_384.hexdigest()
print('SHA384 - length {}: {}'.format(len(hash_val_384), hash_val_384))

# SHA224
hash_val_224 = hashlib.sha224(message.encode())
hash_val_224 = hash_val_224.hexdigest()
print('SHA224 - length {}: {}'.format(len(hash_val_224), hash_val_224))

# SHA1
hash_val_1 = hashlib.sha1(message.encode())
hash_val_1 = hash_val_1.hexdigest()
print('SHA1 - length {}: {}'.format(len(hash_val_1), hash_val_1))
