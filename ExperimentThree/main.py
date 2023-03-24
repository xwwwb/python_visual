from rich.console import Console

console = Console()

oldPrint = print
from random import shuffle
from operator import add

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

    data = zip('1234',[1,2,3,4,5,6])
    print(data)
    print(list(data))
    data = zip('1234',[1,2,3,4,5,6])
    print(tuple(data))
    data = zip('1234',[1,2,3,4,5,6])
    for i in data:
        print(i)

if __name__ == '__main__':
    funcList = ['One', 'Two', 'Three', 'Four', 'Five']
    for func in funcList:
        funcName = 'Content' + func
        console.print(f"执行函数：{funcName}", style="bold blue")
        eval(funcName)()
        oldPrint()
