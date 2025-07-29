import numpy as np
import matplotlib.pyplot as plt

# Homogeneous coordinates of the triangle
triangle = np.array([
    [1, 3, 2],
    [1, 1, 4],
    [1, 1, 1]
])

Tx, Ty = 4, 3
T = np.array([
    [1, 0, Tx],
    [0, 1, Ty],
    [0, 0, 1]
])

translated = T @ triangle
ox, oy = triangle[0], triangle[1]
tx, ty = translated[0], translated[1]
orig = np.vstack([np.column_stack([ox, oy]), [ox[0], oy[0]]])
trans = np.vstack([np.column_stack([tx, ty]), [tx[0], ty[0]]])
fig, ax = plt.subplots()
ax.plot(orig[:, 0], orig[:, 1], 'bo-', label="Original")
ax.plot(trans[:, 0], trans[:, 1], 'ro-', label=f"Translated by ({Tx}, {Ty})")

ax.set_aspect('equal', 'box')
ax.grid(True)
ax.legend()
plt.title('Triangle Translation')
plt.show()
