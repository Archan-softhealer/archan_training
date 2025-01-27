"""You have a dictionary where the values are lists. Find the most frequent element across all
lists."""


from collections import Counter
 
d={'a': [1,2, 3], 'b': [2,3,4], 'c': [2,3,4]}
l1=[]
for key,val in d.items():
    l1.append(val)

def flatten(l1):
    flat_list = []
    
    for i in l1:
        if isinstance(i, list):  
            flat_list.extend(flatten(i))  
        else:
            flat_list.append(i) 
    
    return flat_list
  
l2= flatten(l1)

most_repetitive = max(Counter(l2), key=Counter(l2).get)
print(most_repetitive)    

