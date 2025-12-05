AI Path Planning with Best-First Search
📝 Project Overview

This project implements a robot path planning system using the Best-First Search (BFS) algorithm, a classical AI search technique. It allows a robot to navigate efficiently in grid-based environments while avoiding obstacles. The system leverages a heuristic function (Manhattan Distance) to intelligently guide the search toward the goal, demonstrating practical AI principles in robotics.

The project also features a graphical user interface (GUI) using Tkinter, enabling users to:

Dynamically create maps with obstacles

Set start and goal positions

Visualize the pathfinding process in real-time

🎯 Problem Statement

Design and implement a path planning system where a robot can intelligently navigate from a start position to a goal in a grid-based environment, avoiding obstacles and dynamically displaying the search and final path. The system should incorporate AI techniques for efficient decision-making.

🛠 Project Objectives

Implement the Best-First Search algorithm for robot navigation.

Incorporate a heuristic function (Manhattan Distance) to guide the search.

Develop a user-friendly GUI for map creation, obstacle placement, and visualization.

Allow users to set start and goal positions and reset the environment.

Visualize the search process and final path dynamically.

💻 Features

AI Search: Best-First Search with heuristic-based decision-making

Dynamic Visualization: Light blue cells for search exploration, yellow for the final path

Interactive GUI: Set start (green), goal (red), and obstacles (black)

Random Obstacles: Generate random obstacles for different test cases

Path Metrics: Display total steps in the computed path

🧩 Methodology

Grid & Dataset Setup

User inputs grid size (rows x columns)

Cells are marked as navigable (0) or obstacle (1)

Input Validation

Ensures start/goal positions are valid and not on obstacles

Heuristic Design

Manhattan Distance guides BFS toward the goal efficiently

Best-First Search Algorithm

Priority queue (min-heap) selects the next most promising cell

Tracks visited cells and parent nodes to reconstruct the path

Visualization & Output

Start (green), Goal (red), Obstacles (black), Explored cells (light blue), Final path (yellow)

Displays total steps

Testing & Validation

Open grids (no obstacles)

Complex grids with multiple obstacles

Edge cases where no path exists

🧑‍💻 How to Run

Clone the repository:

git clone https://github.com/mangeshtate/AI-Path-Planning-Best-First-Search.git
cd AI-Path-Planning-Best-First-Search


Install dependencies (Tkinter is included in most Python distributions):

pip install tk


Run the program:

python path_planning.py


Follow the GUI instructions:

Set Start, Goal, and Obstacles

Click Run Search to visualize pathfinding

🖼 Screenshots

![Screenshot1](Screenshots/Screenshot\ 2025-12-05\ 150538.png)
![Screenshot2](Screenshots/Screenshot\ 2025-12-05\ 150621.png)
![Screenshot3](Screenshots/Screenshot\ 2025-12-05\ 150743.png)

📂 Project Files
AI-Path-Planning-Best-First-Search/
│── path_planning.py           # Main Python code
│── README.md                  # Project README
│── Project Report.docx        # Detailed project workflow
│── Screenshots/               # Screenshots of GUI and output

📝 Project Report

For a detailed description of the workflow, methodology, and code explanation, see the Project Report:

Project Report.docx

⚡ Future Enhancements

Dynamic obstacle handling

Diagonal movement support

Cost-based heuristics for weighted paths

Integration with real-world robotics platforms

📚 References

[Artificial Intelligence: A Modern Approach – Russell & Norvig]

Tkinter Documentation: https://docs.python.org/3/library/tkinter.html

Python heapq Documentation: https://docs.python.org/3/library/heapq.html
