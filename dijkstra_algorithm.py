import sys
import heapq

"""
# Dataset Model
Each station has adjacent nodes and associated traversal costs.

To optimize, use an integer index hash map for each station:
##### A dictionary of 
    {
    'station1' = 001,
    'station2' = 002,
    ...
    }

Use these indices in the main dataset dictionary instead of strings as keys -->

Dictionary{
    'station1': {'node': value, 'node': value, ...},
    'station2': {'node': value, 'node': value, ...},
    'station3': {'node': value, 'node': value, ...},
    'station4': {'node': value, 'node': value, ...},
    'station5': {'node': value, 'node': value, ...},
    ...
}

Once the dataset is prepared, the graph can be visualized using matplotlib, PyQt, Tkinter, or any other GUI framework. Next, implement the optimal path search function using Dijkstra's algorithm:

THE PRINCIPLE OF DIJKSTRA'S ALGORITHM:  
    1. Initialize all nodes with an infinite value (using `sys.maxsize`). Each node also stores its traversal cost.
    2. Choose a starting node and set its value to 0.
    3. Maintain a dictionary to track each node's predecessor and the cumulative cost to reach it.
    4. Explore each path from the current node to its neighbors. Update their predecessors and calculate the total cost to reach each neighbor.
    5. Use a set to track visited nodes to avoid redundant checks.
    6. Use a priority queue (implemented with heapq) where nodes with lower cumulative costs are given higher priority.
    7. Repeat until all nodes are processed. Identify the destination node and its total traversal cost. Use the predecessor dictionary to trace back the path and construct the route.
"""