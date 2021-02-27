
def menu_system():
    exit = False
    while not exit:
        print("\n------------------------------")
        print("Welcome to Lucy's menu system!")
        print("------------------------------")
        print("1 - Mad libs")
        print("2 - Month dictionary")
        print("3 - Guess the word")
        print("4 - Files")
        print("5 - Hangman")
        print("0 - Exit")
        choice = int_validation()
        print("\n")
        if choice == 1:
            mad_libs()
        elif choice ==2:
            month_dictionary()
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


def mad_libs():
    print("--------")
    print("Mad Libs")
    print("--------")
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
    print("---------------")
    print("Month Converter")
    print("---------------")
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
    print(month_converter.get(month, "This is not a shortened month"))
    
    
 menu_system()
 
