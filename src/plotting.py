"""Function creating a scatterplot"""

import matplotlib.pyplot as plt

plt.style.use(
    "https://raw.githubusercontent.com/allfed/ALLFED-matplotlib-style-sheet/main/ALLFED.mplstyle"
)


def create_scatter_plot(x_data, y_data, title="", xlabel="", ylabel=""):
    """
    Create a scatter plot with the provided x and y data.

    Arguments:
    x_data (list): The data for the x-axis.
    y_data (list): The data for the y-axis.
    title (str): The title of the plot.
    xlabel (str): The label for the x-axis.
    ylabel (str): The label for the y-axis.
    """

    # Create a new figure and axes
    plt.figure()

    # Create the scatter plot
    plt.scatter(x_data, y_data)

    # Set the title and labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Show the plot
    plt.show()
