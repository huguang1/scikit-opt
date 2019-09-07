import numpy as np
from scipy import spatial
import pandas as pd
import matplotlib.pyplot as plt

num_points = 8

points_coordinate = np.random.rand(num_points, 2)  # generate coordinate of points
distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')
print('distance_matrix is: \n', distance_matrix)


def cal_total_distance(routine):
    num_points, = routine.shape
    return sum([distance_matrix[routine[i % num_points], routine[(i + 1) % num_points]] for i in range(num_points)])


# test:
# points = np.arange(num_points)  # generate index of points
# cal_total_distance(points)

# %%

from sko.GA import GA_TSP

ga_tsp = GA_TSP(func=cal_total_distance, n_dim=8, pop=50, max_iter=200, Pm=0.001)
best_points, best_distance = ga_tsp.fit()

fig, ax = plt.subplots(1, 1)
best_points_ = np.concatenate([best_points, [best_points[0]]])
best_points_coordinate = points_coordinate[best_points_, :]
ax.plot(best_points_coordinate[:, 0], best_points_coordinate[:, 1], 'o-r')
plt.show()