"""Write a Python program to count the number of occurrences of an element in a list."""


a=[10, 20, 30, 10, 10, 20, 40, 50]
dic = {}

for i in a :
       if i not in dic: dic[i] = a.count(i)

for key, val in dic.items():
     print(f"{key} appears {val} times")       