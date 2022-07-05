def function(n=100, k=2):
    k_index = 0
    my_list = [i + 1 for i in range(n)]
    while numbers(my_list) > 1:
        temp = k
        while temp > 0:
            if my_list[k_index] > 0:
                temp -=1
                if temp == 0:
                    break
            k_index = (k_index + 1) % len(my_list)
        my_list[k_index] = -my_list[k_index]
    for i in  my_list:
        if i > 0:
            return i
def numbers(l):
    counter = 0
    for i in l:
        if i > 0:
            counter +=1
    return counter

x = int(input())
for i in range(x):
    inp = input()
    if inp == '*':
        print(function())
    else:
        if inp == 'n':
            n = int(input())
            inp = input()
            if inp == 'k':
                k = int(input())
                print(function(n=n, k=k))
                inp = input()
            elif inp == '*':
                print(function(n=n))
        elif inp == 'k':
            k = int(input())
            print(function(k=k))
            inp = input()