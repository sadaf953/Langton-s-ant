# Langton's Ant Simulation

## Overview
This project is a simulation of Langton's Ant, a two-dimensional universal Turing machine with a very simple set of rules but complex emergent behavior.

## Prerequisites
- Python 3.7+
- NumPy
- Matplotlib
- Pygame

## Installation
1. Clone the repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Simulation
```
python Langton's-ant.py
```

## How It Works
Langton's Ant moves on a grid according to these rules:
- At a white square, turn 90° right, flip the color of the square, move forward one unit
- At a black square, turn 90° left, flip the color of the square, move forward one unit

## Interesting Properties
After a seemingly chaotic initial phase, the ant begins to create a distinctive recurring "highway" pattern.
