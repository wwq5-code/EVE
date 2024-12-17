#Fig. 10. Similarity Comparison


import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
categories = ['Student Agency', 'Teacher Agency', 'Teacher Identity']
gpt_only = [25, 27, 25]  # Updated Student Agency value
model_only = [20, 17, 26]   # Updated Teacher Identity value
gpt_assisted = [21, 11, 30]
model_assisted = [14, 19, 24]

# Define bar width and positions for each group
bar_width = 0.2
index = np.arange(len(categories))

# Define the new pastel colors
gpt_only_color = '#ffb3ba'  # light pink
model_only_color = '#ffdfba'  # light orange
gpt_assisted_color = '#ffffba'  # light yellow
model_assisted_color = '#baffc9'  # light green

# Create the figure and axes
fig, ax = plt.subplots()

# Plot the bars with the specified hatch patterns and colors
ax.bar(index - 1.5 * bar_width, gpt_only, bar_width, label='GPT', color=gpt_only_color, hatch='/', edgecolor='black')  # forward slash pattern
ax.bar(index - 0.5 * bar_width, model_only, bar_width, label='Customized GPT', color=model_only_color, hatch='\\', edgecolor='black')  # backslash pattern
ax.bar(index + 0.5 * bar_width, gpt_assisted, bar_width, label='GPT Assisted', color=gpt_assisted_color, hatch='x', edgecolor='black')  # cross pattern
ax.bar(index + 1.5 * bar_width, model_assisted, bar_width, label='Customized GPT Assisted', color=model_assisted_color, hatch='o', edgecolor='black')  # circle pattern

# Add labels without the title
ax.set_xlabel('Proposal Writing')
ax.set_ylabel('Percentage (%)')

# Adjust the x-ticks and labels with capitalized first letters
ax.set_xticks(index)
ax.set_xticklabels(['Student Agency', 'Teacher Agency', 'Teacher Identity'])

# Adjust the legend text and position to move it further up, over 80% of the vertical coordinate
ax.legend(loc='upper center', bbox_to_anchor=(0.6, 0.9), ncol=1)

# Add a black border around the entire plot
for spine in ax.spines.values():
    spine.set_edgecolor('black')
    spine.set_linewidth(3)

# Show the plot
plt.tight_layout()
plt.savefig('fig10_Similarity_Comparison.pdf', format='pdf', dpi=200)
plt.show()

