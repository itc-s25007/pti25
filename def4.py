import random



def omikuji():



    kuji = ["大吉","中吉","吉","小吉","凶"]

    result = random.choice(kuji)

    #print(result)
    return random.choice(kuji)


kekka = omikuji()
print(f"結果は{kekka}です。")
