from random import randint

def main():
    seikai = shutudai()
    kaitou(seikai)

def shutudai():
    kontena = [{"q":"サザエの旦那の名前は？","a":["ますお","マスオ"]},
                {"q":"カツオの妹の名前は？","a":["わかめ","ワカメ"]},
                {"q":"タラオはカツオから見てどんな関係？","a":["甥","おい", "甥っ子", "おいっこ"]}]
    print("問題：")
    ra = randint(0, 2)
    print(kontena[ra]["q"])
    return kontena[ra]["a"]

def kaitou(seikai):
    ans = input("答えてください")
    if ans in seikai:
        print("正解!!!")
    else:
        print("不正解!!")

if __name__ == "__main__":
    main()