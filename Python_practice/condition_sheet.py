# This Sheet Contains "CONDITIONAL QUESTIONS"

# 1.Write a program to check whether a number is Armstrong or not.
"""

Check if a string is a valid palindrome ignoring spaces, symbols, and case.

Given three numbers, determine if they can form a right-angled triangle.

Check if a string is isogram (no repeating letters).

Given two times (HH:MM), check which one is greater.

Validate a password based on multiple conditions (length, digit, symbol, uppercase).

Check if a number is a Harshad (Niven) number.

Write a program to determine if a substring exists without using in."""
"""n = int(input("Enter a number : "))
temp = n
dig = len(str(n))
cub = 0
while temp > 0:
    rem = temp % 10
    cub = rem**dig + cub
    temp = temp//10

if cub == n:
    print("Armstrong")
else:
    print("not Armstrong")"""

#====================================================================================================================#

# 2.Check if a string is a valid palindrome ignoring spaces, symbols, and case.
s = input("Enter a word : ")
l=[]
for i in s:
    l.append(i)

r = l[::-1]
if l == r:
    print('palindrome')
else:
    print('not palindrome')