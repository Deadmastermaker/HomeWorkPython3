

my_list = [2, 3, 5, 9, 5]
sum = 0
for i in my_list:
    if my_list.index(i)% 2 > 0:
        sum += i
        print(sum)



