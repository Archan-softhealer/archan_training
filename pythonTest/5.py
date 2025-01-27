"""Write a Python function to rotate a list n positions to the right."""

l1=[1, 2, 3, 4, 5, 6]
n = 3

l1 = l1[n:] + l1[:n]
print(l1)