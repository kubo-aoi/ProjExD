import datetime
import random
import string

tcount = 10
kcount = 2
max = 5

def main():
    start = datetime.datetime.now()
    for i in range(max):
        seikai = shutudai()
        correct = kaitou(seikai)
        if correct == 1:
            break
    end = datetime.datetime.now()
    print(f"所要時間：{(end-start).seconds}秒かかりました")

def shutudai():

    eng = string.ascii_uppercase
    teng = [random.choice(eng) for i in range(tcount)]
    print(f"対象文字は：{teng}")

    keng = [random.choice(teng) for i in range(kcount)]

    for i in range(kcount):
        teng.remove(keng[i])
    heng = teng
    print(f"表示文字は：{heng}")
    print(f"欠損文字は：{keng}")
    return keng

def kaitou(seikai):
    ans = int(input("欠損文字はいくつあるでしょうか？："))
    if ans != kcount:
        print("不正解です、、またチャレンジしてください")
        return 0

    else:
        print("正解です！それでは具体的に欠損文字を1つずつ入力してください")
        for i in range(kcount):
            first = input(f"{i+1}文字目を入力してください：")
            if first not in seikai:
                print("不正解です、、またチャレンジしてください")
                return 0
            seikai.remove(first)
        print("正解です")
        return 1

if __name__ == "__main__":
    main()
