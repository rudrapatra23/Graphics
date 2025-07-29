import numpy as np
import matplotlib.pyplot as plt
x, y = 4, 3
cx, cy = 2, 2
theta = np.pi / 2
x_new = (x - cx) * np.cos(theta) - (y - cy) * np.sin(theta) + cx
y_new = (x - cx) * np.sin(theta) + (y - cy) * np.cos(theta) + cy
fig, ax = plt.subplots()
ax.plot([cx, x], [cy, y], 'bo-')
ax.plot([cx, x_new], [cy, y_new], 'ro-')
ax.plot(cx, cy, 'go')
plt.grid(True)
plt.show()
