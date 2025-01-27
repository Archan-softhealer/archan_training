"""Have the function WordSplit(strArr) read the array of strings stored in strArr, which
will contain 2 elements: the first element will be a sequence of characters, and the second
element will be a long string of comma-separated words in alphabetical order, that
represents a dictionary.
Your goal is to determine if the first element in the input can be split into two words, where
both words exist in the dictionary provided in the second input."""


def WordSplit(strArr):
    str = strArr[0]
    lst = list(strArr[1].split(','))
    ol = []
    for i in range(1,len(str)):
        s1 = str[:i]
        s2 = str[i:]
        if s1 in lst and s2 in lst:
            ol.append(s1)
            ol.append(s2)
    if not ol:
        print("not possible")
    else:
        print(ol)   
    
inp = ["applegoodbye", "apple,bat,cat,goodbye,hello,yellow,why"]
WordSplit(inp)