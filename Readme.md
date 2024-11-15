# Toolpath Generation for V-Shape Incremental Sheet Forming
This project contains Python code to generate a toolpath for V-shaped incremental sheet forming (ISF). 
The toolpath is discretized into steps and allows visualizing the path in a 2D plot while exporting the coordinates for use in external applications.

![Tool-path configuration](https://github.com/user-attachments/assets/748d9ab6-4a42-4457-bb41-e0bd7b787512)

## Features
  * Generates a toolpath for forming a V-shape with configurable parameters:
  * Start and end points (A, B, and O).
  * Depth increments per loop.
  * Number of steps for discretization.
  * Outputs the toolpath coordinates in CSV or Excel format.
  * Computes the total path length of the tool.
  * Animates the toolpath using matplotlib for visualization.
## Requirements
The project requires Python 3.6 or later with the following libraries installed:

  * numpy: For mathematical calculations.
  * matplotlib: For visualization and animation.
  * pandas: For exporting coordinates to files.
  * openpyxl: Required if exporting to Excel (.xlsx).
  * Install the required libraries using pip:

## Code Overview
### Input Parameters

  * Start and end points:
A = (-30, 0) (starting point on the left).
O = (0, 0) (center point).
B = (30, 0) (ending point on the right).
Depth settings:
target_depth = 10 (final depth to reach).
depth_increment = 0.5 (incremental depth per loop).
Discretization:
num_steps = 10 (number of steps between each segment of the path).

### Output

#### 1. Coordinates:
Coordinates of the toolpath are printed in the console.
The toolpath is saved to a CSV (toolpath_coordinates.csv) or Excel file (toolpath_coordinates.xlsx).
#### 2. Visualization:
A 2D plot of the toolpath is displayed.
A comet-style animation shows the movement of the tool.

![Tool_Path](https://github.com/user-attachments/assets/983681fc-a64c-42a4-9ebe-70e00c117165)


