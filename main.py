# sphinx_gallery_thumbnail_number = 3
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd

from car import Car
from sim import sim

car = Car("Rental Van", "Van", 20, 100, 7)
# car = Car("High Mileage Sedans", "Van", 42, 0, 5)


sim_results = sim(range(1, 15 + 1), range(6, 14 + 1), car)

sim_results = sorted(sim_results, key=lambda x: x.cost_per_person)[:20]

print(sim_results)

results_as_tuple = list(map(lambda x: x.to_tuple(), sim_results))
x, y, z, extra = zip(*results_as_tuple)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.view_init(45, 55)
ax.set_xlabel('Number of People')
ax.set_ylabel('Number of Days')
ax.set_zlabel('Cost Per Person')

ax.plot3D(x, y, z, 'gray')
# ax.scatter3D(x, y, z, c=z, cmap='Greens')
# ax.contour3D([x, x], [y, y], [z, z], 50, cmap='binary')

fig.show()

df = pd.DataFrame(results_as_tuple, columns=['Num People', 'Num Days', 'Cost Per Person', 'Total Cost'])
print(df)
