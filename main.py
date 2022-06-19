import matplotlib.pyplot as plt


def f(y: float,
      z: float,
      m: float,
      p: float,
      k: float) -> float:
    return - p / m * z - k / m * y


def runge_kutta(m: float, p: float, k: float):
    # left_border = 0
    right_border = 10
    step = 0.01

    # initial conditions
    x_0 = 0.0
    y_0 = 1.0
    z_0 = 2.0  # (y)' = z

    x: list = []
    y: list = []

    while x_0 < right_border:
        k1 = f(y_0, z_0, m, p, k)
        q1 = z_0

        k2 = f(y_0 + q1 * step / 2.0, z_0 + k1 * step / 2.0, m, p, k)
        q2 = z_0 + k1 * step / 2.0

        k3 = f(y_0 + q2 * step / 2.0, z_0 + k2 * step / 2.0, m, p, k)
        q3 = z_0 + k2 * step / 2.0

        k4 = f(y_0 + q3 * step, z_0 + k3 * step, m, p, k)
        q4 = z_0 + k3 * step

        z_1 = z_0 + (k1 + 2.0 * k2 + 2.0 * k3 + k4) * step / 6.0
        y_1 = y_0 + (q1 + 2.0 * q2 + 2.0 * q3 + q4) * step / 6.0

        x.append(x_0 + step)
        y.append(y_1)

        print("\t" + str(x_0 + step) + "\t\t" + str(y_1) + "\t\t" + str(z_1))

        y_0 = y_1
        z_0 = z_1
        x_0 += step

    return x, y


def plot(x: list, y: list):
    plt.style.use('seaborn-whitegrid')

    figure = plt.figure()

    default_axes = figure.add_subplot(1, 1, 1)

    default_axes.plot(x, y)
    plt.show()


if __name__ == '__main__':
    x, y = runge_kutta(1, 0, -4)
    plot(x, y)
