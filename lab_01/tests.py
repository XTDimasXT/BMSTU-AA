import matplotlib.pyplot as plt

from algorithms import *
from functions import *


def levenshtein_graph(lev_time):
    lengths = [i for i in range(10)]
    
    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(lengths, lev_time, "g:", label = "Левенштейн")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина, символы")

    plt.show()
    
    
def damerau_levenshtein_graph(dam_lev_time):
    lengths = [i for i in range(10)]
    
    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(lengths, dam_lev_time, "g:", label = "Дамерау-Левенштейн")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина, символы")

    plt.show()
    
    
def damerau_levenshtein_recursive_time(dam_lev_rec_time):
    lengths = [i for i in range(10)]
    
    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(lengths, dam_lev_rec_time, "g:", label = "Дамерау-Левенштейн (рекурсивно)")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Длина, символы")

    plt.show()
    

def damerau_levenshtein_recursive_cache_time(dam_lev_rec_cache_time):
    lengths = [i for i in range(10)]
    
    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(lengths, dam_lev_rec_cache_time, "g:", label = "Дамерау-Левенштейн (с кэшем)")

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
        lev_time.append(get_time(levenshtein_distance, i))
        dam_lev_time.append(get_time(damerau_levenshtein_distance, i))
        dam_lev_rec_time.append(get_time(damerau_levenshtein_distance_recursive, i))
        dam_lev_rec_cache_time.append(get_time(damerau_levenshtein_distance_recursive_cache, i))
        print("size", i, "has been ended\n")
        
    for i in range(10):
        print(" %1d | %.4f | %.4f | %.4f | %.4f\n" %(i, lev_time[i], dam_lev_time[i], dam_lev_rec_time[i], dam_lev_rec_cache_time[i]))
        
    levenshtein_graph(lev_time)
    damerau_levenshtein_graph(dam_lev_time)
    damerau_levenshtein_recursive_time(dam_lev_rec_time)
    damerau_levenshtein_recursive_cache_time(dam_lev_rec_cache_time)