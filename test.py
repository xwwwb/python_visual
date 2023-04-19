import random
def test(num):
    # 这里的num一定是四位数
    a = num // 1000
    b = num % 1000 // 100
    c = num % 100 // 10
    d = num % 10
    list = [a, b, c, d] # 这是四个数字
    count = 0
    while True:
        if count > 7:
            return False
        # 拿到最大数
        list_1 = sorted(list, reverse=True)
        num_1 = list_1[0] * 1000 + list_1[1] * 100 + list_1[2] * 10 + list_1[3]
        # 拿到最小数
        list_2 = sorted(list)
        num_2 = list_2[0] * 1000 + list_2[1] * 100 + list_2[2] * 10 + list_2[3]
        # 差值
        num_3 = num_1 - num_2
        if num_3 == 6174:
            return True
        else:
            a = num_3 // 1000
            b = num_3 % 1000 // 100
            c = num_3 % 100 // 10
            d = num_3 % 10
            list = [a, b, c, d]
            count += 1

# 生成20个四位数
testList = []
for i in range(20):
    num = random.randint(1000, 9999)
    testList.append(num)

result = all(True == test(i) for i in testList)
print(result)