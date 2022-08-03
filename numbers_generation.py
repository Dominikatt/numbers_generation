import time

time_stamp = time.time()

def number_generation():
    number = int((time_stamp % 1000 - int(time_stamp % 1000)) * 10000000000)
    if number == 0:
        number += 1000

    res = [int(x) for x in str(number)]

    for i in range(0, len(res), 2):
        res[i], res[i+1] = res[i+1], res[i]

    return int(''.join(map(str, res)))

print(number_generation())