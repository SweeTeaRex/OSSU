import random



randomNumber = random.randint(1,10)
correct = False
while not correct:
    
    number = int(input("Guess a number between 1 and 10: "))
    if number<randomNumber:
        print("Too low")
        correct = False
        

    elif number>randomNumber:
        print("Too high")
        correct = False
        
    else:
        correct = True
        print("Correct!")
        
   

    