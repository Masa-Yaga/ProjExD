import random
import datetime

kaisu = 5
taishou = 10
kesson = 2


def main():
    st = datetime.datetime.now()
    for _ in range(kaisu):
        seikai = shutudai()
        f = kaitou(seikai)
        if f == 1:
            break
        #kaitou(seikai)
    ed = datetime.datetime.now()
    print("((ed-st).second)秒かかりました")
    
def shutudai():
    character = [chr(c+65) for c in range(26)]
    all_chara_list = random.sample(character, taishou)

    print(all_chara_list)

    all_chara_list = random.sample()
    print("欠損文字：(all_chara_list)")

    return all_chara_list

def kaitou(seikai):
    ans_kesson = input("欠損文字はいくつあるでしょうか？：")
    if ans_kesson == str(kesson):
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
    else:
        print("不正解です。またのご利用をお待ちしております。")
        return 0

    for i in range(kesson):
        answer = input(f"{i+1}個めの文字を入力してください：")
        if answer.upper() not in seikai:
            print("不正解です。またのご利用お待ちしております。")
            return 0
        else:
            seikai.remove(answer.upper())
if __name__ == "__main__":
    main()

#分からない場所ばっか、てか無理だったのでご指摘お願いします
