from dragon_name_generator import dragon_name
from penguin_name_generator import penguin_name

choice = input("Do you want to know your Dragon name or Penguin name? Please enter 'Dragon' or 'Penguin'.\n")

if choice == "Dragon":
    first_name = input("What is your first name?\n")
    birth_month = input("What month were you born? Enter a number from 1 - 12\n")
    print(dragon_name(first_name, birth_month))
else:
    first_name = input("What is your first name?\n")
    birth_month = input("What month were you born? Enter a number from 1 - 12\n")
    gender = input("What is your gender? Please enter M or F.\n").capitalize()
    print(penguin_name(first_name, birth_month, gender))
