import hashlib
from typing import Tuple

from src.math_from_scratch.curve_point import CurvePoint
from src.math_from_scratch.elliptic_curve.abstract_curve import Curve


def verify_signature(message: str, signature: Tuple[int, int], public_key: CurvePoint, curve: Curve) -> bool:
    message_hash = int.from_bytes(hashlib.sha256(message.encode()).digest(), 'big')
    signature_x_coordinate = signature[0]
    signature_y_coordinate = signature[1]

    # Calculate the inverse of signature's y coordinate with FLT
    signature_y_coordinate_inverse = pow(signature_y_coordinate, curve.order - 2, curve.order)

    # Recover the random point
    # Using formula R' = (h*s1)*G+(r*s1)*pubKey
    # ============================================================================================================
    intermediate_result = ((message_hash % curve.order) * signature_y_coordinate_inverse) % curve.order
    another_intermediate_result = curve.generator.multiply(intermediate_result)
    one_more_intermediate_result = ((
                                            signature_x_coordinate % curve.order) * signature_y_coordinate_inverse) % curve.order
    final_intermediate_result = public_key.multiply(one_more_intermediate_result)
    recovered_random_point = final_intermediate_result.add(another_intermediate_result)

    return signature_x_coordinate == recovered_random_point.point[0]
