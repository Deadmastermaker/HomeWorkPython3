
my_list = [1, 0, 1]

for i in range(int(input('Число: '))):
    my_list.insert(0, my_list[1] - my_list[0])
    my_list.append(my_list[-2] + my_list[-1])

print(my_list)