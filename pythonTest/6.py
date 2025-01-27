"""Write a Python program to flatten a nested list and return the flattened list."""

l1 = [ [1, 2, 3], [4, 5], [6, 7, [8, 9]]]

def flatten(l1):
    flat_list = []
    
    for i in l1:
        if isinstance(i, list):  
            flat_list.extend(flatten(i))  
        else:
            flat_list.append(i) 
    
    return flat_list

flatten = flatten(l1)
print(flatten)