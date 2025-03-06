s = input("Type a word: ")

def char_counts(s):
    vowelSum = 0
    constSum = 0
    for x in range(len(s)):
        if s[x] == "a" or s[x] == "e" or s[x] == "i" or s[x] == "o" or s[x] == "u":
            vowelSum = vowelSum+1
        else:
            constSum = constSum+1
    return(vowelSum, constSum)

print(char_counts(s))