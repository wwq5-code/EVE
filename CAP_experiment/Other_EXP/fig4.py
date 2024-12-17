#Fig. 4. Performance Across Correction Rounds (Teacher Agency)
import matplotlib.pyplot as plt

# 数据
categories = [0, 1, 2, 3]
gpt = [41.67, 41.67, 41.67, 41.67]
customized_gpt = [20, 20, 20, 20]
gpt_assisted = [20, 20, 20, 20]
customized_gpt_assisted = [54.55, 54.55, 36.36, 36.36]

# 绘图
plt.figure(figsize=(6, 4.7))

# 添加每条线的数据和样式
plt.plot(categories, gpt, marker='o', label='GPT', linestyle='-', color='red', linewidth=4, markersize=10)
plt.plot(categories, customized_gpt, marker='s', label='Customized GPT', linestyle='--', color='blue', linewidth=4, markersize=10)
plt.plot(categories, gpt_assisted, marker='^', label='GPT Assisted', linestyle='-.', color='green', linewidth=4, markersize=10)
plt.plot(categories, customized_gpt_assisted, marker='d', label='Customized GPT Assisted', linestyle=':', color='purple', linewidth=4, markersize=10)

# 设置坐标轴标签
plt.xlabel("Correction Round", fontsize=18)
plt.ylabel("Incorrect Percentage (%)", fontsize=18)

# 设置刻度
plt.xticks(categories, fontsize=12)
plt.yticks(fontsize=12)

# 添加网格线
#plt.grid(axis='y', linestyle='--', alpha=0.7)

# 图例设置
plt.legend(fontsize=12)  # 无标题图例

# 调整布局
plt.tight_layout()
plt.savefig('fig4_Across_Correction_Rounds_Teacher_Agency.pdf', format='pdf', dpi=200)
# 显示图像
plt.show()
