#Fig. 8. Performance Comparison by Grading Software in Proposal Writing of Teacher Agency


# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Defining data and settings
grading_software = ['Study Fetch', 'Essay Grader', 'QuillBot', 'Grammarly']
gpt_only = [86, 61, 83, 94]
model_only = [85, 70, 82, 92]
gpt_assisted = [84, 75, 88, 88]
model_assisted = [88, 67, 83, 93]



x = np.arange(len(grading_software))  # the label locations
width = 0.15  # the width of the bars
specified_macaron_colors = ['#ffb3ba', '#ffdfba', '#ffffba', '#baffc9']  # light pink, light orange, light yellow, light green
patterns = ['/', '\\', 'x', 'o']  # Hatch patterns

# File path for saving the PDF
output_path = "fig8_Comparison_by_Grading_Software_in_Proposal_Writing_of_Teacher_Agency.pdf"

# Creating the chart
fig, ax = plt.subplots() #figsize=(10, 6)
rects1 = ax.bar(x - 2*width, gpt_only, width, label='GPT', color=specified_macaron_colors[0], hatch=patterns[0], edgecolor='black')
rects2 = ax.bar(x - width, model_only, width, label='Customized GPT', color=specified_macaron_colors[1], hatch=patterns[1], edgecolor='black')
rects3 = ax.bar(x, gpt_assisted, width, label='GPT Assisted', color=specified_macaron_colors[2], hatch=patterns[2], edgecolor='black')
rects4 = ax.bar(x + width, model_assisted, width, label='Customized GPT Assisted', color=specified_macaron_colors[3], hatch=patterns[3], edgecolor='black')

# Adding labels and ticks
ax.set_xlabel('Grading Software')
ax.set_ylabel('Percentage (%)')
ax.set_xticks(x)
ax.set_xticklabels(grading_software)

# Placing the legend
ax.legend(loc='upper center', bbox_to_anchor=(0.35, 1), ncol=1)

# Adding borders to the axes (spines)
for spine in ax.spines.values():
    spine.set_edgecolor('black')
    spine.set_linewidth(1.5)

# Adding a border around the entire figure
#fig.patch.set_linewidth(2)
#fig.patch.set_edgecolor('black')

# Saving the chart as PDF
plt.tight_layout()
fig.savefig(output_path, format='pdf')
plt.close(fig)

print(f"Chart saved as {output_path}")

