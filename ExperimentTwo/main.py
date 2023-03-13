import math
import platform

from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from rich.console import Console

console = Console()

oldPrint = print


def MyPrint(*args):
    def func(desc=''):
        console.print(desc, style="bold red")
        oldPrint(*args)

    return func


print = MyPrint


def ContentOne():
    print(math.factorial(32))("计算32的阶乘")
    print(0.4 - 0.3 == 0.1)("浮点型比较大小可能会有精度问题")
    print(math.isclose(0.4 - 0.3, 0.1))("使用isclose函数进行浮点型比较")
    num = 7
    squreRoot = num ** 0.5
    print(squreRoot ** 2 == num)("7先开平方在平方是否等于7")
    print(math.isclose(squreRoot ** 2, num))("使用isclose函数进行浮点型比较")


def cni(n, i):
    minNI = min(i, n - i)
    result = i
    for j in range(0, minNI):
        result = result * (n - j) / (minNI - j)
    return result


def ContentTwo():
    print(cni(5, 2))


def ContentThree():
    text = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.'''

    print(len(text))("计算text的长度")

    print(text.count("is"))("计算text中is的个数")

    print("beautiful" in text)("测试字符串中是否包含beautiful")

    print("=" * 20)("打印20个=")

    print("Good " + "Morning")("字符串连接")


def ContentFour():
    print(7.9 - 4.5)("计算7.9-4.5")
    print(5 - 3)("计算5-3")
    num = 3
    print(-num)("num取反")
    print(--num)("num两次取反")
    print(-(-num))("使用括号限制优先级")
    print({1, 2, 3} - {3, 4, 5})("计算集合{1,2,3}和{3,4,5}的差集")
    print({3, 4, 5} - {1, 2, 3})("计算集合{3,4,5}和{1,2,3}的差集")


def ContentFive():
    print(33333 * 55555)("计算数字33333和数字55555的乘法")
    print((3 + 4j) * (5 + 6j))("计算复数3+4j和复数5+6j的乘法")
    print("重要的事情说三遍！" * 3)("打印三次\"重要的事情说三遍！\"")
    print([0] * 5)("[0]*5 生成一个长度为5的列表，列表中的元素都是0")
    print((0,) * 3)("(0,)*3 生成一个长度为3的元组，元组中的元素都是0")


def ContentSix():
    print(2 ** 4)("2**4 2的4次方")
    print(3 ** 3 ** 3)("3 ** 3 ** 3 3的3次方的3次方")
    print(3 ** (3 ** 3))("3 ** (3 ** 3) 使用括号限制优先级")
    print((3 ** 3) ** 3)("(3 ** 3) ** 3 使用括号限制优先级")
    print(9 ** 0.5)("9 ** 0.5 9的平方根")
    print((-1) ** 0.5)("(-1) ** 0.5 负数的平方根 复数")


def ContentSeven():
    print(17 / 4)("17/4 17除以4 浮点计算")
    print(17 // 4)("17//4 17除以4 整数计算")
    print((-17) / 4)("(-17)/4 -17除以4 浮点计算")
    print((-17) // 4)("(-17)//4 -17除以4 整数计算")


def ContentEight():
    print(3 + 2 < 7 + 8)("3 + 2 < 7 + 8 加法运算符优先级高于比较运算符")
    print(3 < 5 > 2)("3 < 5 > 2 相当于 3 < 5 and 5 > 2 ")
    print(3 == 3 < 5)("3 == 3 < 5 相当于 3==3 and 3<5 ")
    print('12345' > '23456')("'12345' > '23456' 字符串比较大小 依次比较每个字符的ASCII码值")
    print('abcd' > 'Abcd')("'abcd' > 'Abcd' 字符串比较大小 依次比较每个字符的ASCII码值")
    print([85, 92, 73, 84] < [91, 82, 73])("[85, 92, 73, 84] < [91, 82, 73] 列表比较大小 依次比较每个元素的大小")
    print([180, 90, 101] > [180, 90, 99])("[180, 90, 101] > [180, 90, 99] 列表比较大小 依次比较每个元素的大小")
    print({1, 2, 3, 4} > {3, 4, 5})("{1, 2, 3, 4} > {3, 4, 5} 集合比较 第一个不是第二个的超集")
    print({1, 2, 3, 4} <= {3, 4, 5})("{1, 2, 3, 4} <= {3, 4, 5} 集合比较 第一个不是第二个的子集")
    print([1, 2, 3, 4] > [1, 2, 3])("[1, 2, 3, 4] > [1, 2, 3] 列表比较前三个元素相同，第一个列表有多余元素 ")


def ContentNine():
    print(60 in [70, 60, 50, 80])("60 in [70, 60, 50, 80] 列表中是否包含60")
    print('abc' in 'a1b2cdfg')("'abc' in 'a1b2cdfg' 字符串中是否包含abc")
    print([3] in [[3], [4], [5]])("[3] in [[3], [4], [5]] 列表中是否包含[3]")
    print('3' in map(str, range(5)))("'3' in map(str, range(5)) 将range(5)的结果依次str操作 然后检测'3'在不在其中 ")
    print(5 in range(5))("5 in range(5) 检测5是否在range(5)中")


def ContentTen():
    print(int(3.5))("int(3.5) 3.5转换为整数")
    print(int('119'))("int('119') 119转换为整数")
    print(int('1111', 2))("int('1111', 2) 1111转换为二进制")
    print(int('1111', 8))("int('1111', 8) 1111转换为八进制")
    print(int('1111', 16))("int('1111', 16) 1111转换为十六进制")
    print(int('  9\n'))("int('  9\\n') 类型转换自动去除空格和换行符")
    print(float('3.1415926'))("float('3.1415926') 3.1415926转换为浮点数")
    print(float('-inf'))("float('-inf') 负无穷")
    print(complex(3, 4))("complex(3, 4) 3+4j")
    print(complex(6j))("complex(6j) 6j")
    print(complex('3'))("complex('3') 3+0j")


def ContentEleven():
    print(bin(8888))("bin(8888) 8888以二进制表示")
    print(oct(8888))("oct(8888) 8888以八进制表示")
    print(hex(8888))("hex(8888) 8888以十六进制表示")
    print(ord('a'))("ord('a') ord()函数获取字符的整数表示")
    print(ord('董'))("ord('董') ord()函数获取字符的整数表示")
    print(chr(65))("chr(65) chr()函数把编码转换为对应的字符")
    print(chr(33891))("chr(33891)   chr()函数把编码转换为对应的字符")
    print(str([1, 2, 3, 4]))("str([1, 2, 3, 4]) str()函数把任意类型转换为字符串")
    print(str({1, 2, 3, 4}))("str({1, 2, 3, 4}) str()函数把任意类型转换为字符串")


def ContentTwelve():
    print(list(), tuple(), dict(), set())("list(), tuple(), dict(), set() 依次调用构造函数")
    s = {3, 2, 1, 4}
    print(list(s), tuple(s))("list(s), tuple(s) 类型转换 集合转列表和元组")
    lst = [1, 1, 2, 2, 3, 4]
    print(tuple(lst), set(lst))("tuple(lst), set(lst) 类型转换 列表转元组和集合 然后集合自动去重")
    print(list(str(lst)))("list(str(lst)) 列表先转字符串再转列表")
    print(dict(name="Dong", sex="Male", age=41))('dict(name="Dong", sex="Male", age=41) 打印这个字典')


def ContentThirteen():
    print("绘制条形图")()
    if platform.system() == 'Darwin':
        font = FontProperties(fname=r"/System/Library/Fonts/STHeiti Light.ttc", size=14)
    else:
        font = FontProperties(fname=r"C:\windows\fonts\msyhl.ttc", size=14)

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
        console.print(f"执行函数：{funcName}", style="bold blue")
        eval(funcName)()
        print()()
