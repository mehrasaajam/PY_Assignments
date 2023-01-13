
import gtts

def read_from_file():
    f = open("translate.txt", "r")
    temp = f.read().split("\n")

    global words_bank
    words_bank = []
    for i in range(0, len(temp), 2):
        my_dict = {"en": temp[i], "pe": temp[i+1]}
        words_bank.append(my_dict)

    f.close()

def write_to_file():
    f = open("translate.txt", "a")
    f.write("\n" + input("Please enter english word: "))
    f.write("\n" + input("Please enter persian word: "))
    f.close()

def translate_english_to_persian():
    user_text = input("Enter your english text: ")
    user_sentence = user_text.split(".")
    output_final = ""
    
    for i in range(len(user_sentence)):
        user_words = user_sentence[i].split(" ")
        output = ""

        for user_word in user_words:

            for word in words_bank:

                if user_word == word["en"]:
                    output = output + word["pe"] + " "
                    break
            else:
                output = output + user_word + " "
        print(output)
        output_final = output_final + output
    x = gtts.gTTS(output_final , lang = "ar", slow = False)
    x.save("voice.mp3")

def translate_persian_to_english():
    user_text = input("Enter your persian text: ")
    user_sentence = user_text.split(".")
    output_final = ""

    for i in range(len(user_sentence)):
        user_words = user_sentence[i].split(" ")
        output = ""

        for user_word in user_words:

            for word in words_bank:

                if user_word == word["pe"]:
                    output = output + word["en"] + " "
                    break
            else:
                output = output + user_word + " "
        print(output)
        output_final = output_final + output
    x = gtts.gTTS(output_final , lang = "ar", slow = False)
    x.save("voice.mp3")
        
def show_menu():
    print("Welcome to my translate")
    print("1: Translate english to persian")
    print("2: Translate persian to english")
    print("3: Add a new word to database")
    print("4: Exit")


read_from_file()

while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        translate_english_to_persian()
    elif choice == 2:
        translate_persian_to_english()
    elif choice == 3:
        write_to_file()
    elif choice == 4:
        exit(0)
