import math

from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties


def ContentOne():
    print("计算32的阶乘")
    print(math.factorial(32))
    print("浮点型比较大小可能会有精度问题")
    print(0.4 - 0.3 == 0.1)
    print("使用isclose函数进行浮点型比较")
    print(math.isclose(0.4 - 0.3, 0.1))
    num = 7
    squreRoot = num ** 0.5

    print("7先开平方在平方是否等于7")
    print(squreRoot ** 2 == num)
    print("使用isclose函数进行浮点型比较")
    print(math.isclose(squreRoot ** 2, num))

def cni(n,i):
    minNI = min(i,n-i)
    result = i
    for j in range(0,minNI):
        result = result * (n-j)/(minNI-j)
    return result

def ContentTwo():
    print(cni(5,2))


def ContentThree():
    text = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.'''
    print("计算text的长度")
    print(len(text))
    print("计算text中is的个数")
    print(text.count("is"))
    print("测试字符串中是否包含beautiful")
    print("beautiful" in text)
    print("打印20个=")
    print("=" * 20)
    print("字符串连接")
    print("Good " + "Morning")


def ContentFour():
    print("计算7.9-4.5")
    print(7.9 - 4.5)
    print("计算5-3")
    print(5 - 3)
    num = 3
    print("num取反")
    print(-num)
    print("num两次取反")
    print(--num)
    print("使用括号限制优先级")
    print(-(-num))
    print("计算集合{1,2,3}和{3,4,5}的差集")
    print({1, 2, 3} - {3, 4, 5})
    print("计算集合{3,4,5}和{1,2,3}的差集")
    print({3, 4, 5} - {1, 2, 3})


def ContentFive():
    print("计算数字33333和数字55555的乘法")
    print(33333 * 55555)
    print("计算复数3+4j和复数5+6j的乘法")
    print((3 + 4j) * (5 + 6j))
    print("打印三次\"重要的事情说三遍！\"")
    print("重要的事情说三遍！" * 3)
    print("[0]*5")
    print([0] * 5)
    print("(0,)*3")
    print((0,) * 3)


def ContentSix():
    print("2**4")
    print(2 ** 4)
    print("3 ** 3 ** 3")
    print(3 ** 3 ** 3)
    print("3 ** (3 ** 3)")
    print(3 ** (3 ** 3))
    print("(3 ** 3) ** 3")
    print((3 ** 3) ** 3)
    print("9 ** 0.5")
    print(9 ** 0.5)
    print("(-1) ** 0.5")
    print((-1) ** 0.5)


def ContentSeven():
    print(17 / 4)
    print(17 // 4)
    print((-17) / 4)
    print((-17) // 4)


def ContentEight():
    print(3 + 2 < 7 + 8)
    print(3 < 5 > 2)
    print(3 == 3 < 5)
    print('12345' > '23456')
    print('abcd' > 'Abcd')
    print([85, 92, 73, 84] < [91, 82, 73])
    print([180, 90, 101] > [180, 90, 99])
    print({1, 2, 3, 4} > {3, 4, 5})
    print({1, 2, 3, 4} <= {3, 4, 5})
    print([1, 2, 3, 4] > [1, 2, 3])


def ContentNine():
    print(60 in [70, 60, 50, 80])
    print('abc' in 'a1b2cdfg')
    print([3] in [[3], [4], [5]])
    print('3' in map(str, range(5)))
    print(5 in range(5))


def ContentTen():
    print(int(3.5))
    print(int('119'))
    print(int('1111', 2))
    print(int('1111', 8))
    print(int('1111', 16))
    print(int('  9\n'))
    print(float('3.1415926'))
    print(float('-inf'))
    print(complex(3, 4))
    print(complex(6j))
    print(complex('3'))


def ContentEleven():
    print(bin(8888))
    print(oct(8888))
    print(hex(8888))
    print(ord('a'))
    print(ord('董'))
    print(chr(65))
    print(chr(33891))
    print(str([1, 2, 3, 4]))
    print(str({1, 2, 3, 4}))


def ContentTwelve():
    print(list(), tuple(), dict(), set())
    s = {3, 2, 1, 4}
    print(list(s), tuple(s))
    lst = [1, 1, 2, 2, 3, 4]
    print(tuple(lst), set(lst))
    print(list(str(lst)))
    print(dict(name="Dong", sex="Male", age=41))


def ContentThirteen():
    font = FontProperties(fname=r"/System/Library/Fonts/STHeiti Light.ttc", size=14)
    month = list(range(1, 13))
    money = [5.2, 2.7, 5.8, 5.7, 7.3, 9.2, 18.7, 15.6, 20.5, 18.0, 7.8, 6.9]
    for x, y in zip(month, money):
        color = '#%02x' % int(y * 10) + '6666'
        plt.bar(x, y, color=color, hatch="*", width=0.6,
                edgecolor='b', linestyle='--', linewidth=1.5)
        plt.text(x - 0.3, y + 0.2, '%.lf' % y)

    plt.xlabel("月份", fontproperties=font)
    plt.ylabel('营业额（万元）', fontproperties=font)
    plt.title('烧烤店营业额', fontsize=14, fontproperties=font)

    plt.xticks(month)
    plt.ylim(0, 22)
    plt.show()


if __name__ == '__main__':
    funcList = ['One', 'Two', 'Three', 'Four', 'Five',
                'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                'Eleven', 'Twelve', 'Thirteen']
    for func in funcList:
        funcName = 'Content' + func
        print('执行函数：' + funcName)
        eval(funcName)()
        print()
