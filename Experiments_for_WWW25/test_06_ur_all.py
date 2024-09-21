import numpy as np
import  matplotlib.pyplot as plt
#
# from brokenaxes import brokenaxes



plt.style.use('seaborn')

fig, ax = plt.subplots(3, 3, figsize=(10, 7)) #sharex='col',
fig.subplots_adjust(bottom=0.16)

# for i in range(2):
#     for j in range(3):
#         ax[i,j].text(0.5,0.5,str((i,j)), fontsize=18, ha='center')

#first pic 0,0


labels = ['VBU', 'RFU', 'HBU']
#unl_fr = [10*10*0.22 *5, 10*10*0.22*5, 10*10*0.22 *5, 10*10*0.22*5 , 10*10*0.22*5  , 10*10*0.22*5  ]

#unl_ss_in = [0.945938 , 0.949387 , 0.93905 , 0.94560 ]
# unl_ss_not_in = [  143, 143  , 143]


#unl_ms_in = [0.910400    , 0.91247 , 0.91605 , 0.9012468]
cap_ms_not_in = [  12.81, 13.01 , 12.74]


mib_ms_not_in = [  146 , 148 , 143]


x = np.arange(len(labels))  # the label locations
width = 0.7  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)

# plt.style.use('bmh')




#plt.subplots(figsize=(8, 5.3))
#plt.bar(x - width / 2 - width / 8 + width / 8, unl_fr, width=0.168, label='Retrain', color='dodgerblue', hatch='/')
#ax[1,2].bar(x - width /6 - width / 6  , unl_ss_in,   width=width/6, label='SS In', color='#9BC985', edgecolor='black', hatch='/')
ax[0,0].bar(x - width / 5,  cap_ms_not_in, width=width/2.5, label='SS Not In', color='#F7D58B', edgecolor='black', hatch='*')
#ax[0,0].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#E58579', edgecolor='black', hatch='/')

ax[0,0].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#B595BF', edgecolor='black', hatch='\\')


#ax[0,0].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#B595BF',edgecolor='black', hatch='\\')
#ax[1,2].bar( x + width / 6 , unl_ms_not_in, width=width/6, label='MS Not In', color='#797BB7', edgecolor='black', hatch='x')
#ax[1,2].bar(x + width / 6 + width/6 , mib_ms_in, width=width/6, label='MIB B-MS In', color='#9CD1C8', edgecolor='black', hatch='o')

# Annotate the small values
for i, v in enumerate(cap_ms_not_in):
    ax[0,0].text(x[i] - width / 5, v + 1, f"{v}", ha='center', color='black')

for i, v in enumerate(mib_ms_not_in):
    ax[0,0].text(x[i] + width / 5, v + 1, f"{v}", ha='center', color='black')

#ax[0,0].bar(x + width / 3 , mib_ms_not_in,   width=width/3, label='MIB B-MS Not In', color='#E58579', edgecolor='black', hatch='/')



# plt.bar(x - width / 2.5 ,  unl_br, width=width/3, label='VBU', color='orange', hatch='\\')
# plt.bar(x,unl_self_r, width=width/3, label='RFU-SS', color='g', hatch='x')
# plt.bar(x + width / 2.5,  unl_hess_r, width=width/3, label='HBU', color='tomato', hatch='-')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax[0,0].set_ylabel('Running Time', fontsize=16)
# ax.set_title('Performance of Different Users n')
ax[0,0].set_xticks(x)
ax[0,0].set_xticklabels(labels ,fontsize=13)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 160.01, 40)
ax[0,0].set_yticks(my_y_ticks )
ax[0,0].set_ylim(0, 160.02)
# plt.ylim()
# ax.set_yticklabels(my_y_ticks,fontsize=15)
ax[0,0].set_title('On MNIST', fontsize=16)

# figure 1,1



labels = [ 'VBU', 'RFU', 'HBU']
#unl_fr = [10*10*0.22 *5, 10*10*0.22*5, 10*10*0.22 *5, 10*10*0.22*5 , 10*10*0.22*5  , 10*10*0.22*5  ]

#unl_ss_in = [0.945938 , 0.949387 , 0.93905 , 0.94560 ]
# unl_ss_not_in = [  135 , 135  , 135]


#unl_ms_in = [0.910400    , 0.91247 , 0.91605 , 0.9012468]
cap_ms_not_in = [  3.93, 4.11 , 3.82]


mib_ms_not_in = [  613 , 617 , 607]



x = np.arange(len(labels))  # the label locations
width = 0.7  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)

# plt.style.use('bmh')


# Plot the bars
ax[0,1].bar(x - width / 5, cap_ms_not_in, width=width/2.5, label='SS Not In', color='#F7D58B', edgecolor='black', hatch='*')
#ax[0,1].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#E58579', edgecolor='black', hatch='/')

ax[0,1].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#B595BF', edgecolor='black', hatch='\\')

# Annotate the small values
for i, v in enumerate(cap_ms_not_in):
    ax[0,1].text(x[i] - width / 5, v + 1, f"{v}", ha='center', color='black')

for i, v in enumerate(mib_ms_not_in):
    ax[0,1].text(x[i] + width / 5, v + 1, f"{v}", ha='center', color='black')


# ax[0,1].bar(x - width / 5,  cap_ms_not_in, width=width/2.5, label='SS Not In', color='#F7D58B', edgecolor='black', hatch='*')
# ax[0,1].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#B595BF',edgecolor='black', hatch='\\')


# Add some text for labels, title and custom x-axis tick labels, etc.
# ax[0,1].set_ylabel('Running Time', fontsize=16)
# ax.set_title('Performance of Different Users n')
ax[0,1].set_xticks(x)
ax[0,1].set_xticklabels(labels ,fontsize=13)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 700.01, 100)
ax[0,1].set_yticks(my_y_ticks )
ax[0,1].set_ylim(0, 700.02)
# plt.ylim()
# ax.set_yticklabels(my_y_ticks,fontsize=15)
ax[0,1].set_title('On CIFAR10', fontsize=16)





#figure 1,2


labels = [  'VBU', 'RFU', 'HBU']
#unl_fr = [10*10*0.22 *5, 10*10*0.22*5, 10*10*0.22 *5, 10*10*0.22*5 , 10*10*0.22*5  , 10*10*0.22*5  ]

#unl_ss_in = [0.945938 , 0.949387 , 0.93905 , 0.94560 ]
# unl_ss_not_in = [ 32.76  , 32.76   , 32.76 ]
#

#unl_ms_in = [0.910400    , 0.91247 , 0.91605 , 0.9012468]
cap_ms_not_in = [  7.52, 7.83 , 7.47]


mib_ms_not_in = [ 641 , 652 , 622]


x = np.arange(len(labels))  # the label locations
width = 0.7  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)

# plt.style.use('bmh')




# Plot the bars
ax[0,2].bar(x - width / 5, cap_ms_not_in, width=width/2.5, label='SS Not In', color='#F7D58B', edgecolor='black', hatch='*')
#ax[0,2].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#E58579', edgecolor='black', hatch='/')

ax[0,2].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#B595BF', edgecolor='black', hatch='\\')

# Annotate the small values
for i, v in enumerate(cap_ms_not_in):
    ax[0,2].text(x[i] - width / 5, v + 1, f"{v}", ha='center', color='black')

for i, v in enumerate(mib_ms_not_in):
    ax[0,2].text(x[i] + width / 5, v + 1, f"{v}", ha='center', color='black')



# plt.bar(x - width / 2.5 ,  unl_br, width=width/3, label='VBU', color='orange', hatch='\\')
# plt.bar(x,unl_self_r, width=width/3, label='RFU-SS', color='g', hatch='x')
# plt.bar(x + width / 2.5,  unl_hess_r, width=width/3, label='HBU', color='tomato', hatch='-')


# Add some text for labels, title and custom x-axis tick labels, etc.
# ax[0,1].set_ylabel('Running Time', fontsize=16)
# ax.set_title('Performance of Different Users n')
ax[0,2].set_xticks(x)
ax[0,2].set_xticklabels(labels ,fontsize=13)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 799.01, 100)
ax[0,2].set_yticks(my_y_ticks )
ax[0,2].set_ylim(0, 700.02)
# plt.ylim()
# ax.set_yticklabels(my_y_ticks,fontsize=15)
ax[0,2].set_title('On CelebA', fontsize=16)


#figure 1,0



labels = [  'VBU', 'RFU', 'HBU']
#unl_fr = [10*10*0.22 *5, 10*10*0.22*5, 10*10*0.22 *5, 10*10*0.22*5 , 10*10*0.22*5  , 10*10*0.22*5  ]

#unl_ss_in = [0.945938 , 0.949387 , 0.93905 , 0.94560 ]
cap_ms_not_in = [  1.0   , 1.0   , 1.0]


#unl_ms_in = [0.910400    , 0.91247 , 0.91605 , 0.9012468]
mib_ms_not_in = [  1.0 , 1.0  , 1.0]



x = np.arange(len(labels))  # the label locations
width = 0.7  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)

# plt.style.use('bmh')


# Plot the bars
ax[1,0].bar(x - width / 5, cap_ms_not_in, width=width/2.5, label='SS Not In', color='#F7D58B', edgecolor='black', hatch='*')
#ax[1,0].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#E58579', edgecolor='black', hatch='/')

ax[1,0].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#B595BF', edgecolor='black', hatch='\\')

# Annotate the small values
# for i, v in enumerate(cap_ms_not_in):
#     ax[1,0].text(x[i] - width / 5, v + 1, f"{v}", ha='center', color='black')
#
# for i, v in enumerate(mib_ms_not_in):
#     ax[1,0].text(x[i] + width / 5, v + 1, f"{v}", ha='center', color='black')

# plt.bar(x - width / 2.5 ,  unl_br, width=width/3, label='VBU', color='orange', hatch='\\')
# plt.bar(x,unl_self_r, width=width/3, label='RFU-SS', color='g', hatch='x')
# plt.bar(x + width / 2.5,  unl_hess_r, width=width/3, label='HBU', color='tomato', hatch='-')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax[1,0].set_ylabel('Verifiability', fontsize=16)
# ax.set_title('Performance of Different Users n')
ax[1,0].set_xticks(x)
ax[1,0].set_xticklabels(labels ,fontsize=13)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0.68, 1.11, 0.08)
ax[1,0].set_yticks(my_y_ticks )
ax[1,0].set_ylim(0.68, 1.12)
# plt.ylim()
# ax.set_yticklabels(my_y_ticks,fontsize=15)
# ax[1,0].set_title('On MNIST', fontsize=16)

# figure 1,1




labels = [ 'VBU', 'RFU', 'HBU']
#unl_fr = [10*10*0.22 *5, 10*10*0.22*5, 10*10*0.22 *5, 10*10*0.22*5 , 10*10*0.22*5  , 10*10*0.22*5  ]

#unl_ss_in = [0.972845 , 0.973203, 0.97236328 -0.001 , 0.9731583-0.001]
cap_ms_not_in = [ 1.0 , 1.0  , 1.0]


#unl_ms_in = [0.96839   ,0.969446  , 0.96787 -0.001, 0.968382 -0.001]
mib_ms_not_in = [  1.0 , 1.0  , 1.0 ]




x = np.arange(len(labels))  # the label locations
width = 0.7  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)

# plt.style.use('bmh')



# Plot the bars
ax[1,1].bar(x - width / 5, cap_ms_not_in, width=width/2.5, label='SS Not In', color='#F7D58B', edgecolor='black', hatch='*')
#ax[1,1].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#E58579', edgecolor='black', hatch='/')

ax[1,1].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#B595BF', edgecolor='black', hatch='\\')

# Annotate the small values
# for i, v in enumerate(cap_ms_not_in):
#     ax[1,1].text(x[i] - width / 5, v + 1, f"{v}", ha='center', color='black')
#
# for i, v in enumerate(mib_ms_not_in):
#     ax[1,1].text(x[i] + width / 5, v + 1, f"{v}", ha='center', color='black')

# plt.bar(x - width / 2.5 ,  unl_br, width=width/3, label='VBU', color='orange', hatch='\\')
# plt.bar(x,unl_self_r, width=width/3, label='RFU-SS', color='g', hatch='x')
# plt.bar(x + width / 2.5,  unl_hess_r, width=width/3, label='HBU', color='tomato', hatch='-')


# Add some text for labels, title and custom x-axis tick labels, etc.
# ax[1,1].set_ylabel('Rec. Similarity', fontsize=20)
# ax.set_title('Performance of Different Users n')
ax[1,1].set_xticks(x)
ax[1,1].set_xticklabels(labels ,fontsize=13)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0.68, 1.11, 0.08)
ax[1,1].set_yticks(my_y_ticks )
ax[1,1].set_ylim(0.68, 1.12)
# ax[1,1].set_title('On CIFAR10', fontsize=16)





#figure 1,2



labels = [  'VBU', 'RFU', 'HBU']
#unl_fr = [10*10*0.22 *5, 10*10*0.22*5, 10*10*0.22 *5, 10*10*0.22*5 , 10*10*0.22*5  , 10*10*0.22*5  ]

#unl_ss_in = [0.97557 , 0.976940, 0.97633 -0.001, 0.977246 -0.001]
cap_ms_not_in = [  1.0  , 1.0   , 1.0 ]


#unl_ms_in = [0.968087   , 0.9652563  , 0.967717-0.001, 0.9661944-0.001]
mib_ms_not_in = [  0.9289 , 0.9297 , 0.9110 ]



x = np.arange(len(labels))  # the label locations
width = 0.7  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)

# plt.style.use('bmh')




# Plot the bars
ax[1,2].bar(x - width / 5, cap_ms_not_in, width=width/2.5, label='SS Not In', color='#F7D58B', edgecolor='black', hatch='*')
#ax[1,2].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#E58579', edgecolor='black', hatch='/')


ax[1,2].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#B595BF', edgecolor='black', hatch='\\')

# Annotate the small values
# for i, v in enumerate(cap_ms_not_in):
#     ax[1,2].text(x[i] - width / 5, v + 1, f"{v}", ha='center', color='black')
#
# for i, v in enumerate(mib_ms_not_in):
#     ax[1,2].text(x[i] + width / 5, v + 1, f"{v}", ha='center', color='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
# ax[1,1].set_ylabel('Rec. Similarity', fontsize=20)
# ax.set_title('Performance of Different Users n')
ax[1,2].set_xticks(x)
ax[1,2].set_xticklabels(labels ,fontsize=13)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0.68, 1.11, 0.08)
ax[1,2].set_yticks(my_y_ticks )
ax[1,2].set_ylim(0.68, 1.12)
# ax[1,1].set_title('On CIFAR10', fontsize=16)







labels = ['VBU', 'RFU', 'HBU']
#unl_fr = [10*10*0.22 *5, 10*10*0.22*5, 10*10*0.22 *5, 10*10*0.22*5 , 10*10*0.22*5  , 10*10*0.22*5  ]

#unl_ss_in = [0.3100  , 0.2700 , 0.2837 , 0.2603 ]
# unl_ss_not_in = [  0.991907 , 0.996957     , 0.993923]


#unl_ms_in = [0.2020    , 0.1833  , 0.1737, 0.1707]
cap_ms_not_in = [  0.97691 , 0.97886  , 0.97897]

#mib_ms_in = [0,0,0,0]
mib_ms_not_in = [0.9751, 0.97571, 0.97473]



x = np.arange(len(labels))  # the label locations
width = 0.7  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)

# plt.style.use('bmh')




# Plot the bars
ax[2,0].bar(x - width / 5, cap_ms_not_in, width=width/2.5, label='SS Not In', color='#F7D58B', edgecolor='black', hatch='*')
#ax[2,0].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#E58579', edgecolor='black', hatch='/')

ax[2,0].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#B595BF', edgecolor='black', hatch='\\')

# Annotate the small values
# for i, v in enumerate(cap_ms_not_in):
#     ax[2,0].text(x[i] - width / 5, v + 1, f"{v}", ha='center', color='black')
#
# for i, v in enumerate(mib_ms_not_in):
#     ax[2,0].text(x[i] + width / 5, v + 1, f"{v}", ha='center', color='black')

# plt.bar(x - width / 2.5 ,  unl_br, width=width/3, label='VBU', color='orange', hatch='\\')
# plt.bar(x,unl_self_r, width=width/3, label='RFU-SS', color='g', hatch='x')
# plt.bar(x + width / 2.5,  unl_hess_r, width=width/3, label='HBU', color='tomato', hatch='-')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax[2,0].set_ylabel('Accuracy', fontsize=16)
# ax.set_title('Performance of Different Users n')
ax[2,0].set_xticks(x)
ax[2,0].set_xticklabels(labels ,fontsize=13)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0.68, 1.01, 0.08)
ax[2,0].set_yticks(my_y_ticks )
ax[2,0].set_ylim(0.68, 1.02)
# ax[2,0].set_ylim(0.5,1.2)
# plt.ylim()
# ax.set_yticklabels(my_y_ticks,fontsize=15)




#figure 2,1



labels = [  'VBU', 'RFU', 'HBU']
#unl_fr = [10*10*0.22 *5, 10*10*0.22*5, 10*10*0.22 *5, 10*10*0.22*5 , 10*10*0.22*5  , 10*10*0.22*5  ]

#unl_ss_in = [0.0708 , 0.0528 , 0.0516 , 0.0760]
cap_ms_not_in = [  0.7935  , 0.7933   , 0.7952]


#unl_ms_in = [0.0628   , 0.0096 ,  0.0112 , 0.0188]
mib_ms_not_in = [  0.7736, 0.7748  , 0.7733]



x = np.arange(len(labels))  # the label locations
width = 0.7  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)

# plt.style.use('bmh')




# Plot the bars
ax[2,1].bar(x - width / 5, cap_ms_not_in, width=width/2.5, label='SS Not In', color='#F7D58B', edgecolor='black', hatch='*')
#ax[2,1].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#E58579', edgecolor='black', hatch='/')

ax[2,1].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#B595BF', edgecolor='black', hatch='\\')


# plt.bar(x - width /6 - width / 6 , unl_muv_MNIST, width=width/6, label='MUV MNIST', color='#C6B3D3', edgecolor='black', hatch='/')
#
# plt.bar(x - width / 6 , unl_muv_CIFAR, width=width/6,  label='MUV CIFAR10', color='#F1DFA4', edgecolor='black' , hatch='x')
# plt.bar(x , unl_muv_CelebA, width=width/6, label='MUV CelebA', color='#80BA8A', edgecolor='black', hatch='o')
#
#
# plt.bar(x + width / 6  , unl_mib_MNIST,   width=width/6, label='MIB MNIST', color='#9CD1C8', edgecolor='black',  hatch='-')
#


# plt.bar(x - width / 2.5 ,  unl_br, width=width/3, label='VBU', color='orange', hatch='\\')
# plt.bar(x,unl_self_r, width=width/3, label='RFU-SS', color='g', hatch='x')
# plt.bar(x + width / 2.5,  unl_hess_r, width=width/3, label='HBU', color='tomato', hatch='-')


# Add some text for labels, title and custom x-axis tick labels, etc.
# ax[2,0].set_ylabel('Verifiability', fontsize=20)
# ax.set_title('Performance of Different Users n')
ax[2,1].set_xticks(x)
ax[2,1].set_xticklabels(labels ,fontsize=13)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0.68-0.16, 1.01-0.16, 0.08)
ax[2,1].set_yticks(my_y_ticks )
ax[2,1].set_ylim(0.68-0.16, 1.02-0.16)

# plt.ylim()
# ax.set_yticklabels(my_y_ticks,fontsize=15)


#figure 2, 2



labels = ['VBU', 'RFU', 'HBU']
#unl_fr = [10*10*0.22 *5, 10*10*0.22*5, 10*10*0.22 *5, 10*10*0.22*5 , 10*10*0.22*5  , 10*10*0.22*5  ]

#unl_ss_in = [0.1591  , 0.1496 , 0.1762 , 0.1445 ]
cap_ms_not_in = [0.9584 , 0.9586 , 0.9582]


#unl_ms_in = [0.0984     , 0.1055 , 0.0994 , 0.0881]
mib_ms_not_in = [0.9579, 0.9588  , 0.9579]





x = np.arange(len(labels))  # the label locations
width = 0.7  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)

# plt.style.use('bmh')




# Plot the bars
ax[2,2].bar(x - width / 5, cap_ms_not_in, width=width/2.5, label='CAP', color='#F7D58B', edgecolor='black', hatch='*')
#ax[2,2].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MS In', color='#E58579', edgecolor='black', hatch='/')

ax[2,2].bar(x + width / 5, mib_ms_not_in, width=width/2.5, label='MIB', color='#B595BF', edgecolor='black', hatch='\\')



# plt.bar(x - width / 2.5 ,  unl_br, width=width/3, label='VBU', color='orange', hatch='\\')
# plt.bar(x,unl_self_r, width=width/3, label='RFU-SS', color='g', hatch='x')
# plt.bar(x + width / 2.5,  unl_hess_r, width=width/3, label='HBU', color='tomato', hatch='-')


# Add some text for labels, title and custom x-axis tick labels, etc.
# ax[2,0].set_ylabel('Verifiability', fontsize=20)
# ax.set_title('Performance of Different Users n')
ax[2,2].set_xticks(x)
ax[2,2].set_xticklabels(labels ,fontsize=13)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0.68, 1.01, 0.08)
ax[2,2].set_yticks(my_y_ticks )
ax[2,2].set_ylim(0.68, 1.02)
# plt.ylim()
# ax.set_yticklabels(my_y_ticks,fontsize=15)




handles, labels = ax[2,2].get_legend_handles_labels()
# Create a "dummy" handle for the legend title
# title_handle = plt.Line2D([], [], color='none', label='Method')
#
# # Insert the title handle at the beginning of the handles list
# handles = [title_handle] + handles
# handles.insert(1, title_handle)
# labels = [''] + labels
# labels.insert(1, '')

fig.legend(handles, labels, frameon=True, facecolor='#EAEAF2', loc='lower center', ncol=4, bbox_to_anchor=(0.5, 0.03),fontsize=16)

# plt.legend( title = 'Methods and Datasets',frameon=True, facecolor='white', loc='best',
#            ncol=2, mode="expand", framealpha=0.5, borderaxespad=0., fontsize=20, title_fontsize=20)

# fig.tight_layout()
plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('test_06_all.pdf', dpi=200,bbox_inches='tight')

plt.show()