from heapq import heappop, heappush

def astar(graph, start, goal, heuristic):
    open_list = [(0, start, [])]  # Priority queue with (f(n), current node, path)
    close_set = set()  # Set to keep track of visited nodes

    while open_list:
        _, current, path = heappop(open_list)

        if current in close_set:
            continue  # Skip this iteration if the node is already visited

        close_set.add(current)  # Mark the current node as visited
        path = path + [current]  # Add the current node to the path

        if current == goal:
            return path  # Goal reached, return the optimized path

        for neighbor, cost in graph[current].items():
            if neighbor not in close_set:
                # Calculate the priority and add the neighbor to the open list
                heappush(open_list, (heuristic[neighbor] + cost, neighbor, path))

    return None  # No path found

# Example usage:
graph = {
    "A": {"B": 9, "C": 4, "D": 7},
    "B": {"E": 11},
    "C": {"E": 17, "F": 12},
    "D": {"F": 14},
    "E": {"Z": 5},
    "F": {"Z": 9},
}

heuristic = {"A": 21, "B": 14, "C": 18, "D": 18, "E": 5, "F": 8, "Z": 0}

start_node = "A"
goal_node = "Z"

result_path = astar(graph, start_node, goal_node, heuristic)

if result_path:
    print(f"Optimized path from {start_node} to {goal_node}: {result_path}")
    print(f"Total distance: {sum(graph[result_path[i]][result_path[i+1]] for i in range(len(result_path)-1))}")
else:
    print(f"No path found from {start_node} to {goal_node}")