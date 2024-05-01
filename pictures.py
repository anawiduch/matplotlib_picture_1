from matplotlib.patches import Circle, Wedge, Polygon, Ellipse, Arc, Path, PathPatch
import matplotlib.pyplot as plt


def draw_cat(ax):
    # туловище
    poly = [(3, 1), (4, 14), (5, 11), (8, 11), (9, 14), (10, 1)]
    polygon = Polygon(poly, fc="orange", ec="black", lw=4)
    ax.add_patch(polygon)

    # глаза
    circle = Circle((5.3, 8.5), 1.2, fc="white", ec="black", lw=4)
    ax.add_patch(circle)

    circle = Circle((7.7, 8.5), 1.2, fc="white", ec="black", lw=4)
    ax.add_patch(circle)

    # зрачки
    circle = Circle((6, 8.3), 0.1, fc="black", ec="black", lw=4)
    ax.add_patch(circle)

    circle = Circle((7, 8.3), 0.1, fc="black", ec="black", lw=4)
    ax.add_patch(circle)

    # нос
    circle = Circle((6.5, 7.5), 0.3, fc="black", ec="black", lw=4)
    ax.add_patch(circle)

    # задние лапы
    wedge = Wedge((3, 1), 2, 86, 180, fc="black", ec="black", lw=4)
    ax.add_patch(wedge)

    wedge = Wedge((10, 1), 2, 0, 94, fc="black", ec="black", lw=4)
    ax.add_patch(wedge)

    # передние лапы
    ellipse = Ellipse((5.5, 1.2), 2, 1.5, fc="black", ec="black", lw=4)
    ax.add_patch(ellipse)

    ellipse = Ellipse((7.5, 1.2), 2, 1.5, fc="black", ec="black", lw=4)
    ax.add_patch(ellipse)

    # улыбка
    arc =  Arc((6.5, 6.5), 5, 3, angle=0, theta1=200, theta2=340, lw=6, fill=False)
    ax.add_patch(arc)

    # линия между носом и улыбкой, усы
    vertices = [(6.5, 5), (6.5, 7.5), (10, 6), (6.5, 7.5), (10, 6.5), (6.5, 7.5), (10, 7),
                (6.5, 7.5), (3, 6), (6.5, 7.5), (3, 6.5), (6.5, 7.5), (3, 7)]

    # число 1 соответствует команде matplotlib.path.Path.MOVETO
    # число 2 соответствует команде matplotlib.path.Path.LINETO
    codes = [1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

    path = Path(vertices, codes)
    path_patch = PathPatch(path, fill=False, lw=1)
    ax.add_patch(path_patch)

def flower(ax):
    #лепестки
    circle = Circle((14, 15), 1, fc="blue", ec="black", lw=1)
    ax.add_patch(circle)

    circle = Circle((14.7, 16.2), 1, fc="blue", ec="black", lw=1)
    ax.add_patch(circle)

    circle = Circle((16, 16), 1, fc="blue", ec="black", lw=1)
    ax.add_patch(circle)
    circle = Circle((16.2, 14.6), 1, fc="blue", ec="black", lw=1)
    ax.add_patch(circle)
    circle = Circle((15, 14), 1, fc="blue", ec="black", lw=1)
    ax.add_patch(circle)

    circle = Circle((15.21, 15), 0.7, fc="yellow", ec="black", lw=1)
    ax.add_patch(circle)

    #стебель
    arc = Arc((15.1, 7), 1, 12, angle=1, theta1=90, theta2=270, lw=3)
    ax.add_patch(arc)
    arc = Arc((15.1, 7), 1, 2, angle=1, theta1=180, theta2=10, lw=3)
    ax.add_patch(arc)

    # листочек
    ellipse = Ellipse((15.65, 8.5), 1, 3, fc="green", ec="black", lw=1)
    ax.add_patch(ellipse)
n = 20

m = 20

plt.xlim(0, n)

plt.ylim(0, m)

ax = plt.gca()

draw_cat(ax)
flower(ax)


ax.axes.set_axis_off()

plt.show()