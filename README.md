# 🚀 Zedmath _v2.0.0_
___Zedmath__ is very simple library for __math__ operations. Zedmath is open source project._

## Installition

### __Using pip__
```bash
python3 -m pip install zedmath
```
### __Clone source code__
```bash
git clone https://github.com/azizbekQozoqov/
MATH.git
```

## USAGE

| Method names  | Description                   | Arguments                         |
| --------------| ------------------------------| ----------------------------------|
| pow           | Returns the power of a number | __x__ - Required - float or integer|
| abs           | Returns the absolute value of the argument | __a__ - Required - float or integer|
| round         | Round a number to a given precision in decimal digits. | __a__ - Required - float or integer |
| sum           | Returns sum of the given numbers. | __args__ - Required - integer, float, string, list[integer, float, string] |
| is_odd        | Returns given numbers is odd or non odd | __a__ - Required - integer |
| is_even       | Returns given numbers is even or non even | __a__ - Required - integer |
| ceil          | Rounds a number up to its nearest integer | __a__ - Required - integer, float |
| floor         | Returns the value of a rounded down to its nearest integer | __a__ - Required - integer, float |
| sign          | Returns given number is positive or negative using 1,-1,0 | __a__ - Required - integer, float |
| min           | Returns minimum number | __a__ - Required - integer, float, string, list[integer, float, string] |
| max           | Returns maximum number | __a__ - Required - integer, float, string, list[integer, float, string] |
| babylonian | <code> none </code> | __S__ - Required - integer, float |
| digits | Returns all digits of given number | __n__ - Required - integer, float |



### EXAMPLES

<code>zedmath.pow(x)</code> - Returns the power of a number

<!--  -->
__code :__
```python
# Import zedmath library
import zedmath as zm

# Create variable called "result" and assign it the result of zd.pow method
result = zm.pow(4, 4)

# Print the result variable
print(result)
```
__output :__
```bash
256
```
<!--  -->

<code>zedmath.abs(a)</code> - Returns the absolute value of the argument

<!--  -->
__code :__
```python
# Import zedmath library
import zedmath as zm

# Create variable called "result" and assign it the result of zd.abs method
result = zm.abs(-16)

# Print the result variable
print(result)
```
__output :__
```bash
16
```
<!--  -->

<code>zedmath.round(a)</code> - Rounds a number to a given precision in decimal digits.

<!--  -->
__code :__
```python
# Import zedmath library
import zedmath as zm

# Create variables called "result", "result2"  and assign its the result of zd.round method
result = zm.round(31.2)
result2 = zm.round(31.6)

# Print variables
print(result)
print(result2)
```
__output :__
```bash
31
32
```
<!--  -->

<code>zedmath.sum(*args)</code> - Returns sum of the given numbers.

<!--  -->
__code :__
```python
# Import zedmath library
import zedmath as zm

# Create variable called "result" and assign it the result of zd.sum method
numbers = [1, 3, 25, 32.5, [21.6, "66.6", ["4", "6"]]]
result = zm.sum(numbers)

# Print the result variables
print(result)
```
__output :__
```bash
159.7
```
<!--  -->

<code>zedmath.is_odd(a)</code> - Returns given numbers is odd or non odd.

<!--  -->
__code :__
```python
# Import zedmath library
import zedmath as zm

# Create variables called "result", "result2"  and assign its the result of zd.is_odd method
result = zm.is_odd(17)
result2 = zm.is_odd(16)

# Print the result variables
print(result)
print(result2)
```
__output :__
```bash
True
False
```
<!--  -->

<code>zedmath.is_even(a)</code> - Returns given numbers is even or non even.

<!--  -->
__code :__
```python
# Import zedmath library
import zedmath as zm

# Create variables called "result", "result2"  and assign its the result of zd.is_even method
result = zm.is_even(17)
result2 = zm.is_even(16)

# Print the result variables
print(result)
print(result2)
```
__output :__
```bash
False
True
```
<!--  -->

<code>zedmath.ceil(a)</code> - Rounds a number up to its nearest integer.

<!--  -->
__code :__
```python
# Import zedmath library
import zedmath as zm

# Create variables called "result", "result2"  and assign its the result of zd.ceil method
result = zm.ceil(11.7)
result2 = zm.ceil(11.3)

# Print the result variables
print(result)
print(result2)
```
__output :__
```bash
11
11
```
<!--  -->

<code>zedmath.floor(a)</code> - Returns the value of a rounded down to its nearest integer.

<!--  -->
__code :__
```python
# Import zedmath library
import zedmath as zm

# Create variables called "result", "result2"  and assign its the result of zd.floor method
result = zm.floor(11.7)
result2 = zm.floor(11.3)

# Print the result variables
print(result)
print(result2)
```
__output :__
```bash
11
11
```
<!--  -->

<code>zedmath.sign(a)</code> - Returns given number is positive or negative using 1,-1,0.

<!--  -->
__code :__
```python
# Import zedmath library
import zedmath as zm

# Create variables called "result", "result2", "result3" and assign its the result of zd.sign method
result = zm.sign(17)
result2 = zm.sign(-17)
result3 = zm.sign(0)

# Print the result variables
print(result)
print(result2)
print(result3)
```
__output :__
```bash
1
-1
0
```
<!--  -->

<code>zedmath.ceil(a)</code> - Rounds a number up to its nearest integer.

<!--  -->
__code :__
```python
# Import zedmath library
import zedmath as zm

# Create variables called "result", "result2"  and assign its the result of zd.ceil method
result = zm.ceil(11.7)
result2 = zm.ceil(11.3)

# Print the result variables
print(result)
print(result2)
```
__output :__
```bash
11
11
```
<!--  -->

<code>zedmath.floor(a)</code> - Returns the value of a rounded down to its nearest integer.

<!--  -->
__code :__
```python
# Import zedmath library
import zedmath as zm

# Create variables called "result", "result2"  and assign its the result of zd.floor method
result = zm.floor(11.7)
result2 = zm.floor(11.3)

# Print the result variables
print(result)
print(result2)
```
__output :__
```bash
11
11
```
<!--  -->

<code>zedmath.min(*args)</code> - Returns minimum number.

<!--  -->
__code :__
```python
# Import zedmath library
import zedmath as zm

# Create variables called "result" and assign its the result of zd.min method

numbers = [1, 3, 25, 32.5, [21.6, "66.6", ["4", "6"]]]

result = zm.min(numbers)

# Print the result variable
print(result)
```
__output :__
```bash
1.0
```
<!--  -->

<code>zedmath.max(*args)</code> - Returns maximum number.

<!--  -->
__code :__
```python
# Import zedmath library
import zedmath as zm

# Create variables called "result" and assign its the result of zd.max method

numbers = [1, 3, 25, 32.5, [21.6, "66.6", ["4", "6"]]]

result = zm.max(numbers)

# Print the result variable
print(result)
```
__output :__
```bash
66.66
```
<!--  -->

<code>zedmath.digits(n)</code> - Returns all digits of given number.

<!--  -->
__code :__
```python
# Import zedmath library
import zedmath as zm

# Create variables called "result" and assign its the result of zd.digits method

numbers = 178

result = zm.digits(numbers)

# Print the result variable
print(result)
```
__output :__
```bash
(1, 7, 8)
```
<!--  -->

### [Author - Azizbek Qozoqov](https://www.azizbekdev.com)
## Social networks
<a href="https://github.com/azizbekQozoqov"><img src="https://img.shields.io/badge/github-000?style=for-the-badge&logo=github&logoColor=white"/></a>
<a href="https://gitlab.com/azizbekQozoqov/"><img src="https://img.shields.io/badge/gitlab-FF6600?style=for-the-badge&logo=gitlab&logoColor=white"/></a></a>
<a href="https://instagram.com/azizbekdeveloper"><img src="https://img.shields.io/badge/instagram-D1001F?style=for-the-badge&logo=instagram&logoColor=white"/></a>
<a href="https://t.me/azizbekdeveloper"><img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/></a>
<a href="https://www.codewars.com/users/azizbekQozoqov/"><img src="https://img.shields.io/badge/codewars-DD915F?style=for-the-badge&logo=codewars&logoColor=white"/></a>
<a href="https://www.sololearn.com/profile/20988344"><img src="https://img.shields.io/badge/sololearn-10397c?style=for-the-badge&logo=sololearn&logoColor=white"/></a>