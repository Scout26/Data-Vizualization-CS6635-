# -*- coding: utf-8 -*-
"""4_1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dvDPcq6t3T5pef5k6clZaGD3jf2ptCyl
"""

#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Here generating random numbers using numpy library in python
np.random.seed(42)

# Question mentions to generate 15 random seed points within the range [0, 19]
seed_points = np.random.randint(0, 20, size=(15, 2))

# Get data
vecs = np.reshape(np.fromfile("wind_vectors.raw"), (20,20,2))
vecs_flat = np.reshape(vecs, (400,2)) # useful for plotting
vecs = vecs.transpose(1,0,2) # needed otherwise vectors don't match with plot

# X and Y coordinates of points where each vector is in space
xx, yy = np.meshgrid(np.arange(0, 20), np.arange(0, 20))

# Plot vectors
plt.plot(xx, yy, marker='.', color='b', linestyle='none')
plt.quiver(xx, yy, vecs_flat[:,0], vecs_flat[:,1], width=0.001)

# This part does the plotting of the seed points with graph label for better understanding
plt.scatter(seed_points[:, 0], seed_points[:, 1], color='red', label='Seed Points')
plt.legend()

plt.show()
