#Imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd


# Parameters
A = (-30, 0)  # Point A coordinates
O = (0, 0)    # Point O coordinates (center)
B = (30, 0)   # Point B coordinates
target_depth = 10  # Final depth
depth_increment = 0.5  # Depth increment per loop
# Number of steps for discretizing the path between two points
num_steps = 20

# Generate toolpath coordinates
x_positions = [A[0]]  # Start directly at A
z_positions = [0.3]     # Start at Z = 0.3 , clearance parameter between the tool and the sheet to ensure zero loading force at the beginning of every loading cycle

# Tool starts at depth 0.3 and moves down by depth_increment each cycle until it reaches the target_depth
current_depth = 0.5


while current_depth < target_depth:
    # Move from A to O
    for i in range(1, num_steps + 1):
        x = A[0] + (O[0] - A[0]) * i / num_steps
        z = 0.3-current_depth * i / num_steps  # Depth change starts right here
        x_positions.append(x)
        z_positions.append(z)
    
    # Move from O to B
    for i in range(1, num_steps + 1):
        x = O[0] + (B[0] - O[0]) * i / num_steps
        z = 0.3-current_depth * (num_steps - i) / num_steps  # Depth continues
        x_positions.append(x)
        z_positions.append(z)
    
    # Increase depth for the next cycle (before next movement from B to O)
    current_depth += depth_increment

    # Move from B to O
    for i in range(1, num_steps + 1):
        x = B[0] + (O[0] - B[0]) * i / num_steps
        z = 0.3-current_depth * i / num_steps  # Depth continues here as well
        x_positions.append(x)
        z_positions.append(z)

    # Move from O to A
    for i in range(1, num_steps + 1):
        x = O[0] + (A[0] - O[0]) * i / num_steps
        z = 0.3-current_depth * (num_steps - i) / num_steps  # Depth continues
        x_positions.append(x)
        z_positions.append(z)

    current_depth += depth_increment

# Output coordinates for use
coordinates = list(zip(x_positions, z_positions))
for i, (x, z) in enumerate(coordinates):
    print(f"Step {i + 1}: X = {x:.2f}, Z = {z:.2f}")

#export data to csv file
#uncomment this part if you need to save X,Z coordinates
"""
df = pd.DataFrame({
    'X': x_positions,
    'Z': z_positions
})

# Save DataFrame to an Excel file
df.to_excel('toolpath_coordinates_20step.xlsx', index=False)
"""

##Tool path visualization purpose

# Plot the tool path with comet animation
fig, ax = plt.subplots()
ax.plot(x_positions, z_positions, color='blue', linewidth=0.5, label='Tool Path')
comet, = ax.plot([], [], 'ro', markersize=5)  # Initialize comet as a single point

# Set axis limits for better visualization
ax.set_xlim(-35, 35)
ax.set_ylim(-target_depth - 1, 1)
ax.set_xlabel('X Position (mm)')
ax.set_ylabel('Z Position (mm)')
ax.set_title('Tool Path for V-Shape Incremental Sheet Forming')
ax.legend()

# Update function for animation
def update(frame):
    # Update comet's position to current frame's coordinates
    comet.set_data([x_positions[frame]], [z_positions[frame]])  
    return comet,

# Create animation
ani = FuncAnimation(fig, update, frames=len(x_positions), interval=100, blit=True)
plt.show()

