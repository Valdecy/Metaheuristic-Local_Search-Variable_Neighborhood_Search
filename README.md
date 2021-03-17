# Metaheuristic-Local_Search-Variable_Neighborhood_Search
Variable Neighborhood Search Function for TSP problems. The function returns: 1) A list with the order of the cities to visit, and the total distance for visiting this same list order.

* X = Distance Matrix.

* buid_distance_matrix (HELPER FUNCTION) = Tranforms coordinates in a distance matrix (euclidean distance).

* city_tour = Initial list of visitation.

* seed (HELPER FUNCTION) = Generates a random list of visitation.

* iterations = Total number of iterations. The Default Value is 5.

* neighbourhood_size = Population size. The Default Value is 5.

* max_attempts = Max number of attempts to improve solution before changing the neighborhood. The Default Value is 20.

* plot_tour_distance_matrix (HELPER FUNCTION) = A projection is generated based on the distance matrix. The estimated projection may present a plot with path crosses, even for the 2-opt optimal solution (Red Point = Initial city; Orange Point = Second City).

* plot_tour_coordinates (HELPER FUNCTION) = Plots the 2-opt optimal solution (Red Point = Initial city; Orange Point = Second City).

# Other Metaheuristics

Try online in the **Colab**  my new library - [pyCombinatorial](https://github.com/Valdecy/pyCombinatorial).

- 2-opt ([ Colab Demo ](https://colab.research.google.com/drive/1SLkM8r_VdlFCpNpm-2yTfr_ynSC5WIX9?usp=sharing))
- 2-opt Stochastic([ Colab Demo ](https://colab.research.google.com/drive/1xTm__7OwQVC_KX2b-eExLGgG1DgnJ10a?usp=sharing))
- 3-opt ([ Colab Demo ](https://colab.research.google.com/drive/1iAZLawLBZ-7yaPCyobMtel1SvBamxtjL?usp=sharing))
- 4-opt ([ Colab Demo ](https://colab.research.google.com/drive/1N8HKhVY4s20sfqo8IWIaCY-NHVk6gARS?usp=sharing))
- Ant Colony Optimization ([ Colab Demo ](https://colab.research.google.com/drive/1O2qogrjE4mZUZX3nsSxw43crumlBnd-D?usp=sharing))
- Extremal Optimization ([ Colab Demo ](https://colab.research.google.com/drive/1Y5YH0eYKjr1nj_IfhJXaILRDIXm-LWLs?usp=sharing))
- GRASP ([ Colab Demo ](https://colab.research.google.com/drive/1OnRyCc6C_QL6wr6-l5RlQI4eGbMdwuhS?usp=sharing))
- Guided Search ([ Colab Demo ](https://colab.research.google.com/drive/1uT9mlDoo37Ni7hqziGNELEGQCGBKQ83o?usp=sharing))
- Iterated Search ([ Colab Demo ](https://colab.research.google.com/drive/1U3sPpknulwsCUQq9mK7Ywfb8ap2GIXZv?usp=sharing))
- Scatter Search ([ Colab Demo ](https://colab.research.google.com/drive/115Ql6KegvOjlNUUfsbY4fA8Vab-db26N?usp=sharing))
- Stochastic Hill Climbing ([ Colab Demo ](https://colab.research.google.com/drive/1_wP6vg4JoRHGItGxEtXcf9Y9OuuoDlDl?usp=sharing))
- Tabu Search ([ Colab Demo ](https://colab.research.google.com/drive/1SRwQrBaxkKk18SDvQPy--0yNRWdl6Y1G?usp=sharing))
- Variable Neighborhood Search ([ Colab Demo ](https://colab.research.google.com/drive/1yMWjYuurzpcijsCFDTA76fAwJmSaDkZq?usp=sharing))
