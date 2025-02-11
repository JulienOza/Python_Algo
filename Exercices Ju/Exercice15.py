def full_name(first_name, last_name) :
    return f"{first_name} {last_name}"


first_name = input("What's your first name ? : ")
last_name = input("What's your last name ? : ")

name = full_name(first_name, last_name).title()
print(f"Your full name is {name}")