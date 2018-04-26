"""
3、输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数，并判断他的指数处于什么级别。（10分）
例如：一個52公斤的人，身高是1.55m，则BMI为 :
52/(1.55**2) = 21.6
BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
"""

#先设定一个函数，设置两个形参,最终返回BMI指数
def BMI(height,weight):

    BMI_num=weight/(height**2)
    print("BMI指数是%.1f"%BMI_num)
    return BMI_num


#调用函数,用户输入并进行判断输出
height=float(input("请输入身高:"))
weight=float(input("请输入体重:"))
num=BMI(height,weight)
if num<18.5:
    print("过轻")
elif 18.5<=num<25:
    print("正常")
elif 25<=num<28:
    print("过重")
elif 28<=num<32:
    print("肥胖")
else:
    print("严重肥胖")
