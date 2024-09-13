from bip_utils import Bip39SeedGenerator, Bip32Slip10Secp256k1
import hashlib
from Crypto.Hash import SHA256, RIPEMD160

# Example BIP-39 seed phrase
seed_phrase = "ice focus breeze input clinic grief rapid firm picnic broken amount above"

# Convert the BIP-39 seed phrase to a seed (512 bits, typically 64 bytes)
seed = Bip39SeedGenerator(seed_phrase).Generate()

# Generate the BIP-32 master key pair
bip32_ctx = Bip32Slip10Secp256k1.FromSeed(seed)
master_public_key = bip32_ctx.PublicKey().RawCompressed().ToBytes()

# Hash the master public key with SHA-256 and then RIPEMD-160
# sha256_hash = hashlib.sha256(master_public_key).digest()
# ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
# Hash the master public key with SHA-256
sha256_hash = SHA256.new(master_public_key).digest()
# Hash the SHA-256 result with RIPEMD-160
ripemd160_hash = RIPEMD160.new(sha256_hash).digest()

# Take the first 4 bytes of the RIPEMD-160 hash
fingerprint = ripemd160_hash[:4]

# Convert to a hexadecimal string for readable output
fingerprint_hex = fingerprint.hex()

print("Fingerprint (first 4 bytes):", fingerprint_hex)