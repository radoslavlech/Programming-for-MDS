# coding: utf8
"""
Write a program that will ask the user for an integer (the size of the triangle)
and then print an isosceles triangle composed of `*` characters of the given
size. E.g:

Enter the size of the triangle: 3
  *
 ***
*****

"""

# your code here
size=int(input("Enter the size of the triangle: "))
stars=""
spaces=size-1
for number in range(0,size):
  for space in range(0,spaces):
    print(end=" ")
  stars=stars+"* "
  spaces=spaces-1
  print(stars)
