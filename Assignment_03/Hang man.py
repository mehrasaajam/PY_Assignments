
import random

user_mistakes = 0
good_chars = []
bad_chars = []

words_bank = ["home", "brother", "office", "yellow", "white"]

x = random.randint(0, len(words_bank)-1)
word = words_bank[x]

while user_mistakes < 6:

    for i in range(len(word)):

        if word[i]in good_chars:
            print(word[i], end = " ")
        else:
            print("_", end = " ")

    user_char = input("please write your guess: ").lower()
    if len(user_char) == 1:

        if user_char in word:
            good_chars.append(user_char)
            print("✅")
        else:
            bad_chars.append(user_char)
            user_mistakes += 1
            print("❌")

    else:
        print("you can't enter more than one object!")

    if len(good_chars) == len(word):
        print("well down! you win 🎊")
        break

else:
    print("game over ☹")
