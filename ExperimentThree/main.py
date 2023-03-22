from rich.console import Console

console = Console()

oldPrint = print


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
    pass

if __name__ == '__main__':
    funcList = ['One', 'Two', 'Three']
    for func in funcList:
        funcName = 'Content' + func
        console.print(f"执行函数：{funcName}", style="bold blue")
        eval(funcName)()
        oldPrint()
