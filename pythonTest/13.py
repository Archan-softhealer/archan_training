"""Given a string, your task is to reverse only the vowels in the string."""

def reverseVowels(s):
    vowels = "aeiouAEIOU"
    
    vowel_list = [char for char in s if char in vowels]
    
    
    result = []
    for char in s:
        if char in vowels:
            result.append(vowel_list.pop())  
        else:
            result.append(char)
    
    return ''.join(result)
print(reverseVowels("hello"))
print(reverseVowels("hello world"))