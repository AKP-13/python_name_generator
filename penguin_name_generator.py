months = {
    "January": "The Icy",
    "February": "The Slippery",
    "March": "Shiverson",
    "April": "The Coldrageous",
    "May": "The Brrrave",
    "June": "Clubperson",
    "July": "Iceberg",
    "August": "Icicle",
    "September": "Frosty",
    "October": "Chilly",
    "November": "Breezy",
    "December": "Christmas"
}

male_initials = {
    "A": "Albert",
    "B": "Bertie",
    "C": "Charlie",
    "D": "Diver",
    "E": "Eskimino",
    "F": "Fisher",
    "G": "Grumpy",
    "H": "Hopper",
    "I": "Icy",
    "J": "Jumpy",
    "K": "Kai",
    "L": "Libelle",
    "M": "Matty",
    "N": "Naughty",
    "O": "Oliver",
    "P": "Pingu",
    "Q": "Quackie",
    "R": "Roger",
    "S": "Snowy",
    "T": "Tiny",
    "U": "Uther",
    "V": "Vuppie",
    "W": "Whitey",
    "X": "Xylo",
    "Y": "Yappie",
    "Z": "Zoro"
}

female_initials = {
    "A": "Arctica",
    "B": "Bergie",
    "C": "Coolie",
    "D": "Defrostia",
    "E": "Elsa",
    "F": "Frida",
    "G": "Gloria",
    "H": "Hoppie",
    "I": "Icerella",
    "J": "Juniper",
    "K": "Kimba",
    "L": "Libelle",
    "M": "Malinda",
    "N": "Northie",
    "O": "Olivia",
    "P": "Pingu",
    "Q": "Quackie",
    "R": "Rachel",
    "S": "Snowy",
    "T": "Tiny",
    "U": "Ursula",
    "V": "Vuppie",
    "W": "Whitey",
    "X": "Xylo",
    "Y": "Yuppie",
    "Z": "Zelda"
}

first_name = input("What is your first name?\n")

gender = input("What is your gender? Please enter M or F.\n").capitalize()

birth_month = input("What month were you born?\n").capitalize()


if gender == "M":
    print(f"Your Penguin name is {male_initials[first_name[0]]} {months[birth_month]}")
else:
    print(f"Your Penguin name is {female_initials[first_name[0]]} {months[birth_month]}")
    