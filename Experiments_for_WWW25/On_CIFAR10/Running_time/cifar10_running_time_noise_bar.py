import matplotlib.pyplot as plt
import numpy as np




labels = ['5', '10', '15', '20', '25']
#unl_fr = [10*10*0.22 *5, 10*10*0.22*5, 10*10*0.22 *5, 10*10*0.22*5 , 10*10*0.22*5  , 10*10*0.22*5  ]


cap_ms_not_in = [  4.0058, 4.00997, 4.06, 3.97, 3.93]


mib_ms_not_in = [  617, 614, 617, 621, 613]


x = np.arange(len(labels))  # the label locations
width = 0.76 # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)

plt.style.use('seaborn')
# plt.figure(figsize=(5.5, 5.3))
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(5.5, 5.3), gridspec_kw={'height_ratios': [1, 3]})

l_w=5
m_s=15
marker_s = 3
markevery=1

ax1.plot(x, cap_ms_not_in, linestyle='-', color='#797BB7', marker='o', fillstyle='full', markevery=markevery, label='CAP', linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)

ax1.plot(x, mib_ms_not_in, linestyle='-.', color='#2A5522',  marker='D', fillstyle='full', markevery=markevery, label='MIB',linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)

ax1.set_ylim(600, 700)
ax1.spines['bottom'].set_visible(False)
ax1.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)


ax2.plot(x, cap_ms_not_in, linestyle='-', color='#797BB7', marker='o', fillstyle='full', markevery=markevery, label='CAP', linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)

ax2.plot(x, mib_ms_not_in, linestyle='-.', color='#2A5522',  marker='D', fillstyle='full', markevery=markevery, label='MIB',linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)


ax2.set_ylim(0, 10)
ax2.spines['top'].set_visible(False)

# Add diagonal lines to indicate a break in the y-axis
d = .015  # size of diagonal lines
kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
ax1.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# Labels
ax2.set_xlabel('Perturbation Limit' ,fontsize=28)
ax2.set_ylabel('Running Time (s)', fontsize=28)
# ax2.yaxis.set_label_position('right')
ax2.yaxis.set_label_coords(-0.1, 0.7)
ax2.set_xticks(x, labels, fontsize=28)
ax2.legend(loc='best',fontsize=28)


# Add some text for labels, title and custom x-axis tick labels, etc.



# plt.ylabel('Running Time (s)', fontsize=24)
# # ax.set_title('Performance of Different Users n')
# plt.xticks(x, labels, fontsize=20)
# # ax.set_xticklabels(labels,fontsize=15)
#
# my_y_ticks = np.arange(0, 800.1, 200)
# plt.yticks(my_y_ticks, fontsize=20)
# # ax.set_yticklabels(my_y_ticks,fontsize=15)
# plt.legend(loc='upper left', fontsize=20)
# plt.xlabel('Perturbation Limit' ,fontsize=24)



# ax.bar_label(rects1, padding=1)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)

# plt.title("On CIFAR10", fontsize= 24)
plt.tight_layout()

plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('cifar10_runningtime_noise_analysis_bar.pdf', format='pdf', dpi=200)
plt.show()
