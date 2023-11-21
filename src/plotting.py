import matplotlib.pyplot as plt
import numpy as np

def plot_scatter(X, Y):
    """
    plot a scatterplot for inputs X and Y

    Arguments:
        X: an array or a list of numbers
        Y: an array or a list of numbers

    Returns:
        plot: scatter plot with X being x-axis and Y being Y-axis
    """
    # use the ALLFED plot style
    plt.style.use("https://raw.githubusercontent.com/allfed/ALLFED-matplotlib-style-sheet/main/ALLFED.mplstyle")
    plt.scatter(x, y)
    plt.show()


np.random.seed(123)
N = 30
x = np.random.rand(N)
y = np.random.rand(N)
plot_scatter(x, y)
