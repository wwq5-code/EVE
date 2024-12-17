import pandas as pd
import matplotlib.pyplot as plt

# 数据定义
data = {
    "Correction Round": [0, 1, 2, 3],
    "GPT Only": [16.67, 8.33, 0, 0],
    "Model Only": [57.14, 57.14, 57.14, 57.14],
    "GPT Assisted": [33.33, 16.67, 8.33, 8.33],
    "Model Assisted": [83.33, 16.67, 16.67, 16.67]
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 图表样式设置
line_styles = ['-', '--', '-.', ':']  # 实线, 虚线, 点划线, 点线
markers = ['o', 's', '^', 'D']  # 圆形, 方形, 三角形, 菱形
new_contrast_colors = ['red', 'blue', 'green', 'purple']  # 红, 蓝, 绿, 紫
even_thicker_line_width = 4  # 线条粗细
larger_marker_size = 10  # marker大小

# 图例名称映射
updated_labels = {
    "GPT Only": "GPT",
    "Model Only": "Customized GPT",
    "GPT Assisted": "GPT Assisted",
    "Model Assisted": "Customized GPT Assisted"
}

# 绘制图表
#plt.figure(figsize=(10, 6))

plt.figure(figsize=(6, 4.7))

for i, column in enumerate(df.columns[1:]):
    plt.plot(df["Correction Round"], df[column], marker=markers[i], label=updated_labels[column],
             linestyle=line_styles[i], color=new_contrast_colors[i],
             linewidth=even_thicker_line_width, markersize=larger_marker_size)

# 图表轴标签和刻度
plt.xlabel('Correction Round', fontsize=18)
plt.ylabel('Incorrect Percentage', fontsize=18)
plt.xticks([0, 1, 2, 3])


# 图例设置
plt.legend(loc="upper right", bbox_to_anchor=(0.85, 0.99), fontsize=12)

# 添加边框
plt.gca().spines['top'].set_linewidth(1.5)
plt.gca().spines['right'].set_linewidth(1.5)
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().spines['bottom'].set_linewidth(1.5)

# 调整布局并显示图表
plt.tight_layout()
plt.savefig('test.pdf', format='pdf', dpi=200)
plt.show()