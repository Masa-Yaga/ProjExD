import random

NUM_OF_ALL_CHARAS = 10


def main():
    st = datetime.datetime.now()
    for _ in range():
        seikai = shutudai()
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
    if num == 
        print("正解です　それでは具体的に欠損文字を1つずつ入力してください")
    

if __name__ == "__main__":
    main()