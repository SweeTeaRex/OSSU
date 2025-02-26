n = int(input("Type an integer: "))
cube = False

for x in range(n):
    num = x**3
    if num == n:
        
        cube = True
        break
    else:
        cube = False
    
if cube is True:
    print("Cube root: ", x)
if cube is False:
    print("error")
