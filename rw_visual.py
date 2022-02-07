import matplotlib.pyplot as plt
from random_walk import Randomwalk

rw = Randomwalk(100_000)
rw.fill_walk()
point_number = range(rw.num_points)

plt.style.use('classic')

fig, ax = plt.subplots(figsize=(15, 9))
ax.scatter(rw.x_values, rw.y_values, s=10, c=point_number, cmap=plt.cm.plasma, 
           edgecolor ='none')

# emphasize the starting and ending points
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()