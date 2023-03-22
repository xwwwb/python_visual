import os

fileList = ["ExperimentOne", "ExperimentTwo","ExperimentThree"]

#default = 0
default = 3 # 默认要执行的实验

if not default:
    while True:
        print("请选择需要执行的实验，输入q退出")
        print("1. 实验一")
        print("2. 实验二")
        choise = input("请输入编号：\n")
        if choise.isdigit() and len(fileList) + 1 > int(choise) > 0:
            name = int(choise)
            os.system(f"python ./{fileList[name - 1]}/main.py")
        elif choise == 'q':
            break
        else:
            print("请输入正确编号")
else:
    os.system(f"python ./{fileList[default - 1]}/main.py")