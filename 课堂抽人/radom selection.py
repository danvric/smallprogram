import random

def main():
    # ---------- 1. 输入总人数 ----------
    while True:
        s = input("请输入学生总人数（学号 1 ~ n）：").strip()
        if s.isdigit() and int(s) > 0:
            n = int(s)
            break
        print("输入有误，请输入一个正整数。")

    # ---------- 2. 生成学号池并打乱 ----------
    pool = list(range(1, n + 1))   # 学号 1, 2, ..., n
    random.shuffle(pool)           # 打乱，避免按顺序抽
    picked = []                    # 已抽到的学号

    print(f"\n共 {n} 个学号。直接按【回车】抽人，输入 q 退出。\n")

    # ---------- 3. 循环抽取 ----------
    while pool:
        cmd = input("按回车抽人 > ").strip().lower()
        if cmd in ("q", "quit", "exit"):
            break
        num = pool.pop()           # 抽一个（抽过的不再出现）
        picked.append(num)
        print(f"  ★ 抽到学号：{num}   （已抽 {len(picked)}/{n}，剩余 {len(pool)}）\n")
    else:
        # pool 空了才会执行这里（break 退出不执行）
        print("所有同学都抽过一遍啦！\n")

    if picked:
        print("本轮已抽到的学号：", "、".join(map(str, sorted(picked))))

if __name__ == "__main__":
    main()