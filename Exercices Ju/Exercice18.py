def compter_lettre_a(phrase: str) -> int:
    count_a = 0
    for lettre in phrase.lower():
        if lettre == "a":
            count_a +=1
    return count_a

def compter_lettre_e(phrase: str) -> int:
    return phrase.lower().count("e")

phrase = input("Saisissez une phrase : ")

print(f"La phrase compte {compter_lettre_a(phrase)} fois la lettre 'a' et {compter_lettre_e(phrase)} la lettre 'e' ")
