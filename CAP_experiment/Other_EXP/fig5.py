#Fig. 5. Performance Across Correction Rounds (Teacher Identity)
import matplotlib.pyplot as plt

# Data from the table
labels = [0, 1, 2, 3]
gpt = [0, 0, 0, 0]
customized_gpt = [20, 20, 20, 20]
gpt_assisted = [26.32, 21.05, 21.05, 21.05]
customized_gpt_assisted = [0, 0, 0, 0]

# Plotting the data
plt.figure(figsize=(6, 4.7))
plt.plot(labels, gpt, linestyle='-', color='red', marker='o', markersize=10, linewidth=4, label="GPT")
plt.plot(labels, customized_gpt, linestyle='--', color='blue', marker='s', markersize=10, linewidth=4, label="Customized GPT")
plt.plot(labels, gpt_assisted, linestyle='-.', color='green', marker='^', markersize=10, linewidth=4, label="GPT Assisted")
plt.plot(labels, customized_gpt_assisted, linestyle=':', color='purple', marker='D', markersize=10, linewidth=4, label="Customized GPT Assisted")

# Adding labels
plt.xlabel("Correction Round", fontsize=18)
plt.ylabel("Incorrect Percentage (%)", fontsize=18)
plt.xticks(labels, fontsize=12)  # Set x-axis labels to 0, 1, 2, 3
#plt.ylim(0, 30)
plt.legend(fontsize=12)
#plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('fig5_Across_Correction_Rounds_Teacher_Identity.pdf', format='pdf', dpi=200)

# Display the plot
plt.show()
