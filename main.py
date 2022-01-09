import random


def menu_system():
    exit = False
    while not exit:
        print("\n------------------------------")
        print("Welcome to Lucy's menu system!")
        print("------------------------------")
        print("1 - Mad libs")
        print("2 - Month dictionary")
        print("3 - Band name generator")
        print("4 - Add word")
        print("5 - Prime numbers")
        print("6 - Number add")
        print("0 - Exit")

        choice = int_validation()
        print("\n")

        if choice == 1:
            mad_libs()
        elif choice == 2:
            month_dictionary()
        elif choice == 3:
            band_name()
        elif choice == 4:
            add_word()
        elif choice == 4:
            prime_nums()
        elif choice == 5:
            num_add()
        elif choice == 0:
            exit = True


def add_word():
    print("-----------")
    print(" Add words")
    print("-----------")
    words = open("words.txt", "r")
    user_word = input("What word would you like to add?: ")
    if user_word.isalpha():
        user_word = user_word.upper()
        line_read = words.readline()
        while line_read != "":
            line_split = line_read.split(", ")
            if line_split[0] == user_word:
                print("This word is already on the list")
                menu_system()
            line_read = words.readline()
        words.close()
        user_hint = input("What hint would you like to give for your word?: ")
        user_hint = user_hint.upper()
        add = user_word + ", " + user_hint + "\n"
        words = open("words.txt", "a")
        words.write(add)
        words.close()
        print("Your word and clue have been added to the list!")
    else:
        print("This isn't a valid word")


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


def band_name():
    city = input('What city did you grow up in?: ')
    pet = input('What was your first pet?: ')
    print(f'Your band could be called {city} {pet}')

    
def int_validate():
        try:
            user_number = int(input(""))
            valid = True
            return user_number
        except ValueError:
            print("Please enter an integer")


def prime_nums():
    print("------------------------")
    print(" Prime Number Generator")
    print("------------------------")
    print("What number do you want to stop at?: ")
    user_range = int_validate()
    if user_range < 3:
        print("This is too low of a number")
        prime_nums()
    elif user_range >= 500:
        print("This is too large of a number")
        prime_nums()
    else:
        for num in range(2, user_range):
            prime = True
            for multiple in range(2, num):
                if num % multiple == 0:
                    prime = False
                    num += 1
            if prime:
                print(num)
            num += 1


def num_add():
    print("--------------")
    print(" Number adder")
    print("--------------")
    print("How many numbers would you like to add: ")
    num_of_inputs = int_validate()
    if 1 <= num_of_inputs <= 10:
        numbers = input("Please enter the numbers you would like to add: ")
        numbers_list = numbers.split(" ")
        # print(numbers_list)
        if len(numbers_list) > num_of_inputs:
            print("Too many numbers entered")
            num_add()
        elif len(numbers_list) < num_of_inputs:
            print("Not enough numbers entered")
            print("Check that you have entered them in the correct format")
            num_add()
        num_total = 0
        for i in range(0, len(numbers_list)):
            if 0 <= int(numbers_list[i]) <= 10**10:
                num_total += int(numbers_list[i])
            else:
                print("Invalid numbers entered")
                num_add()
        print(num_total)
    else:
        print("Invalid number entered")


menu_system()
