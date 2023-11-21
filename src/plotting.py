import matplotlib.pyplot as plt
import numpy as np

plt.style.use("https://raw.githubusercontent.com/allfed/ALLFED-matplotlib-style-sheet/main/ALLFED.mplstyle")

if __name__ == "__main__":
    # Generate some somewhat linear data
    x = np.linspace(0, 10, 50)
    y = x + np.random.randn(50)

    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x, y)

    # Add labels and title
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Scatter Plot of Somewhat Linear Data")

    # Show the plot
    plt.show()
