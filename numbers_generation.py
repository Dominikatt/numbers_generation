import time

time_stamp = time.time()

def somename():
    number = int(time_stamp % 10)
    if number == 0:
        number += 10
    return (number)

print(somename())


# TODO использовать для генерации не секунды, a милисекунды\нано\etc
# TODO расширить генерацию до диапазона 1 - 1000
# TODO создать новый проект, и написать там функцию которая будет считать количество элементов в списке (список создаешь сама)
# список содать не в функции, но передавать в нее в качестве аргумента (в гугле так и пишешь "аргумент для функции")
#