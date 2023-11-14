import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from matplotlib.font_manager import FontProperties


# Function to create graph paper background
def setup_graph_paper(ax):
    # Set major and minor ticks to create gridlines
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.2))

    # Customize the grid
    ax.grid(which='major', color='blue', linestyle='-', linewidth=0.8, alpha=0.3)
    ax.grid(which='minor', color='blue', linestyle=':', linewidth=0.5, alpha=0.3)



fig, ax = plt.subplots()
setup_graph_paper(ax)

# Generate data for the plot
x = np.linspace(0, 5, 100)
y = 2 * np.sin(x)

with plt.xkcd(scale=3, length=200, randomness=5):
    ax.plot(x, y, label='Hand-drawn line')

# gotta manually customise the tick labels
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontname('Humor Sans')
    label.set_fontsize(14)
    label.set_color('blue')
    label.set_alpha(0.5)

# manually add the axis labels in the right font
ax.set_xlabel('X-axis', fontname='Humor Sans', fontsize=14)
ax.set_ylabel('Y-axis', fontname='Humor Sans', fontsize=14)
ax.set_title('Hand-drawn Plot on Graph Paper', fontname='Humor Sans', fontsize=16)
font = FontProperties(family='Humor Sans',
                      weight='bold',
                      style='normal', size=16) # getting the legend to look right
ax.legend(prop=font)

# Adjusting the axis limits to match the graph paper
ax.set_xlim([0, 5])
ax.set_ylim([-2.5, 2.5])

# removing the border frame
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.show()
