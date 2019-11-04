def solve(st):
    length = len(st)    
    s = ''.join(sorted(st))    
    for i in range(1, length):   
        if ord(s[i]) - ord(s[i - 1]) != 1:  
            return False
    else:
        return True
