
import random
from hangman_words import word_list
from hangman_stages_logo import stages
from hangman_stages_logo import logo
def restart_game():
    return True

start_game = True  # Variable to control the game loop

while start_game:
    print(logo)
    #Alegeti aleatoriu un cuvant din word_list si atribuiti-l unei variabile numite chosen word.
    chosen_word=random.choice(word_list)
    print(chosen_word)
    #ToDo3Verificati daca litera pe care utilizatorul a ghicit-o(guess) este una din literele din chosen_word.
    #Creati o lista goala numita display.
    display= []
    #Pentru fiecare litera din chosen_word adaugati un "_" "display".
    chosen_word_lenght=len(chosen_word)
    for letter in range(chosen_word_lenght):
       display+= "_"
    print(display)
    #Cereti utilizatorului sa ghiceasca o litera si sa atribuie raspunsul unei variabile numite guess. faceti variabila lower case
    #guess = input("Write your letter: ").lower()
    #Faceti un loop prin fiecare pozitie din chosen_word;
    #Daca litera din acea pozitie se potriveste cu "guess" atunci arata acea litera pe display
    #Imprimati "display" si ar trebui sa vedeti litera ghicita in pozitia corecta si fiecare litera inlocuita cu "_"
    #Alegeti aleatoriu un cuvant din word_list si atribuiti-l unei variabile numite chosen word.
    # Folositi o bucla while pentru a lasa utilizatorul sa ghiceasca din nou. Bucla ar trebui sa se opreasca numai daca utilizatorul a castigat
    #max_attempt=3
    #attempt=0
    chosen_word_length = len(chosen_word)
    max_attempts = 7
    attempt = 0
    guess_list = []  # Initialize as a list to store guesses
    while attempt < max_attempts and "_" in display:
        guess = input("Write your letter: ").lower()
        if guess in guess_list:
            print("This was already a guess")
            print("Your guesses:", ", ".join(guess_list))
            continue
        guess_list.append(guess)
        found = False  # Flag to check if the guessed letter is found in the word
        for position in range(chosen_word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                found = True
                print("Correct, well done. ")
        print(stages[max_attempts - attempt])
        print(" ".join(display))
        if not found:
            attempt += 1
            print(f"Try again. Attempts left: {max_attempts - attempt}")
            print(stages[max_attempts - attempt])


    if "_" in display:
        print("You lost! No attempts left.")
    else:
        print("Congratulations! You won!")

    end_game=input("Play again? Press Y for yes, N for No:").lower()
    if end_game == "y":
            start_game = restart_game()
    else:
            start_game = False



