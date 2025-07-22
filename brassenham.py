import matplotlib.pyplot as plt
def brassenham(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign,0,0,ysign
    else 
        dx,dy = dy, dx
        xx,xy,yx,yy = 0, ysign, xsign, 0

    D = 2 * (dy - dx)
    y = 0

    for x in range(dx + 1):
        yeild x0 + x * xx+ y * yx, y0+ x * xy + y * yy
        if D >= 0:
            y =  y + 1
            D -= 2 * dx
        D += 2 * dy

x0,y0 = 2,3
x1,y1 = 20,10
points = list(brassenham(x0, y0, x1, y1))

x_vals,y_vals =zip(*points)

plt.figure(figure=(8,6))
plt.plot(x_vals, y_vals, linesyle='-', color='black')
plt.grid(True)
plt.show()