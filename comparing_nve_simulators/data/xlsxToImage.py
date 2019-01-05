import json
import pylab
import numpy as np
from matplotlib.ticker import FuncFormatter

import matplotlib

import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import matplotlib.ticker as mtick


from pyexcel_xlsx import get_data

def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y).replace(".0", "")

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return s + r'$\%$'
    else:
        return s + '%'
    
def showImage(timing, values_1, values_2, values_3, values_4, values_5, ytxt, xtxt, title):


#     key = 'SublinkResourceUtilization'
#     
#     timing = partial_data[key][0]
#     
#     values_1 = partial_data[key][1]
#     values_2 = partial_data[key][2]
#     values_3 = partial_data[key][3]
#     values_4 = partial_data[key][4]
#     values_5 = partial_data[key][5]
    
    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
# SublinkResourceUtilization
def showSubstrateLinkNetworkResourceImage(partial_data, ytxt, xtxt, title):

    key = 'SublinkResourceUtilization'
    
    timing = partial_data[key][0]
    
    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    plt.grid(True)

    formatter = FuncFormatter(to_percent)
    plt.gca().yaxis.set_major_formatter(formatter)
    
    plt.savefig('./' + title + '.png')
    plt.show()

# # RequestEmbedding
def showVirtualNetworkRequestsImage(partial_data, ytxt, xtxt, title):
    
    key = 'RequestEmbedding'
    
    timing = partial_data[key][0]
    
    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]
    
    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    

# # FailureEmbedding
def showFailureVirtualNetworkRequestsImage(partial_data, ytxt, xtxt, title):
    
    key = 'FailureEmbedding'
    
    timing = partial_data[key][0]
    
    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]
    
    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()

# # TransportedDataVolume
def showTotalVirtualNetworksDataVolumeImage(partial_data, ytxt, xtxt, title):
    
    key = 'TransportedDataVolume'
    
    timing = partial_data[key][0]
    
    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]
    
    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
# # DataSwichingEnergy
def showTotalVirtualNetworksDataSwichingEnergyImage(partial_data, ytxt, xtxt, title):
    
    key = 'DataSwichingEnergy'
    
    timing = partial_data[key][0]
    
    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]
    
    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
# # ComTransportedDataVolume
def showCommonVirtualNetworksDataVolumeImage(partial_data, ytxt, xtxt, title):
    
    key = 'ComTransportedDataVolume'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()


# # ComDataSwichingEnergy
def showCommonVirtualNetworksDataSwichingEnergyImage(partial_data, ytxt, xtxt, title):
    
    key = 'ComDataSwichingEnergy'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()


# # SameVirNwDataSwitchingEnergy
def showSameVirtualNetworksDataSwichingEnergyImage(partial_data, ytxt, xtxt, title):
    
    key = 'SameVirNwDataSwitchingEnergy'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    

# # SameVirNwTransportedDataVolume
def showSameVirtualNetworksDataVolumeImage(partial_data, ytxt, xtxt, title):
    
    key = 'SameVirNwTransportedDataVolume'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    

# # EmbeddedNodes
def showEmbeddedVirtualNodesImage(partial_data, ytxt, xtxt, title):
    
    key = 'EmbeddedNodes'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
    
# # EmbeddedLinks
def showEmbeddedVirtualLinksImage(partial_data, ytxt, xtxt, title):
    
    key = 'EmbeddedLinks'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()


# # EmbeddedBandwidth
def showEmbeddedVirtualBandwidthImage(partial_data, ytxt, xtxt, title):

    key = 'EmbeddedBandwidth'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()

# # CurrentEndingVirNws
def showEndingVirtualNetworksImage(partial_data, ytxt, xtxt, title):

    key = 'CurrentEndingVirNws'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()


# # AmountVirNws
def showTotalEmbeddedVirtualNetworksImage(partial_data, ytxt, xtxt, title):

    key = 'AmountVirNws'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()

# # AvailableVirNws
def showAvailableVirtualNetworksImage(partial_data, ytxt, xtxt, title):

    key = 'AvailableVirNws'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
# # CurrentComVirNws
def showCommonVirtualNetworksImage(partial_data, ytxt, xtxt, title):

    key = 'CurrentComVirNws'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
    
# # CurrentSameVirNws
def showSameVirtualNetworksImage(partial_data, ytxt, xtxt, title):

    key = 'CurrentSameVirNws'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    

# # SameVirNwVNodes
def showSameVirtualNetworkNodesImage(partial_data, ytxt, xtxt, title):

    key = 'SameVirNwVNodes'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
# # SameVirNwEmbeddedLinks
def showSameVirtualNetworkLinksImage(partial_data, ytxt, xtxt, title):

    key = 'SameVirNwEmbeddedLinks'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
# # SameVirNwEmbeddedBandwidth
def showEmbeddedSameVirtualNetworkBandwidthImage(partial_data, ytxt, xtxt, title):

    key = 'SameVirNwEmbeddedBandwidth'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
# # SublinkCost
def showVirtualNetworkSubstrateCostImage(partial_data, ytxt, xtxt, title):

    key = 'SublinkCost'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
# # SameVirNwSubCost
def showSameVirtualNetworkSubstrateCostImage(partial_data, ytxt, xtxt, title):

    key = 'SameVirNwSubCost'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
# # CurrentSubLinkResourceMinInfo
def showSubstrateLinkEmbeddableBandwidthResourceLessMinImage(partial_data, ytxt, xtxt, title):
    
    key = 'CurrentSubLinkResourceMinInfo'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
    
# # EmbeddableSubLinkResourceInfo
def showSubstrateLinkEmbeddableBandwidthResourceBetweenMinAndMaxImage(partial_data, ytxt, xtxt, title):
    
    key = 'EmbeddableSubLinkResourceInfo'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
# # CurrentSubLinkResourceMaxInfo
def showSubstrateLinkEmbeddableBandwidthResourceMoreMaxImage(partial_data, ytxt, xtxt, title):

    key = 'CurrentSubLinkResourceMaxInfo'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    

# # CurrentEndingEndUserReqs
def showEnddingEnduserRequestsImage(partial_data, ytxt, xtxt, title):

    key = 'CurrentEndingEndUserReqs'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
# # CurrentEndUserRequests
def showEnduserRequestsImage(partial_data, ytxt, xtxt, title):

    key = 'CurrentEndUserRequests'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
# # CongestionRecords
def showCongestionEnduserRequestsImage(partial_data, ytxt, xtxt, title):

    key = 'CongestionRecords'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
# # CurrentCommonEndUserReqs
def showCommonEnduserRequestsImage(partial_data, ytxt, xtxt, title):

    key = 'CurrentCommonEndUserReqs'
    
    timing = partial_data[key][0]

    values_1 = partial_data[key][1]
    values_2 = partial_data[key][2]
    values_3 = partial_data[key][3]
    values_4 = partial_data[key][4]
    values_5 = partial_data[key][5]

    plt.plot(timing, values_1, label='NVE#2-No-Split', color='b')
    plt.plot(timing, values_2, label='NVE#3-SplitRatio:20%', color='g')
    plt.plot(timing, values_3, label='NVE#3-SplitRatio:30%', color='r')
    plt.plot(timing, values_4, label='NVE#3-SplitRatio:40%', color='c')
    plt.plot(timing, values_5, label='NVE#3-SplitRatio:50%', color='m')

    print plt.gca().get_ylim()
    x_limits, y_limits = plt.gca().get_ylim()
    plt.ylim(0, y_limits * 1.15)

    pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0., fontsize='small')

    plt.ylabel(ytxt)
    plt.xlabel(xtxt)
    plt.title(title)
    
    plt.grid(True)

    plt.savefig('./' + title + '.png')
    plt.show()
    
    

subname = '2017-05-0108:08:22_recordsOutput.xlsx'

partial_data = get_data("data_" + subname)

#
# # SublinkResourceUtilization
showSubstrateLinkNetworkResourceImage(partial_data,
                                       'Utilization', 'Time Unit(s)', 'Evaluation of Substrate Link Resource Utilization')


# # RequestEmbedding
showVirtualNetworkRequestsImage(partial_data,
                                 'Request(s)','Time Unit(s)','Evaluation of Virtual Network Requests')

# # FailureEmbedding
showFailureVirtualNetworkRequestsImage(partial_data,
                                        'Virtual Network(s)','Time Unit(s)','Evaluation of Failure Embedding Virtual Network(s)')


# # TransportedDataVolume
showTotalVirtualNetworksDataVolumeImage(partial_data,
                                         'Data Volume(Megabits)','Time Unit(s)','Evaluation of Total Virtual Network Switching Data Volume')

# # DataSwichingEnergy
showTotalVirtualNetworksDataSwichingEnergyImage(partial_data,
                                                 'Switching Energy(Joule)','Time Unit(s)','Evaluation of Total Virtual Network Data Switching Energy')

# # ComTransportedDataVolume
showCommonVirtualNetworksDataVolumeImage(partial_data,
                                          'Data Volume(Megabits)','Time Unit(s)','Evaluation of Common Virtual Network Switching Data Volume')

# # ComDataSwichingEnergy
showCommonVirtualNetworksDataSwichingEnergyImage(partial_data,
                                                  'Switching Energy(Joule)','Time Unit(s)','Evaluation of Common Virtural Networks'' Data Switching Energy')

# # SameVirNwDataSwitchingEnergy
showSameVirtualNetworksDataSwichingEnergyImage(partial_data,
                                                'Switching Energy(Joule)','Time Unit(s)','Evaluation of Same Virtual Network Data Switching Energy')

# # SameVirNwTransportedDataVolume
showSameVirtualNetworksDataVolumeImage(partial_data,
                                        'Data Volume(Megabits)','Time Unit(s)','Evaluation of Same Virtual Networks'' Switching Data Volume')


# # EmbeddedNodes
showEmbeddedVirtualNodesImage(partial_data,
                               'Virtual Node(s)','Time Unit(s)','Evaluation of Embedded Virtual Node(s)')

# # EmbeddedLinks
showEmbeddedVirtualLinksImage(partial_data,
                               'Virtual Link(s)','Time Unit(s)','Evaluation of Embedded Virtual Link(s)')

# # EmbeddedBandwidth
showEmbeddedVirtualBandwidthImage(partial_data,
                                   'Virtual Bandwidth(Mbps)','Time Unit(s)','Evaluation of Embedded Virtual Bandwidth')


# # CurrentEndingVirNws
showEndingVirtualNetworksImage(partial_data,
                                'Virtual Network(s)','Time Unit(s)','Evaluation of Ending Virtual Network(s)' )

# # AmountVirNws
showTotalEmbeddedVirtualNetworksImage(partial_data,
                                       'Virtual Network(s)','Time Unit(s)','Evaluation of Embedded Virtual Network(s)')

# # AvailableVirNws
showAvailableVirtualNetworksImage(partial_data,
                                   'Virtual Network(s)','Time Unit(s)','Evaluation of Available Virtual Network(s)')

# # CurrentComVirNws
showCommonVirtualNetworksImage(partial_data,
                                'Virtual Network(s)','Time Unit(s)','Evaluation of Common Virtual Networks')

# # CurrentSameVirNws
showSameVirtualNetworksImage(partial_data,
                              'Virtual Network(s)','Time Unit(s)','Evaluation of Same Virtual Networks')

# # SameVirNwVNodes
showSameVirtualNetworkNodesImage(partial_data,
                                  'Virtual Node(s)','Time Unit(s)','Evaluation of Same Virtual Network Nodes')

# # SameVirNwEmbeddedLinks
showSameVirtualNetworkLinksImage(partial_data,
                                  'Virtual Link(s)','Time Unit(s)','Evaluation of Same Virtual Network Links')

# # SameVirNwEmbeddedBandwidth
showEmbeddedSameVirtualNetworkBandwidthImage(partial_data,
                                              'Virtual Bandwidth(s)','Time Unit(s)','Evaluation of Embedded Same Virtual Network Bandwidth')

# # SublinkCost
showVirtualNetworkSubstrateCostImage(partial_data,
                                      'Cost(s)','Time Unit(s)','Evaluation of Substrate Networks Cost')

# # SameVirNwSubCost
showSameVirtualNetworkSubstrateCostImage(partial_data,
                                          'Cost(s)','Time Unit(s)','Evaluation of Same Virtual Network Cost')

# # CurrentSubLinkResourceMinInfo
showSubstrateLinkEmbeddableBandwidthResourceLessMinImage(partial_data,
                                                          'Substrate Link(s)', 'Time Unit(s)', 'Evaluation of Substrate Link Resoruce (Less than 30M)')
# # EmbeddableSubLinkResourceInfo
showSubstrateLinkEmbeddableBandwidthResourceBetweenMinAndMaxImage(partial_data,
                                                                   'Substrate Link(s)', 'Time Unit(s)', 'Evaluation of Substrate Link Resoruce (Among 30M to 100M)')

# # CurrentSubLinkResourceMaxInfo
showSubstrateLinkEmbeddableBandwidthResourceMoreMaxImage(partial_data,
                                                          'Substrate Link(s)', 'Time Unit(s)', 'Evaluation of Substrate Link Resoruce (More than 100M)')

# # CurrentEndingEndUserReqs
showEnddingEnduserRequestsImage(partial_data,
                                 'End-user Request(s)','Time Unit(s)','Evaluation of Ending End-user Requests')

# # CurrentEndUserRequests
showEnduserRequestsImage(partial_data,
                          'End-user Request(s)','Time Unit(s)','Evaluation of End-user Requests')

# # CongestionRecords
showCongestionEnduserRequestsImage(partial_data,
                                    'Congestion Time(s)','Time Unit(s)','Evaluation of End-User Request Congestion')

# # CurrentCommonEndUserReqs
showCommonEnduserRequestsImage(partial_data,
                                'End-user Request(s)','Time Unit(s)','Evaluation of Common End-user Requests')