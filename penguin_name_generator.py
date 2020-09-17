months = {
    "1": "The Icy",
    "2": "The Slippery",
    "3": "Shiverson",
    "4": "The Coldrageous",
    "5": "The Brrrave",
    "6": "Clubperson",
    "7": "Iceberg",
    "8": "Icicle",
    "9": "Frosty",
    "10": "Chilly",
    "11": "Breezy",
    "12": "Christmas"
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

def penguin_name (first_name, birth_month, gender):
    if gender == "M":
        return(f"Your Penguin name is {male_initials[first_name[0]]} {months[birth_month]}")
    else:
        return(f"Your Penguin name is {female_initials[first_name[0]]} {months[birth_month]}")
    