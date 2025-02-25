cube = int(input("Type a number to find cube root of: "))
epsilon = 0.1
low = 0
high = cube
guess = (high+low)/2

while abs(guess**3-cube>=epsilon):
    if guess**3 > cube:
        high = guess
    else:
        low = guess
    guess = (high+low)/2

print(guess)
    