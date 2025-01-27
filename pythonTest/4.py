"""Write a program to remove all even numbers from a list and return the remaining list using
list comprehension."""

a=[1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [i for i in a if i % 2 != 0]
print(result)

    