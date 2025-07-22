import pyplot from matplotlib as pyplot
def DDA(x1, y1, x2, y2):
    dy = y2 - y1
    dx = x2 - x1
    steps = max(dy,dx)

    xinc = dx/steps
    yinc = dy/steps

    x = float(x2)
    y = float(y2)

    x_coordinates = []
    y_coordinates = []

    for i in range(steps):
        x_coorinates.append(x)
        y_coorinates.append(y)

        x = x + xinc
        y = y + yinc

    plt.plot(x_coorinates, y_coorinates, marker="o",
             markersize=1, markerfacecolor="green")
    plt.show()


if __name__ == "__main__":
    x1 = int(input("Enter value of x1: "))
    x2 = int(input("Enter value of x2: "))
    y1 = int(input("Enter value of y1: "))
    y2 = int(input("Enter value of y2: "))

    DDA(x1, y1, x2, y2)