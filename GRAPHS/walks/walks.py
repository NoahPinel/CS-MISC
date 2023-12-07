# Matt Damon solves a few blackboard problems
# in the movie "Good Will Hunting", this code
# solves the first few question of one of the
# "challenging" problems that he magically solves.
# 
# The full question is:
#     1) Find the adjacency matrix A of the graph G
#     2) Find the matrix giving the number of 3 step walks in G.
#     3) Find the generating function for walks from point i to j.
#     4) Find the generating function for walks from points 1 to 3.
# 
# I will solve 1 and 2 here.
# 
# 1) To solve this, simply just find the A_adj, that is,
# encode the graph G as a matrix A, this is done by following
# 
# an entry A_{i,j} is = k, if there are k edges between the vertices
# i and j.
# 
# 2) To solve this, we use the cool fact that with A_adj, we can actually
# raise A_adj ^ n, where n is the step walk size, and the resulting matrix
# is exactly what we want, the encoding of all possible paths of length n!!!
#     
#     A^n(i,j) = # of walks of length n from i --> j
#
#    The Graph G:
#                  (4)
#                  / \ 
#                 /   \
#                /     \
#               /       \
#              /         \
#             /           \
#            /             \   
#           /               \  
#          /                 \ 
#         /                   \ /---------------\
#        (1) --------------- (2)                (3)
#                               \---------------/ 
###
import sys
import numpy as np
from numpy.linalg import matrix_power

def blank_mat(n):
    return np.zeros((n, n))

def build_adj(edges, n):
    A = blank_mat(n)
    for edge in edges:
        i, j = edge
        #print("[{}][{}]".format(i,j))
        A[i, j] += 1
        A[j, i] += 1
        #print(A) 
    return A

def parse_graph(file):
    with open(file, 'r') as f:
        V = np.array(f.readline().strip().split(', '), dtype=int)
        E = np.array([line.strip().split(', ') for line in f], dtype=int)
    return {"vertices": V, "edges": E}

def main():
    if len(sys.argv) > 1:
        try:
            walk = int(sys.argv[1])
        except ValueError:
            print(f"Error: '{sys.argv[1]}' is not a valid integer walk!!!")
            exit(1)
    else:
        print("Error: Please provide an integer (walk length)")
        print("Usage: python walks.py <walk_length>")
        exit(1)
    
    # G:=
    G = parse_graph("matrices.txt")
    #print("Vertices:", G["vertices"])
    #print("Edges:", G["edges"])
    
    # A_adj :=
    ADJ = build_adj(G["edges"], len(G["vertices"]))
    print("SOLUTION FOR (1):")
    print("A_adj:=\n {} ".format(ADJ))
    
    # Get walk of length n
    walk_mat = matrix_power(ADJ, walk)
    print("\nSOLUTION FOR (2):")
    print("A_adj^{}:=\n {} ".format(walk, walk_mat))

if __name__ == "__main__":
    main()
