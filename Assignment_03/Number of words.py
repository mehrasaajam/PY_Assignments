
sentence = input("please enter a sentence: ")

word = 1

for i in range(len(sentence)):
            if sentence[i] == " " and sentence[i+1] != " ":
                word += 1

print(word)
