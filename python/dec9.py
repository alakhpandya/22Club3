"""
Operators:
1. Arithmetic Operators: +, -, *, /, %, **, //
2. Comparision/Relational/Conditional Operators/Conditions:
    <, >, <=, >=, ==, !=
    These operators will always return True or False.
    For Python, False means: 0, null string, [], (), set(), {}
    True means anything which is not listed above.
3. Logical Operators: and, or, not
4. Bitwise Operators: &, |, ~, ^, <<, >>

    Either email or mobile
    Degree | experience
    
    Exclusive OR: Tea ^ Coffee

    5:  0 1 0 1
        & & & &
    3:  0 0 1 1
        -------
        0 0 0 1: 1

    5:  0 1 0 1
        | | | |
    3:  0 0 1 1
        -------
        0 1 1 1: 7

    79 : 0 0 0 0  0 1 0 0  1 1 1 1 = 79
    << : 0 0 0 0  1 0 0 1  1 1 1 0 = 158
    << : 0 0 0 1  0 0 1 1  1 1 0 0 = 316
    << : 0 0 1 0  0 1 1 1  1 0 0 0 = 632

5. Assignment Operators

    a = 5
     <--
    5 + 10 = a      Invalid for computers
    a = 5 + 10

    shorthand operators:
    a = a + b   :   a += b
    a = a - b   :   a -= b
    a = a * b   :   a *= b
    a = a / b   :   a /= b
    a = a % b   :   a %= b
    a = a ** b   :   a **= b
    a = a // b   :   a //= b
    a = a & b   :   a &= b
    a = a | b   :   a |= b
    a = a ^ b   :   a ^= b
    a = a << b   :   a <<= b
    a = a >> b   :   a >>= b


    a = a + 1 : a += 1  (There's no such thing as a++ or a-- in Python)

6. Identity Operators:
    is, is not

7. Membership Operators:
    in, not in

"""

"""
print(5 ** 3)
print(11//4)
print(5 < 3)
print(5 > 3)

a = float(input("Enter three numbers:\n"))
b = float(input())
c = float(input())
d = float(input())
# print(a > b and a > c and a > d)

# print(c > a or c > b or c > d)

not a > b
"""

# print(5 & 3)
# print(5 | 3)
# print(79 << 3)

"""
a = 15
b = 15
print(a is b)
print(a == b)
"""
"""
a = [34, 75, 9, -33, 22.5]
b = a
c = a.copy()
# a.append(900)
# print("a =", a)
# print("b =", b)
# print("c =", c)

print(a is b)
print(a == b)

print(a == c)
print(a is c)
"""
print("khush" in "khush khushal")
print("R" not in "Royal")