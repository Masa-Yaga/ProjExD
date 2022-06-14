import random

NUM_OF_ALL_CHARAS = 10


def main():

    for _ in range():
        seikai = shutudai()
        #kaitou(seikai)

def shutudai():
    character = [chr(c+65) for c in range(26)]
    all_chara_list = random.sample(character, NUM_OF_ALL_CHARAS)

    print(all_chara_list)


if __name__ == "__main__":
    main()