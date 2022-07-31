"""
This programs gives you the shortest distance from one node to the another
"""


# define a function for the main
def way(graph, start, end):
    explored = []
    queue = [[start]]
    # check if the destination node is reached
    if start == end:
        print("True")
        return
    while queue:
        path = queue.pop(0)  # pop removes the [i] element from the stack
        node = path[-1]
        # current node is not visited
        if node not in explored:
            side_nodes = graph[node]
            # iterate over the side_node of the current_node
            for side_node in side_nodes:
                new_path = list(path)
                new_path.append(side_node)
                queue.append(new_path)
                # check if the side_node is the end point then route found (True)
                if side_node == end:
                    print("True = ", *new_path)
                    return
            explored.append(node)
    # if no route found
    print("False")
    return


# main
if __name__ == "__main__":
    # define the parent node and the side_node
    graph = {'A': ['B'],  # 'parent node' : [side_nodes]
             'B': ['A', 'D', 'E', 'C'],
             'C': ['E', 'D', 'B'],
             'D': ['B', 'E', 'C'],
             'E': ['B', 'D', 'C'],
             }

    way(graph, 'A', 'E')  # ----> True (A B E)
    way(graph, 'A', 'G')  # ----> False
