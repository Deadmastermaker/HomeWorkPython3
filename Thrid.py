import random

my_list = []

for _ in range(5):
    index = random.randint(0, 2)
    my_list.append(round(random.uniform(0, 5), index))
print(my_list)


for i in range(len(my_list)):
        if my_list[i] % 100 > my_list[-i] % 100:
            digit1 = my_list[i] % 100
            suma = digit1 - digit2
            if my_list[i] % 100 < my_list[-i] % 100:
                digit2 = my_list[-i] % 100
                print(suma)




