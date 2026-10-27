# Lab 4: A* Search Audit

## Introduction
This lab implements and tests the A* search algorithm and compares its results with Uniform Cost Search (UCS).

## Files Included
- `lab4_astar_audit.py` — Main Python file for the lab tasks.
- `README.md` — Instructions for setting up and running the project.
- `outputs/` — Captured outputs or trace files, if included.

## Requirements
- Python 3
- Visual Studio Code (VS Code)

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal by selecting **Terminal → New Terminal**.
4. Run the Python file using this command:

```bash
python lab4_astar_audit.py
```

##Tests Performed
- Run A* search on the given graph.
- Compare A* with UCS using a heuristic of zero.
- Test a modified heuristic.
- Test an unreachable goal.

## Expected Results
- A* and UCS with a zero heuristic should find the same minimum-cost path.
- The modified heuristic is used to examine how heuristic values affect A*.
- The unreachable-goal test checks whether the algorithms handle failure correctly.

## Conclusion
This lab provides practical experience with A* search, Uniform Cost Search, heuristic values, and testing search algorithms.

## Author
AI Student