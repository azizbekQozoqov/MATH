from typing import Any, Literal, Sequence, Union


class MATH:
    def __init__(self) -> None:
        self.PI = 3.141592653589793
    def pow(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        """
        - Returns the power of a number
        - This method returns Integer or Float data type.

        ### Example code:
        ```python
        import zedmath

        result = zedmath.pow(2, 4)

        print(result)
        ```

        ### Output:
        ```bash
        16
        ```
        """
        return x ** y
    def abs(self, a: Union[int, float]) -> Union[int, float]:
        """
        - Returns the absolute value of the argument.
        - This method returns Integer or Float data type.

        ### Example code:
        ```python
        import zedmath

        result = zedmath.abs(-2)

        print(result)
        ```

        ### Output:
        ```bash
        2
        ```
        """
        return a - a - a
    def round(self, a: Union[int, float]) -> Union[int, float]: 
        """
        - Round a number to a given precision in decimal digits.
        - This method returns Integer or Float data type.

        ### Example code:
        ```python
        import zedmath

        print(zedmath.round(3.5))
        print(zedmath.round(2.5))
        print(zedmath.round(5.4))
        print(zedmath.round(5.6))
        ```

        ### Output:
        ```bash
        4
        2
        5
        6
        ```
        """
        tmp = a-(a)//1
        if tmp > 1 - tmp:
            return int(a + 1 - tmp)
        if tmp < 1 - tmp:
            return int(a - tmp)
        else:
            if (a - tmp) % 2 == 0:
                return int(a - tmp)
            else:
                thisP = int(a - tmp)
                while True:
                    thisP += 1
                    if thisP % 2 == 0:
                        break
                return thisP
    def sum(self, *args: Union[int, float, str, list[Union[int, float, str]]]) -> Union[int, float]:
        """
        - Returns sum of the given numbers.
        - Data types: str, int, float

        ### Example code:
        ```python
        import zedmath

        print(zedmath.sum([2, 5, [5, 7], [4, "7.1"], [4, [16, 78]]], "19"))
        ```

        ### Output:
        ```bash
        147.1
        ```
        """
        def _do(a, start=0):
            all_Sum = 0
            for i in a:
                if type(i) == list:
                    all_Sum += _do(i, all_Sum)
                elif type(i) == int or type(i) == float:
                    all_Sum += i
                else:
                    try:
                        all_Sum += float(i)
                    except:
                        raise ValueError("Given value must be number.")
            return all_Sum
        return _do(args)
    def is_odd(self, a: int ) -> bool:
        """
        - Returns given numbers is odd or non odd.
        - Returns boolean data type.

        ### Example

        ```python
        import zedmath

        print(zedmath.is_odd(3))
        print(zedmath.is_odd(2))
        print(zedmath.is_odd(188))
        ```

        ### Output

        ```bash
        True
        False
        False
        ```
        """
        if type(a) != int:
            print(type(a))
            raise ValueError("Data type of given value must be int.")
        return (a+1) % 2 == 0
    def is_even(self, a:int) -> bool:
        """
        - Returns given numbers is even or non even.
        - Returns boolean data type.

        ### Example

        ```python
        import zedmath

        print(zedmath.is_even(3))
        print(zedmath.is_even(2))
        print(zedmath.is_even(188))
        ```

        ### Output

        ```bash
        False
        True
        True
        ```
        """
        if type(a) != int:
            print(type(a))
            raise ValueError("Data type of given value must be int.")
        return a % 2 == 0
    def ceil(self, a: Union[int, float]) -> int:
        """
        - Rounds a number up to its nearest integer.

        ### Example.
        ```python
        import zedmath

        print(zedmath.ceil(3.9))
        print(zedmath.ceil(3.3))
        print(zedmath.ceil(3.0))
        ```

        ### Output.
        ```bash
        4
        4
        3
        ```
        """
        tmp = a - (a//1)
        tmp2 = a - tmp

        if tmp == 0 or tmp == 0.0:
            return int(a)

        return  int(tmp2 + 1)
    def floor(self, a: Union[int, float]) -> int:
        """
        - Returns the value of a rounded down to its nearest integer.

        ### Example.
        ```python
        import zedmath

        print(zedmath.floor(3.9))
        print(zedmath.floor(3.3))
        print(zedmath.floor(3.0))
        ```

        ### Output.
        ```bash
        3
        3
        3
        ```
        """
        tmp = a - (a//1)
        tmp2 = a - tmp

        if tmp == 0 or tmp == 0.0:
            return int(a)

        return  int(tmp2)
    def sign(self, a: Union[int, float]) -> int:
        """
        - if given numbers is positive: returns 1
        - if given numbers is negative: returns -1
        - if given numbers is 0: returns 0

        ### Example.

        ```python
        import zedmath

        print(zedmath.sign(-5.1))
        print(zedmath.sign(5.1))
        print(zedmath.sign(0))
        ```

        ### Output.

        ```bash
        -1
        1
        0
        ```
        """
        if a > 0:
            return 1
        elif a < 0:
            return -1
        return 0
    def min(self, *args : Union[int, float, str, list[Union[int, float, str]]]) ->Union[int, float]:
        def _do(a, old):
            mn = old
            for i in a:
                if type(i) != list:
                    try:
                        i = float(i)
                    except:
                        raise ValueError("Given value must be number.")
                    if i < mn:
                        mn = i
                else:
                    mn = _do(i, mn)
            return mn

        return _do(args, args[0])
    def max(self, *args : Union[int, float, str, list[Union[int, float, str]]]) ->Union[int, float]:
        def _do(a, old):
            mn = old
            for i in a:
                if type(i) != list:
                    try:
                        i = float(i)
                    except:
                        raise ValueError("Given value must be number.")
                    if i > mn:
                        mn = i
                else:
                    mn = _do(i, mn)
            return mn

        return _do(args, args[0])



