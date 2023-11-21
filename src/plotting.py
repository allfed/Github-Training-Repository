import matplotlib.pyplot as plt
plt.style.use("https://raw.githubusercontent.com/allfed/ALLFED-matplotlib-style-sheet/main/ALLFED.mplstyle")

def plot_data(x,y, title, x_label, y_label):


    """
    Plots the results of the model
    Arguments:
        x: x values to plot
        y: y values to plot
        title: title of the plot
        x_label: label for the x axis
        y_label: label for the y axis
    Returns:
        None, but plots the results
    """
    plt.scatter(x, y, alpha=0.5)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


