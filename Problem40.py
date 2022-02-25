"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
string = ""
for i in range(1,1000000):
    string += str(i)
integer = 1
print(string[0:100])
for i in range(6):
    print(string[(10 ** i) - 1])
    integer *= int(string[(10 ** i) - 1])
print(integer)
