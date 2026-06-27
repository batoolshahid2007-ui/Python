# A* Pathfinding Visualizer Game

This project is a 2D grid-based visualizer that demonstrates the **A\* (A-Star) Pathfinding Algorithm** in action. It simulates an AI or a game character finding the shortest possible route through a maze from a starting position to a specific destination.

---

## 🕹️ What is Inside the Project?

The project consists of a **10x10 Grid Game Board** built using Pygame where an automated agent solves a pathfinding puzzle. Inside the game, you will see:

* 🔴 **Start Node (Red Circle):** The starting point of the agent, located at the bottom-left corner `(9, 0)`.
* 🟡 **Goal Node (Yellow Circle):** The target destination, located at the top-right corner `(0, 9)`.
* ⬛ **Obstacles / Walls (Black Blocks):** A pre-defined fixed maze or barrier system that blocks the path. The agent cannot pass through these blocks.
* 🟦 **Walkable Space (Blue Grid):** The open area where the agent is allowed to move (Up, Down, Left, Right).
* 🟢 **The Shortest Path (Green Circles):** The final, most optimized route calculated by the algorithm to reach the goal instantly.

---

## 🧠 How the Game Logic Works

Instead of randomly guessing the way, the game uses intelligence to solve the maze:

1. **The Grid Initialization:** A `10x10` coordinate system is generated, and specific coordinates are locked as solid walls (`1` in the backend matrix).
2. **Heuristic Calculation:** The game uses **Manhattan Distance** ($|x_1 - x_2| + |y_1 - y_2|$) to calculate how far any given block is from the final goal.
3. **Smart Decision Making:** Using a Priority Queue (`heapq`), the algorithm constantly evaluates which neighboring block has the lowest total cost ($f = g + h$), ensuring it never takes unnecessary steps.
4. **Path Reinterpretation:** Once the goal is successfully reached, the algorithm traces its steps backward, connects the dots, and draws the final **Green Path** on the screen.

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.x
* **Core Library:** `pygame` (For rendering the game window and graphics)
* **Data Structure:** `heapq` (For managing the priority queue efficiently)

---

## 🚀 How to Run

1. Install Pygame:
   ```bash
   pip install pygame
