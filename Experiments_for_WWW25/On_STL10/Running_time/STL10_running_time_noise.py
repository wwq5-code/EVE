import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = [  '15', '30', '45', '60', '75']
#unl_fr = [10*10*0.22 *5, 10*10*0.22*5, 10*10*0.22 *5, 10*10*0.22*5 , 10*10*0.22*5  , 10*10*0.22*5  ]


cap_ms_not_in = [  3.258, 3.51040, 3.60770, 3.74139, 3.4413]


mib_ms_not_in = [  567, 564, 561, 562, 560]


x = np.arange(len(labels))  # the label locations
width = 0.76 # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)

plt.style.use('seaborn')
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(5.5, 5.3), gridspec_kw={'height_ratios': [1, 3]})

l_w=5
m_s=15
marker_s = 3
markevery=1

ax1.plot(x, cap_ms_not_in, linestyle='-', color='#797BB7', marker='o', fillstyle='full', markevery=markevery, label='CAP', linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)

ax1.plot(x, mib_ms_not_in, linestyle='-.', color='#2A5522',  marker='D', fillstyle='full', markevery=markevery, label='MIB',linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)

ax1.set_ylim(500, 600)
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



plt.tight_layout()

plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('stl10_rt_noise_analysis_bar.pdf', format='pdf', dpi=200)
plt.show()
