############################################################################

# Created by: Prof. Valdecy Pereira, D.Sc.
# UFF - Universidade Federal Fluminense (Brazil)
# email:  valdecy.pereira@gmail.com
# Course: Metaheuristics
# Lesson: Variable Neighborhood Search

# Citation: 
# PEREIRA, V. (2018). Project: Metaheuristic-Local_Search-Variable_Neighborhood_Search, File: Python-MH-Local Search-Variable Neighborhood Search.py, GitHub repository: <https://github.com/Valdecy/Metaheuristic-Local_Search-Variable_Neighborhood_Search>

############################################################################

# Required Libraries
import pandas as pd
import random
import copy

# Function: Distance
def distance_calc(Xdata, route):
    distance = 0
    for k in range(0, len(route[0])-1):
        m = k + 1
        distance = distance + Xdata.iloc[route[0][k]-1, route[0][m]-1]            
    return distance

# Function: Stochastic 2_opt
def stochastic_2_opt(Xdata, city_tour):
    best_route = copy.deepcopy(city_tour)      
    i, j  = random.sample(range(0, len(city_tour[0])-1), 2)
    if (i > j):
        i, j = j, i
    best_route[0][i:j+1] = list(reversed(best_route[0][i:j+1]))           
    best_route[0][-1]  = best_route[0][0]              
    best_route[1] = distance_calc(Xdata, route = best_route)                     
    return best_route

# Function: Local Search
def local_search(Xdata, city_tour, max_attempts = 50, neighbourhood_size = 5):
    count = 0
    solution = copy.deepcopy(city_tour) 
    while (count < max_attempts): 
        for i in range(0, neighbourhood_size):
            candidate = stochastic_2_opt(Xdata, city_tour = solution)
        if candidate[1] < solution[1]:
            solution  = copy.deepcopy(candidate)
            count = 0
        else:
            count = count + 1                             
    return solution 

# Function: Variable Neighborhood Search
def variable_neighborhood_search(Xdata, city_tour, max_attempts = 20, neighbourhood_size = 5, iterations = 50):
    count = 0
    solution = copy.deepcopy(city_tour)
    best_solution = copy.deepcopy(city_tour)
    while (count < iterations):
        for i in range(0, neighbourhood_size):
            for j in range(0, neighbourhood_size):
                solution = stochastic_2_opt(Xdata, city_tour = best_solution)
            solution = local_search(Xdata, city_tour = solution, max_attempts = max_attempts, neighbourhood_size = neighbourhood_size )
            if (solution[1] < best_solution[1]):
                best_solution = copy.deepcopy(solution) 
                break
        count = count + 1
        print("Iteration = ", count, "->", best_solution)
    return best_solution

######################## Part 1 - Usage ####################################

X = pd.read_csv('Python-MH-Local Search-Variable Neighborhood Search-Dataset-01.txt', sep = '\t') #17 cities = 2085

cities = [[   1,  2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,   1   ], 4722]
lsvns = variable_neighborhood_search(X, city_tour = cities, max_attempts = 25, neighbourhood_size = 5, iterations = 1000)
