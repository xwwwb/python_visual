import platform
import threading
from functools import reduce
from operator import add, mul, or_
from random import shuffle

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from rich.console import Console

console = Console()
oldPrint = print

if platform.system() == 'Darwin':
    font = FontProperties(
        fname=r"/System/Library/Fonts/STHeiti Light.ttc", size=14)
else:
    font = FontProperties(fname=r"C:\windows\fonts\msyhl.ttc", size=14)


def MyPrint(*args):
    def func(desc=''):
        if desc == '':
            pass
        else:
            console.print("运行的语句：" + str(*args) + '\n描述：' + desc, style="bold red")
        oldPrint(eval(*args))
        oldPrint()

    return func


print = MyPrint


def ContentOne():
    print("eval('3+4j')")("可以对字符串求值得到复数")
    print("eval('8**2')")("可以求字符串表达式的值")
    print("eval('[1,2,3,4,5]')")("可以求字符串列表的列表")
    print("eval('{1,2,3,4}')")("可以求字符串集合的集合")


def ContentTwo():
    print("[3,22,111]")("data列表")
    print("max([3,22,111])")("求data列表中的最大值")
    print("min([3,22,111])")("求data列表中的最小值")
    print("max([3,22,111],key=str)")("先转换为字符串，再求最大值")
    print("max(['3','22','111'])")("字符串列表求最大值，和上面的结果一样")
    print("max(['3','22','111'],key = len)")("求字符串长度最大的字符串")
    print("['abc','Abcd','ab']")("新的data列表")
    print("max(['abc','Abcd','ab'])")("求data列表中的最大值 依次比较大小")
    print("max(['abc','Abcd','ab'],key = str.lower)")("先转换为小写，再求最大值")
    print("max(['abc','Abcd','ab'],key = len)")("求字符串长度最大的字符串")
    print("[1,1,1,2,2,1,3,1]")("data列表")
    data = [1, 1, 1, 2, 2, 1, 3, 1]
    try:
        print("max(set(data),key = data.count)")("求data列表中出现次数最多的元素")
    except Exception as e:
        pass
    oldPrint(max(set(data), key=data.count))
    try:
        print("max(range(len(data)),key = data.__getitem__)")("求最大元素的索引")
    except Exception as e:
        pass
    oldPrint(max(range(len(data)), key=data.__getitem__))


def ContentThree():
    data = [1, 2, 3, 4]
    oldPrint(len(data))
    oldPrint(sum(data))
    data = (1, 2, 3)
    oldPrint(len(data))
    oldPrint(sum(data))
    data = {1, 2, 3}
    oldPrint(len(data))
    oldPrint(sum(data))
    data = 'Readability counts.'
    oldPrint(len(data))
    data = {97: 'a', 65: 'A', 48: '0'}
    oldPrint(len(data))
    oldPrint(sum(data))


def ContentFour():
    print = oldPrint
    data = list(range(20))
    shuffle(data)
    print(data)
    print(sorted(data))
    print(sorted(data, key=str))
    print(sorted(data, key=str, reverse=True))
    data = list(range(20))
    shuffle(data)
    print(data)
    reversedData = reversed(data)
    print(reversedData)
    print(list(reversedData))
    print(tuple(reversedData))


def ContentFive():
    print = oldPrint
    num = int(input("请输入一个大于2的自然数："))
    if num % 2 == 1:
        print("这是一个奇数")
    else:
        print("这是一个偶数")
    lst = eval(input("请输入一个列表，包含若干大于2的自然数"))
    print("列表中所有元素的和为：", sum(lst))
    print(1, 2, 3, 4, 5)
    print(1, 2, 3, 4, 5, sep=",")
    print(3, 5, 7, end=' ')
    print(9, 11, 13)


def ContentSix():
    print = oldPrint
    range1 = range(10)
    range2 = range(1, 11)
    range3 = range(1, 11, 2)
    range4 = range(20, 0, -2)
    print(range1)
    print(range2)
    print(range3)
    print(range4[2])
    print(list(range1), list(range2), list(range3), list(range4))
    for i in range(10):
        print(i, end=" ")

    data = zip('1234', [1, 2, 3, 4, 5, 6])
    print(data)
    print(list(data))
    data = zip('1234', [1, 2, 3, 4, 5, 6])
    print(tuple(data))
    data = zip('1234', [1, 2, 3, 4, 5, 6])
    for i in data:
        print(i)
    print(map(str, range(10)))
    print(list(map(str, range(10))))
    print(list(map(len, ['abc', '1234', 'test'])))
    for num in map(add, range(5), range(5, 10)):
        print(num)
    seq = range(1, 10)
    print(reduce(add, seq))
    print(reduce(mul, seq))
    seq = [{1}, {2}, {3}, {4}]
    print(reduce(or_, seq))
    seq = ['abcd', '1234', '.,?!', '']
    print(list(filter(str.isdigit, seq)))
    print(list(filter(str.isalpha, seq)))
    print(list(filter(str.isalnum, seq)))
    print(list(filter(None, seq)))


def ContentSeven():
    text = input("请输入一个字符串：")
    oldPrint(reduce(add, reversed(text)))


def ContentEight():
    list = eval(input("请输入一个整数列表："))
    oldPrint("列表中最大的数是：", max(list))


def ContentNine():
    lst = eval(input("请输入一个整数列表："))
    newList = sorted(lst, key=lambda num: num % 2 == 0)
    oldPrint(newList)


def ContentTen():
    month = list(range(1, 13))
    money = [5.2, 2.7, 5.8, 5.7, 7.3, 9.2,
             18.7, 15.6, 20.5, 18.0, 7.8, 6.9]
    # 绘制每个月份的营业额
    for x, y in zip(month, money):
        color = '#%02x' % int(y * 10) + '6666'
        plt.bar(x, y,
                color=color, hatch='*', width=0.6, edgecolor='b', linestyle='--'
                , linewidth=1.5)
        plt.text(x - 0.3, y + 0.2, '%.1f' % y)
    # 设置x、y轴标签和字体
    plt.xlabel('月份', fontproperties=font)
    plt.ylabel('营业额（万元） ', fontproperties=font)
    plt.title('烧烤店营业额', fontproperties=font, fontsize=14)
    # 设置x轴刻度
    plt.xticks(month)
    # 设置y轴跨度
    plt.ylim(0, 22)
    plt.show()


def ContentEleven():
    x = [1, 3, 5]
    y = [3, 8, 9]
    y1 = [2, 6, 3]
    plt.bar(x, y, align="center", color="#66c2a5", tick_label=["A", "B", "C"], label="A")
    plt.bar(x, y1, align="center", color="#8da0cb", tick_label=["A", "B", "C"], label="B")
    plt.legend()
    plt.show()


def ContentTwelve():
    x = np.arange(1, 13)
    y = [5.2, 2.7, 5.8, 5.7, 7.3, 9.2, 18.7, 15.6, 20.5, 18.0, 7.8, 6.9]
    y1 = [3.6, 0.6, 2.1, 3.8, 8.9, 12.8, 26.5, 27.8, 33.9, 26.2, 15.3, 3.7]
    bar_width = 0.4
    tick_label = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
    plt.bar(x, y, align="center", color="#66c2a5", width=bar_width, label="2019", alpha=0.5)
    plt.bar(x + bar_width, y1, align="center", color="#8da0cb", width=bar_width, label="2020", alpha=0.5)
    plt.xticks(x + bar_width / 2, tick_label, fontproperties=font)

    plt.legend()
    plt.show()


def ContentThirteen():
    labels = ["A部门", 'B部门', 'C部门', 'D部门']
    nums = [0.25, 0.15, 0.36, 0.24]
    colors = ["#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]
    explode = (0.1, 0.1, 0.1, 0.1)
    patches, l_text, p_text = plt.pie(nums, explode=explode, labels=labels, colors=colors, autopct="%3.1f%%",
                                      shadow=True, startangle=90)
    plt.title("一季度各部门盈利构成", fontproperties=font)

    for t in l_text:
        t.set_fontproperties(font)

    plt.show()


if __name__ == '__main__':
    funcList = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    job1 = threading.Thread(target=ContentTen)
    job1.start()
    job1.join()
    job2 = threading.Thread(target=ContentEleven)
    job2.start()
    job2.join()
    job3 = threading.Thread(target=ContentTwelve)
    job3.start()
    job3.join()
    job4 = threading.Thread(target=ContentThirteen)
    job4.start()
    job4.join()

    for func in funcList:
        funcName = 'Content' + func
        console.print(f"执行函数：{funcName}", style="bold blue")
        eval(funcName)()
        oldPrint()
