# ECDSA

Python implementation of ECDSA [Elliptic Curve Digital Signature Algorithm] with secp256k1.

**⚠️ Doesn't implement RFC6979 for secure secret point generation**

## Quick Start

```python
from src.math_from_scratch.elliptic_curve.secp256k1 import Secp256k1
from src.math_from_scratch.keys import generate_public_key, generate_private_key
from src.math_from_scratch.signature import create_signature, verify_signature

# Generate keys
private_key = generate_private_key(256)
public_key = generate_public_key(private_key)

# Sign
message = "Hello, ECDSA!"
signature = create_signature(message, private_key, Secp256k1())

# Verify
is_valid = verify_signature(message, signature, public_key, Secp256k1())
```

## Features

- No external crypto dependencies
- Private/public key generation
- Digital signature creation and verification
- secp256k1 curve (Bitcoin/Ethereum compatible)


## Run

Just run main.py