import time

time_stamp = time.time()

def number_generation():
    number = int((time_stamp % 1000 - int(time_stamp % 1000)) * 100000000)
    if number == 0:
        number += 1000

    res = [int(x) for x in str(number)]
    print(res)
    for i in range(0, len(res), 2):
        res[i], res[i+1] = res[i+1], res[i]

    return int(''.join(map(str, res)))

print(number_generation())

alphabets_in_lowercase = []
def add_letters():
    for i in range(97, 107):
        alphabets_in_lowercase.append(chr(i))
    # print(alphabets_in_lowercase)
    number = int(time_stamp % 100000)
    if number == 0:
        number += 100000
    number_list = [int(x) for x in str(number)]
    result = list()
    for i in range(len(number_list)):
        result.append(alphabets_in_lowercase[number_list[i]])
    return result

print(''.join(map(str, add_letters())))

def examole_1(numeric_from_example_2):
    return 7-numeric_from_example_2

def example_2(numeric):
    return 43 - examole_1(numeric)

print(example_2(2))


# TODO превратить строки 6,7,8 и 24,25,26 в отдельную функцию. и вызывать ее внутри number_generation и add_letters.
#  Длина ряда должна регулироваться передаваемым аргументом (см example)





