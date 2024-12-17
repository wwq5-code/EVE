import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = [ '5', '10', '15', '20', '25']
#unl_fr = [10*10*0.22 *5, 10*10*0.22*5, 10*10*0.22 *5, 10*10*0.22*5 , 10*10*0.22*5  , 10*10*0.22*5  ]



cap_ms_not_in = [  13.052, 11.997, 12.933, 12.977498, 12.81]


mib_ms_not_in = [  145, 143, 146, 144, 146]


x = np.arange(len(labels))  # the label locations
width = 0.76 # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)

plt.style.use('seaborn')
plt.figure(figsize=(5.5, 5.3))
l_w=5
m_s=15
marker_s = 3
markevery=1
#plt.subplots(figsize=(8, 5.3))
#plt.bar(x - width / 2 - width / 8 + width / 8, unl_fr, width=0.168, label='Retrain', color='dodgerblue', hatch='/')
# plt.bar(x - width / 3, TaPD_ss,   width=width / 3, label='TAPE (SS)', color='#797BB7', edgecolor='black', hatch='*')
# plt.bar(x , TaPS_ms, width=width / 3, label='CAP', color='#9BC985',edgecolor='black', hatch='*')
# plt.bar(x + width / 3, MIB, width=width / 3, label='MIB', color='#E58579', edgecolor='black', hatch='/')
#plt.bar(x + width / 2 - width / 8 + width / 16, unl_hess_r, width=0.168, label='HBFU', color='orange', hatch='\\')

# # Plot the bars
# plt.bar(x - width / 5, cap_ms_not_in, width=width/2.5, label='CAP', color='#F7D58B', edgecolor='black', hatch='*')
# #ax[2,2].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#E58579', edgecolor='black', hatch='/')
#
# plt.bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MIB', color='#B595BF', edgecolor='black', hatch='\\')

plt.plot(x, cap_ms_not_in, linestyle='-', color='#797BB7', marker='o', fillstyle='full', markevery=markevery, label='EUV', linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)

plt.plot(x, mib_ms_not_in, linestyle='-.', color='#2A5522',  marker='D', fillstyle='full', markevery=markevery,
         label='MIB',linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)


# plt.bar(x - width / 2.5 ,  unl_br, width=width/3, label='VBU', color='orange', hatch='\\')
# plt.bar(x,unl_self_r, width=width/3, label='RFU-SS', color='g', hatch='x')
# plt.bar(x + width / 2.5,  unl_hess_r, width=width/3, label='HBU', color='tomato', hatch='-')


# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('Running Time (s)', fontsize=28)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=28)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 200.1, 40)
plt.yticks(my_y_ticks, fontsize=28)
# ax.set_yticklabels(my_y_ticks,fontsize=15)
plt.legend(loc='best', fontsize=28)
plt.xlabel('Perturbation Distance' ,fontsize=28)
# ax.bar_label(rects1, padding=1)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)
# plt.title("On MNIST", fontsize= 24)
plt.tight_layout()

plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('mnist_runningtime_noise_analysis_bar.pdf', format='pdf', dpi=200)
plt.show()
