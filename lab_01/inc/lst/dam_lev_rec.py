from functions import *

def damerau_levenshtein_distance_recursive(str1, str2):
    n, m = len(str1), len(str2)

    flag = 0
    if n == 0 or m == 0:
        return abs(n - m)

    if str1[-1] != str2[-1]:
        flag = 1

    result = min(
        damerau_levenshtein_distance_recursive(str1[:-1], str2) + 1,
        damerau_levenshtein_distance_recursive(str1, str2[:-1]) + 1,
        damerau_levenshtein_distance_recursive(str1[:-1], str2[:-1]) + flag)
    
    if n > 1 and m > 1 and str1[-1] == str2[-2] and str1[-2] == str2[-1]:
        result = min(result, damerau_levenshtein_distance_recursive(str1[:-2], str2[:-2]) + 1)

    return result