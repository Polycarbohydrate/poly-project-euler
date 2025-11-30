# https://projecteuler.net/problem=66
import time
import math
from decimal import Decimal, getcontext
start_time = time.time()
getcontext().prec = 100
biggest_x = 1
new_d = 1
for d in range(0, 1001):
    if math.sqrt(d).is_integer():
        continue
    d = Decimal(d)
    items = []
    items.append(int(d.sqrt()))
    temp = Decimal(1) / ((d.sqrt()) - (int(d.sqrt())))
    items.append(int(temp))
    while int(temp) != (items[0] * 2):
        temp = Decimal(1.0) / Decimal(temp - items[(len(items) - 1)])
        items.append(int(temp))
    original_period_len = len(items) - 1
    if original_period_len % 2 == 0:
        integer = items[0]
        del items[0]
        del items[original_period_len - 1]
        new_len = len(items)
        if new_len >= 2:
            lower = items[new_len - 1]
            upper = items[new_len - 2]
            top = 1
            for i in reversed(range(0, new_len - 2)):
                temp_0_top = lower * upper + top
                top = lower
                lower = temp_0_top
                upper = items[i]
            temp_0 = lower * upper + top
            top = lower
            lower = temp_0
            final_top = integer * lower + top
            if final_top > biggest_x:
                biggest_x = final_top
                new_d = d
    else:
        integer = items[0]
        del items[0]
        cloned_items = items.copy()
        items.extend(cloned_items)
        length_0 = len(items)
        del items[length_0 - 1]
        new_len = len(items)
        if new_len >= 2:
            lower = items[new_len - 1]
            upper = items[new_len - 2]
            top = 1
            for i in reversed(range(new_len - 2)):
                temp_0_top = lower * upper + top
                top = lower
                lower = temp_0_top
                upper = items[i]
            temp_0 = lower * upper + top
            top = lower
            lower = temp_0
            final_top = integer * lower + top
            if final_top > biggest_x:
                biggest_x = final_top
                new_d = d
print(new_d)
print("============================")
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)