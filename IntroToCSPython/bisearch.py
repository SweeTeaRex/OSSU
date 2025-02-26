cube = int(input("Type an integer to get the cube root: "))
epsilon = 0.1
low = 0
high = cube
guess = (high+low)/2
numberOfGuess = 0

while abs(guess**3-cube >= epsilon):
    if guess**3 > cube:
        
        high = guess
        numberOfGuess = numberOfGuess+1
    else:
        low = guess
        numberOfGuess = numberOfGuess+1
    guess = (high+low)/2

print(guess)
print(numberOfGuess)


