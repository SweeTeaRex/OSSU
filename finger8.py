def same_char(s1, s2):
    
    for char in s1:
        if char in s2:
            return True
            
    return False
    

    




print(same_char("abc", "cab"))
print(same_char("abccc", "caaab"))
print(same_char("abcd", "cabaa"))
print(same_char("abcabc", "cabz"))