from functions import *
from algorithms import *
from tests import *

def description():
    print("\n\nМЕНЮ:")
    print("1. Расстояние Левенштейна")
    print("2. Расстояние Дамерау-Левенштейна")
    print("3. Расстояние Дамерау-Левенштейна (рекурсивно)")
    print("4. Расстояние Дамерау-Левенштейна (рекурсивно с кешем)")
    print("5. Измерить время")
    print("0. Выход\n")
    print("Выберите пункт: ", end="")


def menu():
    option = -1
    
    while option != 0:
        description()
        try:
            option = int(input())
        except:
            option = 6
            
        if option == 1:
            str1, str2 = input_strings()
            result = levenshtein_distance(str1, str2)
            print("\nРезультат:", result)
        
        elif option == 2:
            str1, str2 = input_strings()
            result = damerau_levenshtein_distance(str1, str2)
            print("\nРезультат:", result)
            
        elif option == 3:
            str1, str2 = input_strings()
            result = damerau_levenshtein_distance_recursive(str1, str2)
            print("\nРезультат:", result)
        
        elif option == 4:
            str1, str2 = input_strings()
            result = damerau_levenshtein_distance_recursive_cache(str1, str2)
            print("\nРезультат:", result)
            
        elif option == 5:
            test_time_memory()

        elif option == 0:
            pass
        
        else:
            print("Необходимо ввести цифру от 0 до 5")