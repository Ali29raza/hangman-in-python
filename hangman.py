import random
words=["APPLE", "CAT", "BUS", "SHARK", "DOG", "JUNGLE"]
word=random.choice(words)
guessed_word= "_"*len(word)
total_chances=6
# print(guessed_word)

while total_chances !=0:
    print(guessed_word)
    letter=input("guess a letter: ").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index]==letter:
                guessed_word=guessed_word[:index]+letter+guessed_word[index+1:]
        if guessed_word==word:
            print("congrats you have won the game")
            break
    else:
        print("incorrect guess")
        total_chances-=1
        print("your remaining chances are: ", total_chances)
else:
    print("Game over")
    print("you lose")
    print("your all chances are exhausted")

print("the correct word is: " , word)
