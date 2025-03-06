s = input("Type a lowercase word")

def char_counts(s):
    for x in len(s):
        if s[x] == "a" or s[x] == "e" or s[x] == "i" or s[x] == "o" or s[x] == "u":
            vowelSum = vowelSum+1
        else:
            constSum = constSum+1
    
    return(vowelSum, constSum)
