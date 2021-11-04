# coding: utf8
"""
Write a program that prompts the user to enter a password, and then prints
exactly one of the following messages: ‘The password is secure.’ or
‘The password is insecure!’. A secure password must meet the following
conditions:

* have at least one lowercase letter,
* have at least one capital letter,
* have at least one digit.

Examples:

Enter the password: Katar7yna
The password is secure.
Enter the password: catastrophe01
The password is insecure!

"""

# your code here
password=input("Enter your password: ")
sum_capitals=0
sum_lower_case=0
sum_numbers=0
for character in password:
    if 'A' <= character<='Z':
        sum_capitals+=1
    elif 'a' <= character<='z':
        sum_lower_case+=1
    elif '0' <= character<='9':
        sum_numbers+=1
if sum_capitals==0 or sum_lower_case==0 or sum_numbers==0:
    print("The password is insecure!")
else:
    print("The password is secure.")