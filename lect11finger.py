def remove_and_sort(Lin, k):
    
    newLin = [index for index in Lin if index != k]
    newLin.sort()
    return newLin
        
L = [1, 6, 3]
k = 1

L = remove_and_sort(L, k)
print(L)
