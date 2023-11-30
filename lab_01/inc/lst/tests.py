import matplotlib.pyplot as plt

from algorithms import *
from functions import *


def levenshtein_graph(lev_time):
    lengths = [i for i in range(0, 200, 20)]
    
    fig = plt.figure(figsize=(7, 5))
    plot = fig.add_subplot()
    plot.plot(lengths, lev_time, label = "Левенштейн")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина, символы")

    plt.show()
    
    
def damerau_levenshtein_graph(dam_lev_time):
    lengths = [i for i in range(0, 200, 20)]
    
    fig = plt.figure(figsize=(7, 5))
    plot = fig.add_subplot()
    plot.plot(lengths, dam_lev_time, label = "Дамерау-Левенштейн")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина, символы")

    plt.show()
    
    
def damerau_levenshtein_recursive_time(dam_lev_rec_time):
    lengths = [i for i in range(10)]
    
    fig = plt.figure(figsize=(7, 5))
    plot = fig.add_subplot()
    plot.plot(lengths, dam_lev_rec_time, label = "Дамерау-Левенштейн (рекурсивно)")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина, символы")

    plt.show()
    

def damerau_levenshtein_recursive_cache_time(dam_lev_rec_cache_time):
    lengths = [i for i in range(0, 200, 20)]
    
    fig = plt.figure(figsize=(7, 5))
    plot = fig.add_subplot()
    plot.plot(lengths, dam_lev_rec_cache_time, label = "Дамерау-Левенштейн (с кэшем)")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина, символы")

    plt.show()


def matrix_time(lev_time, dam_lev_time, dam_lev_rec_cache_time):
    lengths = [i for i in range(0, 200, 20)]
    
    fig = plt.figure(figsize=(7, 5))
    plot = fig.add_subplot()

    plot.plot(lengths, lev_time, label = "Левенштейн")
    plot.plot(lengths, dam_lev_time, label = "Дамерау-Левенштейн")
    plot.plot(lengths, dam_lev_rec_cache_time, label = "Дамерау-Левенштейн (с кэшем)")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина, символы")

    plt.show()
    

def test_time_memory():
    lev_time = []
    dam_lev_time = []
    dam_lev_rec_time = []
    dam_lev_rec_cache_time = []
    
    for i in range(10):
        lev_time.append(get_time(levenshtein_distance, i * 20))
        dam_lev_time.append(get_time(damerau_levenshtein_distance, i * 20))
        dam_lev_rec_time.append(get_time(damerau_levenshtein_distance_recursive, i))
        dam_lev_rec_cache_time.append(get_time(damerau_levenshtein_distance_recursive_cache, i * 20))
        print("Выполнено", i + 1, "/ 10 замеров\n")
        
    print("ТАБЛИЦА ДЛЯ АЛГОРИТМОВ ЛЕВЕНШТЕЙНА, ДАМЕРАУ-ЛЕВЕНШТЕЙНА, ДАМЕРАУ-ЛЕВЕНШТЕЙНА (С КЭШЕМ)")
    print(" %3s | %12s | %12s | %12s\n" %("i", "Лев", "Дам-Лев", "Дам-Лев (кэш)"))
    for i in range(10):
        print(" %3d | %12f | %12f | %12f\n" %(i * 20, 0, dam_lev_time[i] * 1000, 0))
    
    print("\n")
    print("ТАБЛИЦА ДЛЯ АЛГОРИТМА ДАМЕРАУ-ЛЕВЕНШТЕЙНА (РЕКУРСИВНО)")
    print(" %3s | %12s\n" %("i", "Дам-Лев (рек)"))
    for i in range(10):
        print(" %3d | %12f\n" %(i, dam_lev_rec_time[i] * 1000))        
    
        
    levenshtein_graph(lev_time)
    damerau_levenshtein_graph(dam_lev_time)
    damerau_levenshtein_recursive_time(dam_lev_rec_time)
    damerau_levenshtein_recursive_cache_time(dam_lev_rec_cache_time)
    matrix_time(lev_time, dam_lev_time, dam_lev_rec_cache_time)