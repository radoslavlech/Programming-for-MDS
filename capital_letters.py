# coding: utf8
"""
Write a program that prompts user to enter some text and prints the number
of CAPITAL LETTERS on the screen. E.g:

Enter text: Data Science is SUPER!
7

"""

# your code here
text=input("Add your text here: ")
sum=0
for character in text:
    if character 'A' <= character<='Z':
        sum+=1
print("number of capital letters: "+str(sum))        

    