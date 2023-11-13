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