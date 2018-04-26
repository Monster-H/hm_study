"""
4、题目：一球从 100米高度自由落下，
每次落地后反跳回原高度的一半；再落下，求它在第 10 次落地时，
共经过多少米？第 10 次反弹多高？（10分）
"""
"""
100-----50
50------25
25------12.5

"""
i=1
height=100
sum_height=100
while i<=10:
    height=(height/2)
    # print("第%d 次弹跳起来的高度%f"%(i,height))
    sum_height+=height
    # print(sum_height)
    i+=1
print("第%d 次反弹起来的高度%f 米"%(i-1,height))
print("第%d 次落地时，共经过%f 米"%(i-1,sum_height))
