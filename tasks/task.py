from typing import Tuple, Union
from math import sqrt


def solution(a, b, c) -> Union[Tuple[float, float], Tuple[float], None]:

    # Add your code here or call it from here
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        # No real roots
        result = None
    elif discriminant == 0:
        # One real root
        root = -b / (2*a)
        result = (root,)
    else:
        # Two real roots
        root1 = (-b - sqrt(discriminant)) / (2*a)
        root2 = (-b + sqrt(discriminant)) / (2*a)
        result = tuple(sorted((root1, root2)))

    return result

