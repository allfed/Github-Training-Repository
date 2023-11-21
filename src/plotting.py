"""
File contains a single function to plot a scatter plot following ALLFED Guidelines.
"""
import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use(
    "https://raw.githubusercontent.com/allfed/ALLFED-matplotlib-style-sheet/main/ALLFED.mplstyle"
)


def scatterplot(N):
    """
    Plots a matplotlib scatterplot using random data.

    Arguments:
        N (int): number of random datapoints to plot
    Returns:
        None
    """
    x = np.random.rand(N)
    y = np.random.rand(N)
    plt.scatter(x, y)
    plt.ylabel("Y-Axis")
    plt.xlabel("X-Axis")
    plt.title("Example Data")
    plt.show()
