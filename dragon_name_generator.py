initials = {
    "A": "Abrasax",
    "B": "Bessie",
    "C": "Campacti",
    "D": "Draco",
    "E": "Erwin",
    "F": "Fafner",
    "G": "Gargoyle",
    "H": "Hydra",
    "I": "Iemisch",
    "J": "Jormungandr",
    "K": "Kimba",
    "L": "Libelle",
    "M": "Malinda",
    "N": "Nuri",
    "O": "Orm",
    "P": "Pendragon",
    "Q": "Quetzalcoatl",
    "R": "Ryoko",
    "S": "Samael",
    "T": "Tanwen",
    "U": "Uther",
    "V": "Vasuki",
    "W": "Wyvern",
    "X": "Xiuhcoatl",
    "Y": "Yaras",
    "Z": "Zamaran"
}

dragon_months = {
    "1": "The Terrifying",
    "2": "The Destructor",
    "3": "The Flame Breather",
    "4": "The Golden",
    "5": "The Magnificent",
    "6": "The Destroyer",
    "7": "The Wicked",
    "8": "The Wild",
    "9": "The Crusher",
    "10": "The Compassionate",
    "11": "The Craven",
    "12": "The Annihilator"
}

def dragon_name (first_name, birth_month):
    return f"Your Dragon name is {initials[first_name[0]]} {dragon_months[birth_month]}"