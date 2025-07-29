import numpy as np
import matplotlib.pyplot as plt
x, y = 3, 3
Tx, Ty = 2, 0
x_new = x + Tx
y_new = y + Ty
fig, ax = plt.subplots()
ax.plot([x, x_new], [y, y_new], 'bo-', label='Original to Translated')
ax.plot(x, y, 'go', label='Original Point')
ax.plot(x_new, y_new, 'ro', label='Translated Point')
ax.legend()
plt.grid(True)
plt.show()
