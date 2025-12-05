import tkinter as tk
from tkinter import messagebox, simpledialog
import heapq
import time
import random

# ------------------------------
# AI COMPONENT 1: Heuristic Function
# ------------------------------
# The Manhattan Distance heuristic helps the search algorithm decide
# which cell is *most promising* to explore next.
# This is a core concept of AI (Informed Search).
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# ------------------------------
# AI COMPONENT 2: Best-First Search Algorithm
# ------------------------------
# This is an AI search algorithm used in Robotics, Navigation, and Game AI.
# It uses the heuristic to intelligently choose the next best move.
def best_first_search(grid, start, goal, canvas, rects, cell_size, animate=False):

    # Priority Queue → explores BEST cell first (AI decision-making)
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), start))

    visited = set()
    parent = {start: None}

    while pq:
        _, current = heapq.heappop(pq)

        # Goal Reached → AI achieved optimal navigation
        if current == goal:
            return reconstruct_path(goal, parent)

        visited.add(current)

        # Visualization of AI search progress
        if animate:
            r, c = current
            if current != start and current != goal:
                canvas.itemconfig(rects[r][c], fill="lightblue")
                canvas.update()
                time.sleep(0.05)

        # Explore neighboring cells (Up, Down, Left, Right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

            nr, nc = current[0] + dr, current[1] + dc
            neighbor = (nr, nc)

            # Skip invalid or blocked cells
            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and
                grid[nr][nc] != 1 and
                neighbor not in visited and
                neighbor not in parent):

                # AI uses heuristic to prioritize neighbors closer to goal
                heapq.heappush(pq, (heuristic(neighbor, goal), neighbor))

                # Track movement for path reconstruction
                parent[neighbor] = current

    return None

# ------------------------------
# AI COMPONENT 3: Path Reconstruction
# ------------------------------
# Once the goal is found, AI reconstructs the final optimal path.
def reconstruct_path(goal, parent):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    return path[::-1]

# ------------------------------
# GUI (User Interface)
# ------------------------------
class PathPlanningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Robot Path Planning - Best First Search")

        self.cell_size = 40
        self.rows = simpledialog.askinteger("Input", "Enter number of rows:", minvalue=5, maxvalue=30)
        self.cols = simpledialog.askinteger("Input", "Enter number of columns:", minvalue=5, maxvalue=30)

        self.canvas = tk.Canvas(root, width=self.cols * self.cell_size, height=self.rows * self.cell_size)
        self.canvas.pack()

        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.rects = [[None for _ in range(self.cols)] for _ in range(self.rows)]

        self.start = None
        self.goal = None

        self.canvas.bind("<Button-1>", self.on_click)
        self.mode = "obstacle"

        self.build_buttons()
        self.draw_grid()
        self.place_initial_obstacles(count=30)

    def build_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Button(frame, text="Set Start", command=self.set_start_mode).pack(side=tk.LEFT)
        tk.Button(frame, text="Set Goal", command=self.set_goal_mode).pack(side=tk.LEFT)
        tk.Button(frame, text="Set Obstacle", command=self.set_obstacle_mode).pack(side=tk.LEFT)
        tk.Button(frame, text="Run Search", command=self.run_search).pack(side=tk.LEFT)
        tk.Button(frame, text="Reset", command=self.reset).pack(side=tk.LEFT)

    def draw_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                x1, y1 = c * self.cell_size, r * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="gray")
                self.rects[r][c] = rect

    def place_initial_obstacles(self, count=30):
        placed = 0
        while placed < count:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if self.grid[r][c] == 0:
                self.grid[r][c] = 1
                self.canvas.itemconfig(self.rects[r][c], fill="black")
                placed += 1

    def on_click(self, event):
        row = event.y // self.cell_size
        col = event.x // self.cell_size

        if row >= self.rows or col >= self.cols:
            return

        if self.mode == "start":
            if self.start:
                old_r, old_c = self.start
                self.canvas.itemconfig(self.rects[old_r][old_c], fill="white")
            self.start = (row, col)
            self.canvas.itemconfig(self.rects[row][col], fill="green")

        elif self.mode == "goal":
            if self.goal:
                old_r, old_c = self.goal
                self.canvas.itemconfig(self.rects[old_r][old_c], fill="white")
            self.goal = (row, col)
            self.canvas.itemconfig(self.rects[row][col], fill="red")

        elif self.mode == "obstacle":
            if self.grid[row][col] == 0:
                self.grid[row][col] = 1
                self.canvas.itemconfig(self.rects[row][col], fill="black")

    def set_start_mode(self):
        self.mode = "start"

    def set_goal_mode(self):
        self.mode = "goal"

    def set_obstacle_mode(self):
        self.mode = "obstacle"

    def run_search(self):
        if not self.start or not self.goal:
            messagebox.showwarning("Warning", "Please set both start and goal.")
            return

        # Reset obstacle cells visually
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 1:
                    self.canvas.itemconfig(self.rects[r][c], fill="black")

        # ------------------------------
        # AI CALL: Run Best-First Search
        # ------------------------------
        path = best_first_search(self.grid, self.start, self.goal, self.canvas, self.rects, self.cell_size, animate=True)

        if path:
            for (r, c) in path:
                if (r, c) != self.start and (r, c) != self.goal:
                    self.canvas.itemconfig(self.rects[r][c], fill="yellow")
            messagebox.showinfo("Path Found", f"Path length: {len(path)} steps.")
        else:
            messagebox.showinfo("No Path", "No path found to the goal.")

    def reset(self):
        self.canvas.delete("all")
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.rects = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.start = None
        self.goal = None
        self.draw_grid()
        self.place_initial_obstacles(count=30)


# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = PathPlanningApp(root)
    root.mainloop()
