from dragon_name_generator import dragon_name
from penguin_name_generator import penguin_name

first_name = input("What is your first name?\n")

birth_month = input("What month were you born? Enter a number from 1 - 12\n")

gender = input("What is your gender? Please enter M or F.\n").capitalize()

outcome = penguin_name(first_name, birth_month, gender)

print(outcome)
