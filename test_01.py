# 1、编写一个函数，调用函数返回四位不含0的随机数作为验证码，
# 要求用while循环拼接(4分)

import random
def number_suiji():
    i=0
    numbers=""
    while i<=3:
        a=str(random.randint(1,9))
        numbers+=a
        i+=1
    return numbers

print(number_suiji())