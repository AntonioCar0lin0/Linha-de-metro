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
import heapq
from data_loader import data_nodes

# Example of the Data:
example = {
    "A": {"B": 4, "C": 6},
    "B": {"A": 4, "C": 1, "D": 11},
    "C": {"A": 4, "B": 1, "D": 10},
    "D": {"B": 11, "C": 10, "E": 7, "F": 2},
    "E": {"D": 7, "F": 1, "G": 3},
    "F": {"D": 2, "E": 1, "G": 4},
    "G": {"E": 3, "F": 4}
}


# creates a dictionary of every cost of travelling to a node and it's predecessor, from a inicial_node
def organize_path(initial_node = str, dataset = {}):
    min_cost_and_predecessor = {key: (0 if key == initial_node else float('inf'), None) for key in dataset.keys()} # Dict for all predecessor's and all respectually costs

    priority_list = [(0, initial_node)]
    heapq.heapify(priority_list) # a priority list to keep the lowest node cost in the top 

    visited = [] # a list to mark all nodes that were already "tested"

    while priority_list:
        current_node_cost, current_node = heapq.heappop(priority_list) # remove the top of the priority list and keep it's cost and itself
    
        if current_node in visited:
            continue

        visited.append(current_node) 

        for neighbor, cost in dataset[current_node].items():
            new_cost = current_node_cost + cost # cost to travel to that neighbor from our current node

            if new_cost < min_cost_and_predecessor[neighbor][0]:
                min_cost_and_predecessor[neighbor] = (new_cost, current_node)

                # if the neighbor wasn't visited yet, 
                if neighbor not in visited:
                    heapq.heappush(priority_list, (new_cost, neighbor))


    return min_cost_and_predecessor


# returns a itinerary of the fasttest travel from startin_node to final_node
def organize_itinerary(organized_dict = {}, starting_node = str, final_node = str):
    itinerary = [final_node] 
    current_node = final_node # start from the end

    while current_node != starting_node:
        _, predecessor = organized_dict[current_node] # takes the predecessor 

        itinerary.append(predecessor) 
        current_node = predecessor # atualize the node
    
    itinerary.reverse() # inverse the list for correct viewring

    return itinerary
  


print(organize_path("Rithala", data_nodes))
print(organize_itinerary(organize_path("Rithala", data_nodes), "Rithala", "Kashmere Gate"))