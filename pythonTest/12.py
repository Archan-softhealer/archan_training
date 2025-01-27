"""Have the function bracketMatcher(str) take the str parameter being passed and
return 1 if the brackets are correctly matched and each one is accounted for. Otherwise,
return 0. Only ( and ) will be used as brackets. If str contains no brackets, return 1."""

def bracketMatcher(s):
    count = 0
    
    for char in s:
        if char == '(':
            count += 1  
        elif char == ')':
            count -= 1  
            
            if count < 0:  
                return 0
    
    return 1 if count == 0 else 0

print(bracketMatcher("(hello)(world)"))