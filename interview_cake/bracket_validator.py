def bracket_validator(s):
    ref, stack = {'[': ']', '{': '}', '(': ')'}, []
    
    for char in s: 
        if char in ref: stack.append(ref[char])
        else: 
            if len(stack) == 0 or char != stack.pop(): return False
    
    return len(stack) == 0

print bracket_validator("{[]()}")
print bracket_validator("{[(])}")
print bracket_validator("{[}")