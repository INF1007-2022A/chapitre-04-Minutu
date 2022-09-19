#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    #Vérifier si le nombre de caractères d’une chaîne de caractères est pair
    return len(string) % 2 == 0




def remove_third_char(string: str) -> str:
    #Supprimer le 3ème caractère d’une chaîne de caractères
    string=string[0:2]+string[3:]
    return string
#return string.replace(string[2],'')

def replace_char(string: str, old_char: str, new_char: str) -> str:
    #Remplacer un caractère d’une chaîne de caractère par un autre
    for i in range(len(string)):
        if string[i]==old_char:
            string=string[:i]+new_char+string[i+1:]
    return string

def get_number_of_char(string: str, char: str) -> int:
    number_of_char=0

    for c in string:
        if c==char:
            number_of_char+=1
    return number_of_char


def get_number_of_words(sentence: str, word: str) -> int:
    words = sentence.split()
    number_of_words=0
    for i in words:
        if i==word:
            number_of_words+=1
    return number_of_words


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
