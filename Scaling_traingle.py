import numpy as np
import matplotlib.pyplot as plt

triangle = np.array([
    [1, 3, 2],
    [1, 1, 4],
    [1, 1, 1]
])

sx, sy = 2.0, 1.5
S = np.array([[sx, 0, 0],
              [0, sy, 0],
              [0,  0, 1]])

scaled = S @ triangle

ox, oy = triangle[0], triangle[1]
sx_, sy_ = scaled[0], scaled[1]

orig = np.vstack([np.column_stack([ox, oy]), [ox[0], oy[0]]])
sc = np.vstack([np.column_stack([sx_, sy_]), [sx_[0], sy_[0]]])

fig, ax = plt.subplots()
ax.plot(orig[:, 0], orig[:, 1], 'bo-', label="Original")
ax.plot(sc[:, 0], sc[:, 1], 'ro-', label=f"Scaled by ({sx}, {sy})")

ax.set_aspect('equal', 'box')
ax.grid(True)
ax.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Triangle Scaling')
plt.show()
