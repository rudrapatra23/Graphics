import matplotlib.pyplot as plt
x_vals = []
y_vals = []
def set_pixel(x, y):
    x_vals.extend([x, -x, x, -x])
    y_vals.extend([y, y, -y, -y])


def midpoint(a, b):
    x = 0
    y = b
    aa = a * a
    bb = b * b
    aa2 = aa * 2
    bb2 = bb * 2
    fx = 0
    fy = aa2 * b
    p = bb - aa * b + 0.25 * aa
    while fx < fy :
        set_pixel(x,y)
        x += 1
        fx += bb2
        if p < 0 :
            p = p + fx +bb
        else:
            y -= 1
            fy -= aa2
            p = p + fx - fy + bb
    set_pixel(x, y)
    p = bb*(x + 0.5)*(x + 0.5) + aa*(y - 1)*(y - 1) - aa * bb
    while y > 0:
        y -= 1
        fy -= aa2
        if p >= 0:
            p = p - fy + aa
        else:
            x += 1
            fx += bb2
            p = p + fx - fy + aa
        set_pixel(x, y)

midpoint(700,500)
plt.scatter(x_vals, y_vals, s = 0.5)
plt.grid(True)
plt.show()
