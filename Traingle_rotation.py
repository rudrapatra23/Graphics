import numpy as np
import matplotlib.pyplot as plt

triangle = np.array([
    [1, 3, 2],
    [1, 1, 4],
    [1, 1, 1]
])

r_deg = 45
r = np.deg2rad(r_deg)

R = np.array([
    [ np.cos(r), -np.sin(r), 0],
    [ np.sin(r),  np.cos(r), 0],
    [        0,         0,  1]
])

rotated = R @ triangle

ox, oy = triangle[0], triangle[1]
rx, ry = rotated[0], rotated[1]

orig = np.vstack([np.column_stack([ox, oy]), [ox[0], oy[0]]])
rots = np.vstack([np.column_stack([rx, ry]), [rx[0], ry[0]]])

fig, ax = plt.subplots()
ax.plot(orig[:, 0], orig[:, 1], 'bo-', label="Original")
ax.plot(rots[:, 0], rots[:, 1], 'go-', label=f"Rotated by {r_deg}°")

ax.grid(True)
ax.legend()

plt.title('Triangle Rotation')
plt.show()
