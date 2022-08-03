import time

time_stamp = time.time()
number = int((time_stamp % 1000 - int(time_stamp % 1000)) * 10000000000)
def number_generation():
    number = int((time_stamp % 1000 - int(time_stamp % 1000)) * 10000000000)
    if number == 0:
        number += 1000
    return(number)

res = [int(x) for x in str(number)]
list_n = str(res)

print(list_n)


for i in range(0, (len(list_n)-1), 2):
    int(number[i]), int(number[i+1]) = int(number[i+1]), int(number[i])


print(list_n)
print(number_generation())

# list = [1, 2, 3, 4]
#
# def somefunction(qweqwe):
#     return(len(qweqwe))
#
# print(somefunction(list))


# TODO создать новый проект, и написать там функцию которая будет считать количество элементов в списке (список создаешь сама)
# список содать не в функции, но передавать в нее в качестве аргумента (в гугле так и пишешь "аргумент для функции")
#