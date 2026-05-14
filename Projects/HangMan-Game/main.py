def clear() -> None:  # clear function making
    """Clear the terminal."""  # ...
    print("\033[H\033[2J", end="", flush=True)  # ...


import random  # import random
from words import word_list  # import word_list

chosen_word = random.choice(word_list)  # randomly choose word
word_length = len(chosen_word)  # then check its length
from logo_stages import logo, stages  # import the logo & stages
print(logo)  # print logo
# testing code= print(f"the solution is {chosen_word}.")
display = []  # Create blanks
for _ in range(word_length):  # ...
    display += "_"  # ...
lives = 6  # lives
end_of_game = False  # starter....
while not end_of_game:  # while loop run until its = true
    guess = input("Guess a letter: ").lower()  # guess
    clear()  # clear function calling
    if guess in display:  # If the user has entered a letter they've already guessed
        print(f"You've already guessed {guess}")  # print the letter to know him/her
    for position in range(word_length):  # Check: all the letter by comparing its position
        letter = chosen_word[position]  # eg..letter=bamboo[0] OR letter=bamboo[1]
        if letter == guess:  # then if letter is equal to guess letter
            display[position] = letter  # replace the letter by dash "_"
    if guess not in chosen_word:  # If the letter is not in the chosen_word
        print(f"You guessed {guess}, that's not in the word. You lose a life.")  # print the letter to know him/her
        lives -= 1  # You lose a life
        if lives == 0:  # If all life wasted
            end_of_game = True  # so end the while loop
            print("You lose.")  # END GAME
    print(f"{' '.join(display)}")  # Join all the elements in the list and turn it into a String.
    if "_" not in display:  # Check if user has got all letters
        end_of_game = True  # so our game is completed
        print("You win.")  # WIN GAME
    print(stages[lives])  # print stages
