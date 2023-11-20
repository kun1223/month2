import random
def start_game():
    animel=["собака", "кошка", "мышка","корова"]
    animels=random.choice(animel)
    word_letters=[]
    attemtes=5
    while attemtes>0:
        hiden_mord=""
        for letter in animels:
            if letter in animel:
                hiden_mord+=letter 
            else:
                hiden_mord+="_"
        print(f"Загадыные слова:{hiden_mord}")
        print(f"осталас{attemtes} папыток ")  
        user=input("ведите букву:").lower()
        if user in animel:
            print(f"откройте букву:{user}")
            continue
        animel.append(user)

        if user not in animels:
            attemtes-=1
            print("к сожелени такой буква нет")

            if "_" not in hiden_mord:
                print("В выйигрили")
                break

        if attemtes==0:
            print(f"Загадыное слова -({animels})")
            print(f"В поиграли")



        


