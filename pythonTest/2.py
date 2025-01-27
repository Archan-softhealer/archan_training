"""Write a function that takes a list of tuples (each tuple contains a name and age) and returns
a list of names of people aged 30 and above"""

def people_sort(people):
    people_30_above = []
    for i , j in people:
        if j>=30 : people_30_above.append(i)
        
    return people_30_above          



people =  [("Alice", 25), ("Bob", 35), ("Charlie", 30)]
people_30_above= people_sort(people)
print(people_30_above)
