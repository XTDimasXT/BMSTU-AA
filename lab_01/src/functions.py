import random
import time

def input_strings():
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")
    return str1, str2


def create_levenshtein_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]
    
    for i in range(n):
        matrix[i][0] = i
    for j in range(m):
        matrix[0][j] = j 
    
    return matrix


def print_matrix(matrix, str1, str2):
    n, m = len(str1), len(str2)
    
    print("   ∅  " + "  ".join([symb for symb in str2]))
    for i in range(n + 1):
        if i != 0:
            print(str1[i - 1], end = "")
        else:
            print("∅", end = "")
        for j in range(m + 1):
            print("  " + str(matrix[i][j]), end = "")
        print()
        

def get_random_str(length):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    return "".join(random.choice(alphabet) for _ in range(length))
        

def get_time(function, length):
    count = 100
    time_res = 0
    
    for _ in range(count):
        str1 = get_random_str(length)
        str2 = get_random_str(length)
        
        time_1 = time.process_time()
        function(str1, str2)
        time_2 = time.process_time()
        
        time_res += (time_2 - time_1)
        
    return time_res / count
        