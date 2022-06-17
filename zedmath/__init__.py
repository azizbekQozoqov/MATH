"""
MATH library for python
Made by https://www.azizbekdev.com \n
v0.0.1
"""

if __name__ != "__main__":
    from .library import MATH as rt
else:
    from library import MATH as rt

MATH = rt()
PI = MATH.PI
pow = MATH.pow
abs = MATH.abs
round = MATH.round
sum = MATH.sum
is_odd = MATH.is_odd