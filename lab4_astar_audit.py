import heapq

# Given graph
graph = {"S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []}

# Given heuristic values
heuristic = { "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0}


def search(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    processed = []
    expanded = []

    while pq:
        f, g, node, path = heapq.heappop(pq)

        # Ignore outdated entries
        if g != best.get(node):
            continue

        processed.append(node)

        if node == goal:
            return g, path, processed, expanded

        expanded.append(node)

        for next_node, cost in graph.get(node, []):
            new_g = g + cost

            if new_g < best.get(next_node, float("inf")):
                best[next_node] = new_g
                new_f = new_g + h[next_node]

                heapq.heappush(
                    pq,
                    (new_f, new_g, next_node, path + [next_node])
                )

    return None, [], processed, expanded


def run_test(title, h, test_graph, start="S", goal="G"):
    print("\n", title)

    cost, path, processed, expanded = search(
        test_graph, h, start, goal
    )

    print("Path:", " -> ".join(path) if path else "No path found")
    print("Returned cost:", cost)

    # Independently calculate the path cost
    total = 0
    for u, v in zip(path, path[1:]):
        for next_node, weight in test_graph[u]:
            if next_node == v:
                total += weight
                break

    print("Independently summed cost:", total if path else "N/A")
    print("Processed-node trace:", processed)
    print("Expanded nodes:", expanded)
    print("Expansion count:", len(expanded))


# Task 2: A* Search
run_test("A* SEARCH", heuristic, graph)

# Task 2: Uniform Cost Search
zero_h = {node: 0 for node in graph}
run_test("UCS SEARCH", zero_h, graph)

# Task 3: Overestimate h(C)
bad_h = heuristic.copy()
bad_h["C"] = 10
run_test("A* WITH OVERESTIMATED h(C)", bad_h, graph)

# Edge-case test: Goal is unreachable
test_graph = {
    "S": [("A", 1)],
    "A": [],
    "G": []}

test_h = {"S": 0, "A": 0, "G": 0}

run_test(
    "EDGE CASE: UNREACHABLE GOAL",
    test_h,
    test_graph)
