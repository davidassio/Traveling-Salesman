# Traveling-Salesman

This project is an implementation of a branch and bound depth
first search using a nearest neighbor heuristic and a
stochastic local search using a hill climbing method to
solve the Traveling Salesman Problem.

## How to generate a TSP

Open the "generate_travelling_salesman_problem.py" file and run it.
Input your desired number of cities. Next enter a number for mean and
standard deviation. This will give you a matrix of distances based on
the inputted mean and deviation.

## Instructions to run the algorithms

In the files "bnb_dfs_2.0.py" and "sls.py" are a variable called
"filename" and "file_path," respectively. Both are set to "input_file".
Replace "input_file" with a TSP that you have generated.
"5_0.0_1.0.out" is already included for ease of access and can be
used as an input.
