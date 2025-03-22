# -*- coding: utf-8 -*-
"""4_3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J7fiWTCFyokIFPVTRXj0LCz3pQLi67LL
"""

#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


# Here generating random numbers using numpy library in python
np.random.seed(42)


# Question mentions to generate seed points within the range [0, 20]
seed_points = np.random.randint(0, 20, size=(15, 2))

# Get data
vecs = np.reshape(np.fromfile("wind_vectors.raw"), (20, 20, 2))
vecs = vecs.transpose(1, 0, 2)  # needed otherwise vectors don't match with plot


# Bilinear_interpolation Function creation
def bi(x, y, grid):
    x0, y0 = int(x), int(y)
    x1, y1 = x0 + 1, y0 + 1
    # grid size adjustment 
    x0 = max(0, min(x0, 19))
    x1 = max(0, min(x1, 19))
    y0 = max(0, min(y0, 19))
    y1 = max(0, min(y1, 19))
    #print(x0,y0,x1,y1)
    # Fetching the neighbour vector
    Q11 = grid[x0, y0]
    Q21 = grid[x1, y0]
    Q12 = grid[x0, y1]
    Q22 = grid[x1, y1]
    # Bilinear interpolation Step
    dx = x - x0
    dy = y - y0
    interpolated = (Q11 * (1 - dx) * (1 - dy) + Q21 * dx * (1 - dy) + Q12 * (1 - dx) * dy + Q22 * dx * dy)
    return interpolated

# We also need a function to trace streamline
def tc(start, grid, timestep, steps):
    x, y = start
    streamline = [start]

    for _ in range(steps):
      # For each point we also need a interpolation vector
        vector = bi(x, y, grid)
        # Updating the value of x and y
        x += vector[0] * timestep
        y += vector[1] * timestep
        #print("Value after updation",x,y)
        # For each point to the grid we bound them
        x = max(0, min(x, 19))
        y = max(0, min(y, 19))
        streamline.append((x, y))

        # Let's say if boundary is reached then we break the loop
        if x <= 0 or x >= 19 or y <= 0 or y >= 19:
            break

    return np.array(streamline)


# Now for each point in x and y            
xx, yy = np.meshgrid(np.arange(0, 20), np.arange(0, 20))

# Function to plot streamlines with given parameters
def pc(time_step, steps, title):
    streamlines = [tc(point, vecs, timestep, steps) for point in seed_points]

    plt.figure()
    plt.plot(xx, yy, marker='.', color='b', linestyle='none')
    plt.quiver(xx, yy, vecs[:, :, 0], vecs[:, :, 1], width=0.001)

    
    # This step will plot vectors
    plt.scatter(seed_points[:, 0], seed_points[:, 1], color='red', label='Seed Points')
    for streamline in streamlines:
        plt.plot(streamline[:, 0], streamline[:, 1], color='green', marker='o', markersize=3)

    plt.title(title)
    plt.legend()
    plt.show()

# Plot streamlines for the four sets of parameters
plot_streamlines(time_step=0.15, steps=16, title="Step Size 0.15, Steps 16")
plot_streamlines(time_step=0.075, steps=32, title="Step Size 0.075, Steps 32")
plot_streamlines(time_step=0.0375, steps=64, title="Step Size 0.0375, Steps 64")
