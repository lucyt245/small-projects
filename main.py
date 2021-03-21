
import random


def menu_system():
    exit = False
    while not exit:
        print("\n------------------------------")
        print("Welcome to Lucy's menu system!")
        print("------------------------------")
        print("1 - Mad libs")
        print("2 - Month dictionary")
        print("3 - Hangman")
        print("0 - Exit")

        choice = int_validation()
        print("\n")

        if choice == 1:
            mad_libs()
        elif choice == 2:
            month_dictionary()
        elif choice == 3:
            hangman()
        elif choice == 0:
            exit = True


def int_validation():
    valid = False

    while not valid:
        try:
            number = int(input("Please enter your choice: "))
            valid = True
            return number
        except ValueError:
            print("Invalid option entered")


def a_or_an(word):
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in range(0, len(vowels)):
        if word[0] == vowels[i]:
            return 'an ' + word

    return 'a ' + word


def mad_libs():
    print("----------")
    print(" Mad Libs")
    print("----------")

    word_one = input("Please enter an adjective: ")
    word_two = input("Please enter a noun: ")
    word_three = input("Please enter a plural noun: ")
    word_four = input("Please enter a person in the room (f): ")
    word_five = input("Please enter an adjective: ")
    word_six = input("Please enter an article of clothing: ")
    word_seven = input("Please enter an '-ing' verb: ")
    word_eight = input("Please enter an adjective: ")
    word_nine = input("Please enter a place name: ")

    print("-----------------------------\n")
    print("There are many " + str(word_one) + " ways to choose " + str(a_or_an(word_two)) + " " + str(word_two))
    print("to read. First, you could ask for recommendations from your friends and " + str(word_three) + ".")
    print("Just don't ask Aunt " + str(word_four) + " - she only reads " + str(word_five) + " books with ")
    print(str(word_six) + "-ripping goddesses on the front cover. If your friends and family are no help, try ")
    print(str(word_seven) + " the " + str(word_eight) + " review in 'The " + str(word_nine) + " Times'.")


def month_dictionary():
    print("-----------------")
    print(" Month Converter")
    print("-----------------")

    month_converter = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "May": "May",
        "Apr": "April",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December",
    }

    month = input("Enter the shortened version of the month: ")
    month = month.capitalize()
    print(month_converter.get(month, "This is not a shortened month"))


def word_get():
    words = open("words.txt", "r")
    lineRead = words.readline()
    word_list = []
    hint_list = []
    i = 0

    while lineRead != "":
        split_words = lineRead.split(", ")
        word_list.append(split_words[0])
        hint_list.append(split_words[1])
        i += 1
        lineRead = words.readline()

    words.close()
    number = random.randint(0, i - 1)
    word_choice = word_list[number]
    # print(word_choice)
    hint = hint_list[number]
    # print(hint)
    return word_choice, hint


def guess_validate(wrong_guesses, word_choice, word_display, guessed):
    guessed_before = False

    user_guess = input("Please guess a letter or the word: ")
    print(guessed)

    # checks that the letter/word hasn't already been guessed
    for i in range(0, len(guessed)):
        if guessed[i] == user_guess:
            guessed_before = True

    # isaplha() checks that the input is a string made of letter
    if user_guess.isalpha() and not guessed_before:
        guessed.append(user_guess)
        # print(guessed)
        # returns it as upper case
        return user_guess.upper()
    elif guessed_before:
        print("You've already guessed that")
        hangman_guessing(wrong_guesses, word_choice, word_display, guessed)
    else:
        print("Invalid guess")
        hangman_guessing(wrong_guesses, word_choice, word_display, guessed)


def hangman_display(wrong_guesses):
    dead = ['''
              o
             /|\\
              |
             / \\
            ''',
            '''
              o
             /|\\
              |
             / 
            ''',
            '''
              o
             /|\\
              |

            ''',
            '''
              o
             /|
              |

            ''',
            '''
              o
              |
              |

            ''',
            '''
              o
              |
              
             
            ''']

    return dead[wrong_guesses]


def hangman():
    print("---------")
    print(" Hangman")
    print("---------")

    word_choice, hint = word_get()
    word_display = []

    for i in range(0, len(word_choice)):
        word_display.append("_")
        i += 1

    wrong_guesses = 0
    guessed = []
    print(hangman_display(wrong_guesses))
    print(word_display)
    hangman_guessing(wrong_guesses, word_choice, word_display, guessed)


def hangman_guessing(wrong_guesses, word_choice, word_display, guessed):
    while wrong_guesses < 5:
        guessed_letter = False
        user_guess = guess_validate(wrong_guesses, word_choice, word_display, guessed)
        if len(user_guess) > 1:
            if user_guess == word_choice:
                print("Congratulations!")
                print("You guessed the word!")
                menu_system()
            else:
                print("Incorrect guess!")
                wrong_guesses += 1
                print(hangman_display(wrong_guesses))
                print(word_display)

        else:
            for i in range(0, len(word_choice)):
                if user_guess == word_choice[i]:
                    print("You guessed a letter!")
                    guessed_letter = True
                    word_display[i] = user_guess

            if not guessed_letter:
                print("Incorrect guess!")
                wrong_guesses += 1

            print(hangman_display(wrong_guesses))
            print(word_display)

    print("You had too many wrong guesses and DIED")
    print("Better luck next time!")


menu_system()
