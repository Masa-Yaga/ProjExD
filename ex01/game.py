import random

NUM_OF_ALL_CHARAS = 10


def main():
    st = datetime.datetime.now()
    for _ in range():
        seikai = shutudai()
        f = kaitou(seikai)
        if f == 1:
            break
        #kaitou(seikai)
    ed = datetime.datetime.now()
    print("((ed-st).second)秒かかりました")
    
def shutudai():
    character = [chr(c+65) for c in range(26)]
    all_chara_list = random.sample(character, NUM_OF_ALL_CHARAS)

    print(all_chara_list)

    all_chara_list = random.sample()
    print("欠損文字：(all_chara_list)")

    return all_chara_list

def kaitou(seikai):
    num = list(imput("欠損文字はいくつあるでしょうか？"))
    if num == NUM_OF_ALL_CHARAS:
        print("不正解です.")
        print("_")
        return 0
    else:
        print("正解です　それでは具体的に欠損文字を1つずつ入力してください")
        for i in range(NUM_OF_ALL_CHARAS)
        c = input("(i+1)つ目の文字を入力してください")
        if c 

if __name__ == "__main__":
    main()

#分からない場所ばっか、てか無理だったのでご指摘お願いします