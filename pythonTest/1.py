"""Write a function that takes a list of integers as input and returns the second largest number
in the list."""

def sec_large(a):
    a.sort()
    return a[1]

a = [10, 20, 4, 45, 99]
num=sec_large(a)
print(num)