# -*- coding: utf-8 -*-
"""
The program should print two roots of the quadratic equation of the form

a x² + b x + c = 0

The roots must be stored in a tuple named xx and printed at the very end of the program.
"""

# This is sample input data

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# This is a tuple for results. You should override it with actual results

solution = ()

# DO NOT CHANGE ANYTHING ABOVE THIS LINE!!!


# Put your here...
delta=b**2-4*a*c
if a==0:
    solution=-c/b
elif delta<0:
    solution=('no real roots')
elif delta==0:
    solution=-b/(2*a),
else:
    solution=(-b-delta**0.5)/(2*a),(-b+delta**0.5)/(2*a)


# At the end the results are printed to the screen
print(*solution)
