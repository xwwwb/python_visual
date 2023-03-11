from functools import reduce
import time

def add5(num):
    return num + 5

def ContentOne():
    print("实验内容1：输入姓和名，通过屏幕向大家打招呼")
    lastName = input("姓：")
    firstName = input("名：")
    print("使用字符串的拼接：")
    print("Hello Everyone,My name is " + lastName + " " + firstName + ".")
    print("使用python3.7新特征模板字符串")
    print(f"Hello Everyone,My name is {lastName} {firstName}.")
    print()

def ContentTwo():
    print("实验内容2：列表所有数字加五，得到新列表")
    x = list(range(10))
    y = []
    print("被加列表：" + str(x) + " 空列表" + str(y))
    print("使用列表的遍历")
    for num in x:
        y.append(num + 5)
    print("结果：" + str(y))
    print("使用python的生成器语法")
    print([num + 5 for num in x])
    print("使用map方法和普通函数")
    print(list(map(add5, x)))
    print("使用map方法和lambda表达式 省略单独定义函数的步骤")
    print(list(map(lambda num: num + 5, x)))
    print()
def ContentThree():
    print("实验内容3：计算1-100整数和")
    print("使用遍历加和")
    sum = 0
    t1 = time.time()
    for i in range(100000000):
        i = i + 1
        sum += i
    t2 = time.time()
    print("结果：" + str(sum))
    print("使用高阶函数reduce")
    t3 = time.time()
    sum = reduce(lambda x, y: x + y, [num + 1 for num in range(100000000)])
    t4 = time.time()
    print("结果：" + str(sum))
    print("使用数学公式")
    t5 = time.time()
    sum = ((1 + 100000000) * 100000000) / 2
    t6 = time.time()
    print("结果：" + str(int(sum)))
    print("其中列表遍历加和的运行时间差是：" + str((t2 - t1) * 1000) +
          " reduce计算时间差：" + str((t4 - t3) * 1000) +
          " 公式计算时间差是：" + str((t6 - t5) * 1000))
if __name__ == '__main__':
    # ContentOne()
    # ContentTwo()
    ContentThree()
