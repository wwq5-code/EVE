import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['1%', '2%', '3%', '4%', '5%', '6%']



unl_muv_MNIST = [6.4497, 12.818  , 17.6206 , 23.850, 28.958, 33.92136]
unl_mib_MNIST = [142.6597 , 142.42  , 142.6431 , 142.9856858, 141, 143]

unl_muv_CIFAR = [2.1034, 3.93  , 5.934 , 7.2067, 9.1340, 10.7340 ]
unl_mib_CIFAR = [618.6597 , 613.42  , 620.6431 , 598.12, 594, 612]

unl_muv_CelebA = [3.7621, 7.52 , 11.141661, 14.737170, 18.0619, 21.5819]
unl_mib_CelebA = [623.582  , 641.4467 , 625.5774, 620.929, 627.0406, 625.699]



for i in range(len(labels)):
    unl_muv_MNIST[i] = unl_muv_MNIST[i]
    unl_mib_MNIST[i] = unl_mib_MNIST[i]
    unl_muv_CIFAR[i] = unl_muv_CIFAR[i]
    unl_mib_CIFAR[i] = unl_mib_CIFAR[i]
    unl_muv_CelebA[i] = unl_muv_CelebA[i]
    unl_mib_CelebA[i] = unl_mib_CelebA[i]


x = np.arange(len(labels))  # the label locations
width = 0.9

plt.style.use('seaborn')
plt.figure()

plt.bar(x - width /6 - width / 6 , unl_muv_MNIST, width=width/6, label='EUV MNIST', color='#C6B3D3', edgecolor='black', hatch='/')


plt.bar(x + width / 6  , unl_mib_MNIST,   width=width/6, label='MIB MNIST', color='#9CD1C8', edgecolor='black',  hatch='-')

plt.bar(x - width / 6 , unl_muv_CIFAR, width=width/6,  label='EUV CIFAR10', color='#F7D58B', edgecolor='black' , hatch='x')



plt.bar(x + width / 6 + width/6 , unl_mib_CIFAR, width=width/6, label='MIB CIFAR10', color='#6BB7CA', edgecolor='black', hatch='*')

plt.bar(x , unl_muv_CelebA, width=width/6, label='EUV CelebA', color='#80BA8A', edgecolor='black', hatch='o')


plt.bar(x + width / 6 + width / 6 + width/6  , unl_mib_CelebA,   width=width/6, label='MIB CelebA', color='#E58579', edgecolor='black', hatch='\\')



plt.ylabel('Running Time (s)', fontsize=20)

plt.xticks(x, labels, fontsize=20)


my_y_ticks = np.arange(0, 650, 100)
plt.yticks(my_y_ticks, fontsize=20)

plt.legend( frameon=True, facecolor='#EAEAF2', loc='best', bbox_to_anchor=(0.9601, -0.15), ncol=3, fontsize=14.6,)




plt.xlabel('$\it{ESR}$' ,fontsize=20)


plt.tight_layout()

plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('mnist_rt_sample_size_bar.pdf', format='pdf', dpi=200)
plt.show()
