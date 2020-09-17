from dragon_name_generator import dragon_name
from penguin_name_generator import penguin_name

def play():
    choice = input("Do you want to know your Dragon name or Penguin name? Please enter 'Dragon' or 'Penguin'.\n")
    # exit if choice == 'exit' else generate_name(choice)
    if choice == "exit":
        exit
    elif choice == "Dragon" or choice == "Penguin":
        generate_name(choice)
    else:
        play()

def generate_name(choice):
    try:
        if choice == "Dragon":
            first_name = input("What is your first name?\n")
            birth_month = input("What month were you born? Enter a number from 1 - 12\n")
            print(dragon_name(first_name, birth_month))
        else:
            first_name = input("What is your first name?\n")
            birth_month = input("What month were you born? Enter a number from 1 - 12\n")
            gender = input("What is your gender? Please enter M or F.\n").capitalize()
            print(penguin_name(first_name, birth_month, gender))
    except ValueError:
        print('Error')
    finally:
        play()

play()