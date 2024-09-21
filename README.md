
# Berkeley CS188: Pacman Search Project

This repository contains the solution to **Project 1: Search in Pacman**, from the UC Berkeley CS188 Intro to AI course. In this project, we implement a variety of search algorithms to help Pacman navigate mazes, collect food efficiently, and solve different search-based problems.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Algorithms Implemented](#algorithms-implemented)
  - [1. Depth First Search (DFS)](#1-depth-first-search-dfs)
  - [2. Breadth First Search (BFS)](#2-breadth-first-search-bfs)
  - [3. Uniform Cost Search (UCS)](#3-uniform-cost-search-ucs)
  - [4. A* Search](#4-a-search)
- [Heuristics Implemented](#heuristics-implemented)
  - [1. Corners Problem Heuristic](#1-corners-problem-heuristic)
  - [2. Food Search Heuristic](#2-food-search-heuristic)
- [How to Run the Project](#how-to-run-the-project)

## Introduction
This project introduces basic search algorithms applied to a Pacman agent that must navigate mazes efficiently. The goal is to implement different search strategies and use them to solve increasingly complex problems in a grid world.

Pacman is a simple agent that can move in four directions (north, south, east, west), and your task is to guide him to reach his goal by searching through different paths.

## Project Structure
The codebase for this project consists of the following Python files:
- `search.py`: Contains implementations of the search algorithms.
- `searchAgents.py`: Contains search-based agents for Pacman.
- `pacman.py`: Main file to run Pacman games.
- `util.py`: Provides data structures such as `Stack`, `Queue`, and `PriorityQueue` for search algorithms.

### Files you need to edit:
- `search.py`: Implement search algorithms.
- `searchAgents.py`: Implement agents that use the search algorithms to guide Pacman.

## Algorithms Implemented

### 1. Depth First Search (DFS)
Depth First Search (DFS) explores as far down a branch of the search tree as possible before backing up to explore other branches. It uses a LIFO (Last In, First Out) stack to keep track of the nodes.

**DFS Characteristics:**
- **Fringe Structure:** Stack (LIFO)
- **Optimality:** Not optimal (may not find the shortest path)
- **Completeness:** Not complete (may get stuck in an infinite loop)

Command to test DFS:
```bash
python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs
```

### 2. Breadth First Search (BFS)
Breadth First Search (BFS) explores all nodes at the present depth level before moving on to the nodes at the next depth level. It uses a FIFO (First In, First Out) queue to manage the fringe.

**BFS Characteristics:**
- **Fringe Structure:** Queue (FIFO)
- **Optimality:** Yes (finds the shortest path)
- **Completeness:** Complete

Command to test BFS:
```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```

### 3. Uniform Cost Search (UCS)
Uniform Cost Search (UCS) is similar to BFS but takes the cost of the path into account. It uses a priority queue to expand the least-cost node first.

**UCS Characteristics:**
- **Fringe Structure:** Priority Queue (based on path cost)
- **Optimality:** Yes (finds the least-cost path)
- **Completeness:** Complete

Command to test UCS:
```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
```

### 4. A* Search
A* Search is an informed search algorithm that uses a heuristic function in addition to the cost to prioritize which nodes to explore. It combines the benefits of UCS and greedy best-first search.

**A* Characteristics:**
- **Fringe Structure:** Priority Queue (based on cost + heuristic)
- **Optimality:** Yes, if the heuristic is admissible and consistent
- **Completeness:** Complete

Command to test A* Search:
```bash
python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

## Heuristics Implemented

### 1. Corners Problem Heuristic
In the Corners Problem, Pacman must visit all four corners of the maze. The heuristic is designed to estimate the shortest path that touches all four corners. It is important that the heuristic is both admissible and consistent to ensure optimality.

Command to test:
```bash
python pacman.py -l mediumCorners -p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic
```

### 2. Food Search Heuristic
This heuristic is used to solve the problem where Pacman must collect all the food pellets in the maze. The goal is to minimize the number of steps required to clear all the food.

Command to test:
```bash
python pacman.py -l trickySearch -p AStarFoodSearchAgent
```

## How to Run the Project
1. Download the project files from the course website.
2. Unzip the files and navigate to the project directory.
3. You can run the Pacman game using the following command:
    ```bash
    python pacman.py
    ```
4. To test your search algorithms, run the following commands:
    - For DFS:
      ```bash
      python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs
      ```
    - For BFS:
      ```bash
      python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
      ```
    - For UCS:
      ```bash
      python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
      ```
    - For A*:
      ```bash
      python pacman.py -l bigMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
      ```

## Acknowledgments
This project is based on UC Berkeley's [CS188: Introduction to Artificial Intelligence](http://ai.berkeley.edu). All the materials provided in this repository are for educational purposes.
