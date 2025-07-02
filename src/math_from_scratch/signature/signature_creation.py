import hashlib
import random


def create_signature(message: str, private_key: int, curve: 'Curve'):
    message_hash = int.from_bytes(hashlib.sha256(message.encode()).digest(), 'big')

    # This is insecure! Unfortunately, I'm too lazy to implement RFC6979
    secret = random.randint(1, curve.order - 1)

    generator_point = curve.generator
    random_point = generator_point.multiply(secret)

    random_point_x_coordinate = random_point.point[0]

    # Calculating signature proof
    # Using formula R' = (h*s1) * G + (r * s1) * pubKey
    # ============================================================================================================
    # 1) Inverse of secret
    secret_inverse = pow(secret, curve.order - 2, curve.order)  # Probably not optimal
    # 2) Calculate the product of random point's x coordinate and private key
    intermediate_result = ((random_point_x_coordinate % curve.order) * (private_key % curve.order)) % curve.order
    # 3) Add up message hash and the intermediate result
    another_intermediate_result = ((message_hash % curve.order) + intermediate_result) % curve.order
    # 4) Final step, calculate the product of the secret's inverse with "another_intermediate_result"
    # Frankly, all of this could just be one formula
    result = (secret_inverse * another_intermediate_result) % curve.order

    return random_point_x_coordinate, result
