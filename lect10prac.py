n = int(input("Type a number: "))

def make_ordered_list(n):
    my_list = []
    for x in range(n):
        my_list.append(x)
        
    return my_list

print(make_ordered_list(n))