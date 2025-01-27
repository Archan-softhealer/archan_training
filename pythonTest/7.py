"""Given a dictionary, write a program to invert it. The keys become values, and the values
become keys."""

d = {'a': 1, 'b': 2, 'c': 3}

d={value: key for key, value in d.items()}
    
print(d)   