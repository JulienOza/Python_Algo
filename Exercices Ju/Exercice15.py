# Si seul certains paramètres par défaut , les mettre en dernier 
def full_name(first_name: str = "John", last_name: str = "Doe") : 
    return f"{first_name} {last_name}"

first_name = input("What's your first name ? : ")
last_name = input("What's your last name ? : ")

print(f"Your full name is {full_name(first_name, last_name).title()}")

# print(f"Your full name is {full_name().title()}")
