from src.math_from_scratch.elliptic_curve.secp256k1 import Secp256k1
from src.math_from_scratch.keys import generate_public_key, generate_private_key
from src.math_from_scratch.signature import create_signature, verify_signature

if __name__ == "__main__":
    private_key = generate_private_key(256)
    public_key = generate_public_key(private_key)
    elliptic_curve = Secp256k1()

    message = "It better be working"
    signature = create_signature(message, private_key, elliptic_curve)

    verification_result = verify_signature(message, signature, public_key, elliptic_curve)

    print(verification_result)
