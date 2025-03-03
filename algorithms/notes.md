# Revision time....


## Generating subsets recursively

For each item, can include or don't include

Ideas about subset
1. Generate recursively
2. For each number, the subsets is all the subsets x (include or don't include)
3. Time complexity is 2^N * N, (two choices) x (two choices) x .... n times 

## Permutations

For n choices, keep track if they are chosen

Pick 1 as first choice, mark as chosen. then recurse to pick the restw

Time complexity: N! since N choices x N-1 x N-2 ... 1


TODO : next permutation given n


## N queens

Try to place at each row, for each row, try all columns




## Bit operations

Set, toggle, flip kth bit

Representing sets using n bit integer whose one bit indicate which element belongs to subset

Efficient way to represent sets



# DP


## Longest increasing subsequence

Maximum length of sequence and each element in seq is larger than previous element

Let LIS(k) be LIS of subsequence ending at index k

Calculate all values from 0 to n-1 for k

Can optimise using binary search and modifying lists to swap out second larger value





# Graphs


## Terminology

A graph consist of nodes (vertices) that are connected with edges. 

A path leads from one node to another node through the edges of the graph.

Length of a path: number of edges in it.

A cycle is a path where first and last node is the same.

A graph is connected if there is a path between any two nodes.

Connected part of a graph is called components.

A tree is a connected graph with no cycles.

In a directed graph, edges can be traverse in one direction only.

Weighted graph edges is assigned a weight.

Two nodes are neighours if there is an edge between them. Degree of a node is number of its neighbours.

Sum of degrees is always 2m. Regular graph if every node has constant degree. Complete graph if degree of every node is n-1.

Bipartite graph if it does not have a cycle with odd number of edges.

Graph representations
1. Adjacency list. Each node is assigned an adjacency list to which there is an edge from x. 
2. Adjacency matrix. adj(a, b) indicates if there's an edge from node a to node b
3. edge list. All edges in some order list<pair<int, int>>


Fundamental graph algorithms
1. DFS (nodes + edges)
2. BFS


## Bellman Ford algorithm

Finds shortest paths from starting node to all nodes. All kinds of graph ok except cycle with negative length. 

The algorithm keeps track of distances from starting node to all nodes of the graph. Initially it's 0 and distance to other node is infinity. Then it reduces distances by finding edges that shorten paths.

Time complexity: n-1 rounds x m edges

By running an additional cycle and checking if distance shorterns, can detect negative cycle.

## Dijkstra

Finds shortest path to all nodes. Algorithm requires no negative weight edges.

Maintains distances to nodes and relaxes/reduces them each cycle. Select a node that is not processed and distance is smallest. Goes through all the nodes that start with it and reduces edges.

Processes each edge once


Time complexity: N + M log M
Goes through all the nodes, add each edge to PQ once and pop it.


## Floyd-Warshall

Finds shortest path between all pairs using a matrix distance


# Directed acyclic graphs

Such graphs do not contain cycles. Construct topological sort and apply DP

## Topological sort

Ordering of the nodes in directed graph s.t if there is a path from node a to node, node a appears before node b in ordering

If there's a cycle, cannot have topo sort. DFS can check cycle and construct topological sort.

Run DFS. Each node has a state: not processed, processing, and processed. If we encounter a node that is processing, this is a back edge and also cycle

To get topological list, add nodes to list when state is processed. Reverse it


