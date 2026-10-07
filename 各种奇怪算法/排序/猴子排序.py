import random

n = int(input("请输入一共有多少数字："))
function = int(input("要正序还是倒序(0 or 1)："))

ara = []
for i in range(n):
    ara.append(int(input(f"输入第{i+1}个数字：")))
    
times = 0

while True:
    if function == 0:          # 正序
        for i in range(len(ara) - 1):
            if ara[i] > ara[i+1]:
                times += 1
                random.shuffle(ara)
                break
        else:
            break
    elif function == 1:        # 倒序
        for i in range(len(ara) - 1):
            if ara[i] < ara[i+1]:
                times += 1
                random.shuffle(ara)
                break
        else:
            break

print("排序完成：", ara)
print("次数：",times)