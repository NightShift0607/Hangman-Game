import random
import words
import arts

chosen_word = random.choice(words.word_list)
lives = 6

print(arts.logo)
display = []
for j in range(len(chosen_word)):
    display.append("_")
flag = True
while flag:
    guess = input("Guess a letter: ")
    guess = guess.lower()
    if guess in display:
        print(f"You have already guess {guess}")
    for i in range(len(chosen_word)):
        if (chosen_word[i] == guess):
            display[i] = guess
    if guess not in chosen_word:
        print("You guess the wrong letter. You lost 1 life.")
        lives -= 1
    print(arts.stages[lives])
    str_display = ' '.join(display)
    print(str_display,"\n")
    if not '_' in display:
        flag = False
        print("You Won!!!")
    elif lives == 0:
        flag = False
        print("You Lose!!!")
        print(f"The chosen word was {chosen_word}.")