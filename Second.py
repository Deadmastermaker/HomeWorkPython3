
my_list = [2, 3, 4, 5, 6]
sum = 0

for i in range(len(my_list)):
    sum = my_list[i] * my_list[-i - 1]
    print(sum)
    if my_list[i] == my_list[-i - 1]:
        my_list[i] * my_list[i]
        break









