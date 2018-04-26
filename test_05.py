# 5、使用for循环，完成以下图形的输出，并封装成函数有一个参数为打印的行数。（10分）
#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
#  * * * * * *

def xiaoxingxing(row):
    # row = int(input("请输入一个数:"))
    for i in range(1, row):
        j = 1
        while j <= i:
            if j == 1:
                print(" " * (row - i), end="")
            print("* ", end="")
            j += 1
        print("")

row=int(input("请输入要打印的行数："))
xiaoxingxing(row)