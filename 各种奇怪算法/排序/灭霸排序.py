import random

n = int(input("请输入一共有多少数字："))
function = int(input("要正序还是倒序(0 or 1)："))

ara = []
for i in range(n):
    ara.append(int(input(f"输入第{i+1}个数字：")))

times = 0   # 响指次数

def is_sorted(arr, func):
    """检查 arr 是否按 func 要求有序"""
    for i in range(len(arr) - 1):
        if func == 0 and arr[i] > arr[i+1]:
            return False
        if func == 1 and arr[i] < arr[i+1]:
            return False
    return True

while not is_sorted(ara, function):
    times += 1
    # 随机删掉一半：先决定删多少个
    half = len(ara) // 2          # 向下取整
    if len(ara) % 2 == 1:
        # 奇数个：随机决定删 half 个还是 half+1 个
        half = random.choice([half, half + 1])
    # 随机选 half 个下标删掉
    victims = random.sample(range(len(ara)), half)
    # 从大到小删，避免下标错位
    for idx in sorted(victims, reverse=True):
        del ara[idx]

print("排序完成：", ara)
print("响指次数：", times)