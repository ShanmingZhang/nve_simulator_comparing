import json
import pylab
import numpy as np
from matplotlib.ticker import FuncFormatter

import matplotlib

import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import matplotlib.ticker as mtick

subname = '2017-04-1809:09:06_recordsOutput.json'


nve_1_file = 'NVE#1_' + subname

nve_2_file = 'NVE#3_20_' + subname

nve_3_file = 'NVE#3_30_' + subname

nve_4_file = 'NVE#3_40_' + subname

nve_5_file = 'NVE#3_50_' + subname


def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return s + r'$\%$'
    else:
        return s + '%'

def showImage( key, record_1, record_2, record_3, record_4, record_5, ytxt, xtxt, title):
	timing_1 = []
	timing_2 = []
	timing_3 = []
	timing_4 = []
	timing_5 = []

	values_1 = []
	values_2 = []
	values_3 = []
	values_4 = []
	values_5 = []

	for item in record_1[key]:

		timing_1.append(item['Timing'])
		values_1.append(item['Total'])

	for item in record_2[key]:

		timing_2.append(item['Timing'])
		values_2.append(item['Total'])


	for item in record_3[key]:

		timing_3.append(item['Timing'])
		values_3.append(item['Total'])


	for item in record_4[key]:

		timing_4.append(item['Timing'])
		values_4.append(item['Total'])


	for item in record_5[key]:

		timing_5.append(item['Timing'])
		values_5.append(item['Total'])

	print len(timing_1)
	print timing_1
	print len(values_1)
	print values_1
	print len(timing_2)
	print timing_2
	print len(values_2)
	print values_2
	print len(timing_3)
	print timing_3
	print len(values_3)
	print values_3
	print len(timing_4)
	print timing_4
	print len(values_4)
	print values_4
	print len(timing_5)
	print timing_5
	print len(values_5)
	print values_5

	plt.plot(timing_1, values_1,label='NVE#1-No-Split', color='b' )
	plt.plot(timing_2, values_2,label='NVE#3-SplitRatio:20%', color='g' )
	plt.plot(timing_3, values_3,label='NVE#3-SplitRatio:30%', color='r' )
	plt.plot(timing_4, values_4,label='NVE#3-SplitRatio:40%', color='c' )
	plt.plot(timing_5, values_5,label='NVE#3-SplitRatio:50%', color='m')

	print plt.gca().get_ylim()
	x_limits, y_limits = plt.gca().get_ylim()
	plt.ylim(0, y_limits * 1.15 )

	pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='small')

	plt.ylabel(ytxt)
	plt.xlabel(xtxt)
	plt.title(title)
	plt.grid(True)

	plt.savefig('./'+ title + '.png')
	plt.show()

	del timing_1[:]
	del timing_2[:]
	del timing_3[:]
	del timing_4[:]
	del timing_5[:]

	del values_1[:]
	del values_2[:]
	del values_3[:]
	del values_4[:]
	del values_5[:]

# key_1 : FailureEmbedding
# key_1 : RequestEmbedding
# AccetpionRatio = 1 - FailureEmbedding / RequestEmbedding
def showAllAcceptionRatioImage( key_1, key_2, limits, record_1, record_2, record_3, record_4, record_5, ytxt, xtxt, title):
	timing_1 = []
	timing_2 = []
	timing_3 = []
	timing_4 = []
	timing_5 = []

	values_1 = []
	values_2 = []
	values_3 = []
	values_4 = []
	values_5 = []


	
	timing_1.append(0)
	timing_2.append(0)
	timing_3.append(0)
	timing_4.append(0)
	timing_5.append(0)

	values_1.append(1)
	values_2.append(1)
	values_3.append(1)
	values_4.append(1)
	values_5.append(1)

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_1[key_1], record_1[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_1.append(index)
			values_1.append(1- (float(sum_1)/float(sum_2)))
			sum_1 = 0
			sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_2[key_1], record_2[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_2.append(index)
			values_2.append(1- (float(sum_1)/float(sum_2)))
			sum_1 = 0
			sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_3[key_1], record_3[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_3.append(index)
			values_3.append(1- (float(sum_1)/float(sum_2)))
			sum_1 = 0
			sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_4[key_1], record_4[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_4.append(index)
			values_4.append(1- (float(sum_1)/float(sum_2)))
			sum_1 = 0
			sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_5[key_1], record_5[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_5.append(index)
			values_5.append(1- (float(sum_1)/float(sum_2)))
			sum_1 = 0
			sum_2 = 0


	print len(timing_1)
	print timing_1
	print len(values_1)
	print values_1
	print len(timing_2)
	print timing_2
	print len(values_2)
	print values_2
	print len(timing_3)
	print timing_3
	print len(values_3)
	print values_3
	print len(timing_4)
	print timing_4
	print len(values_4)
	print values_4
	print len(timing_5)
	print timing_5
	print len(values_5)
	print values_5

	plt.plot(timing_1, values_1,label='NVE#1-No-Split',marker='o', markersize=3, color='b' )
	plt.plot(timing_2, values_2,label='NVE#3-SplitRatio:20%',marker='o', markersize=3, color='g' )
	plt.plot(timing_3, values_3,label='NVE#3-SplitRatio:30%',marker='o', markersize=3, color='r' )
	plt.plot(timing_4, values_4,label='NVE#3-SplitRatio:40%',marker='o', markersize=3, color='c' )
	plt.plot(timing_5, values_5,label='NVE#3-SplitRatio:50%',marker='o', markersize=3, color='m')

	pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='small')

	plt.ylabel(ytxt)
	plt.xlabel(xtxt)
	plt.title(title)

	plt.grid(True)
	
	print plt.gca().get_ylim()
	x_limits, y_limits = plt.gca().get_ylim()
	plt.ylim(0, y_limits * 1.15 )

	formatter = FuncFormatter(to_percent)
	plt.gca().yaxis.set_major_formatter(formatter)

	plt.savefig('./'+ title + '.png')
	plt.show()

	del timing_1[:]
	del timing_2[:]
	del timing_3[:]
	del timing_4[:]
	del timing_5[:]

	del values_1[:]
	del values_2[:]
	del values_3[:]
	del values_4[:]
	del values_5[:]


# key_1 : FailureEmbedding
# key_1 : RequestEmbedding
# AccetpionRatio = 1 - FailureEmbedding / RequestEmbedding
def showTwoAcceptionRatioImage( key_1, key_2, limits, record_1, record_2, ytxt, xtxt, title, ratio):
	timing_1 = []
	timing_2 = []

	values_1 = []
	values_2 = []

	
	timing_1.append(0)
	timing_2.append(0)

	values_1.append(1)
	values_2.append(1)


	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_1[key_1], record_1[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_1.append(index)
			values_1.append(1- (float(sum_1)/float(sum_2)))
			sum_1 = 0
			sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_2[key_1], record_2[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_2.append(index)
			values_2.append(1- (float(sum_1)/float(sum_2)))
			sum_1 = 0
			sum_2 = 0

	print len(timing_1)
	print timing_1
	print len(values_1)
	print values_1
	print len(timing_2)
	print timing_2
	print len(values_2)
	print values_2

	col = 'y'
	if ratio == '20':
		col = 'g'

	if ratio == '30':
		col = 'r'

	if ratio == '40':
		col = 'c'

	if ratio == '50':
		col = 'm'

	plt.plot(timing_1, values_1,label='NVE#1-No-Split',marker='o', markersize=3, color='b' )
	plt.plot(timing_2, values_2,label='NVE#3-SplitRatio:' + ratio + '%',marker='o', markersize=3, color=col )

	pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='small')

	plt.ylabel(ytxt)
	plt.xlabel(xtxt)
	plt.title(title)

	plt.grid(True)
	
	print plt.gca().get_ylim()
	x_limits, y_limits = plt.gca().get_ylim()
	plt.ylim(0, y_limits * 1.15 )

	formatter = FuncFormatter(to_percent)
	plt.gca().yaxis.set_major_formatter(formatter)

	plt.savefig('./'+ title + '_' + ratio + '.png')
	plt.show()

	del timing_1[:]
	del timing_2[:]

	del values_1[:]
	del values_2[:]


# key_1 : EmbeddedBandwidth
# key_2 : EmbeddedNodes (1 vnode : 1 cpu)
# VirNwsRevenue = EmbeddedBandwidth + sum(embeddedNodes'cpu)
def showTwoVirNwsRevenueImage( key_1, key_2, limits, record_1, record_2, ytxt, xtxt, title, ratio):
	timing_1 = []
	timing_2 = []

	values_1 = []
	values_2 = []

	timing_1.append(0)
	timing_2.append(0)

	values_1.append(0)
	values_2.append(0)

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_1[key_1], record_1[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_1.append(index)
			values_1.append( float(sum_1 + sum_2) / float(limits) )
			sum_1 = 0
			sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_2[key_1], record_2[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_2.append(index)
			values_2.append(float(sum_1 + sum_2) / float(limits))
			sum_1 = 0
			sum_2 = 0

	print len(timing_1)
	print timing_1
	print len(values_1)
	print values_1
	print len(timing_2)
	print timing_2
	print len(values_2)
	print values_2

	col = 'y'
	if ratio == '20':
		col = 'g'

	if ratio == '30':
		col = 'r'

	if ratio == '40':
		col = 'c'

	if ratio == '50':
		col = 'm'

	plt.plot(timing_1, values_1,label='NVE#1-No-Split',marker='o', markersize=3, color='b' )
	plt.plot(timing_2, values_2,label='NVE#3-SplitRatio:' + ratio + '%',marker='o', markersize=3, color=col )

	pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='small')

	plt.ylabel(ytxt)
	plt.xlabel(xtxt)
	plt.title(title)

	plt.grid(True)
	
	print plt.gca().get_ylim()
	x_limits, y_limits = plt.gca().get_ylim()
	plt.ylim(0, y_limits * 1.15 )

	plt.savefig('./'+ title + '_' + ratio + '.png')
	plt.show()

	del timing_1[:]
	del timing_2[:]

	del values_1[:]
	del values_2[:]

# key_1 : SublinkCost
# key_2 : EmbeddedNodes (1 vnode : 1 cpu)
# VirNwsCost = EmbeddedBandwidth + sum(embeddedNodes'cpu)
def showTwoVirNwsSubCostImage( key_1, key_2, limits, record_1, record_2, ytxt, xtxt, title, ratio):
	timing_1 = []
	timing_2 = []

	values_1 = []
	values_2 = []

	timing_1.append(0)
	timing_2.append(0)

	values_1.append(0)
	values_2.append(0)

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_1[key_1], record_1[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_1.append(index)
			values_1.append( float(sum_1 + sum_2) / float(limits) )
			sum_1 = 0
			sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_2[key_1], record_2[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_2.append(index)
			values_2.append(float(sum_1 + sum_2) / float(limits))
			sum_1 = 0
			sum_2 = 0

	print len(timing_1)
	print timing_1
	print len(values_1)
	print values_1
	print len(timing_2)
	print timing_2
	print len(values_2)
	print values_2

	col = 'y'
	if ratio == '20':
		col = 'g'

	if ratio == '30':
		col = 'r'

	if ratio == '40':
		col = 'c'

	if ratio == '50':
		col = 'm'

	plt.plot(timing_1, values_1,label='NVE#1-No-Split',marker='o', markersize=3, color='b' )
	plt.plot(timing_2, values_2,label='NVE#3-SplitRatio:' + ratio + '%',marker='o', markersize=3, color=col )

	pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='small')

	plt.ylabel(ytxt)
	plt.xlabel(xtxt)
	plt.title(title)

	plt.grid(True)
	
	print plt.gca().get_ylim()
	x_limits, y_limits = plt.gca().get_ylim()
	plt.ylim(0, y_limits * 1.15 )

	plt.savefig('./'+ title + '_' + ratio + '.png')
	plt.show()

	del timing_1[:]
	del timing_2[:]

	del values_1[:]
	del values_2[:]


#key_1 = 'EmbeddedBandwidth', 
#key_2 = 'EmbeddedNodes'
#key_11 = 'SublinkCost'
#key_22 = 'EmbeddedNodes'
#Revenue to subcost = Revenue / SubCost
## key_1 and key_2 to calculate revenue
## key_11 and key_22 to calcuate subcost

def showTowVirNwsRevenueToSubCostImage( key_1, key_2, key_11, key_22, limits, record_1, record_2, ytxt, xtxt, title, ratio):
	timing_1 = []
	timing_2 = []

	values_1 = []
	values_2 = []

	timing_1.append(0)
	timing_2.append(0)

	values_1.append(0)
	values_2.append(0)

	sum_1 = 0
	sum_2 = 0
	sum_3 = 0
	sum_4 = 0

	index = 0
	for item_1, item_2, item_11, item_22 in zip(record_1[key_1], record_1[key_2],record_1[key_11], record_1[key_22]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		sum_3 = sum_3 + item_11['Total']
		sum_4 = sum_4 + item_22['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_1.append(index)
			if float(sum_1 + sum_2) == 0.0 or float(sum_3 + sum_4) == 0.0:
				values_1.append( 0.0 )
			else:
				
				values_1.append(  float(sum_1 + sum_2) / float(sum_3 + sum_4) )
			sum_1 = 0
			sum_2 = 0
			sum_3 = 0
			sum_4 = 0

	sum_1 = 0
	sum_2 = 0
	sum_3 = 0
	sum_4 = 0

	index = 0
	for item_1, item_2, item_11, item_22 in zip(record_2[key_1], record_2[key_2],record_2[key_11], record_2[key_22]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		sum_3 = sum_3 + item_11['Total']
		sum_4 = sum_4 + item_22['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_2.append(index)
			if float(sum_1 + sum_2) == 0.0 or float(sum_3 + sum_4) == 0.0:
				values_2.append( 0.0 )
			else:
				
				values_2.append(  float(sum_1 + sum_2) / float(sum_3 + sum_4) )
			sum_1 = 0
			sum_2 = 0
			sum_3 = 0
			sum_4 = 0


	print len(timing_1)
	print timing_1
	print len(values_1)
	print values_1
	print len(timing_2)
	print timing_2
	print len(values_2)
	print values_2


	col = 'y'
	if ratio == '20':
		col = 'g'

	if ratio == '30':
		col = 'r'

	if ratio == '40':
		col = 'c'

	if ratio == '50':
		col = 'm'

	plt.plot(timing_1, values_1,label='NVE#1-No-Split',marker='o', markersize=3, color='b' )
	plt.plot(timing_2, values_2,label='NVE#3-SplitRatio:' + ratio + '%',marker='o', markersize=3, color=col )

	pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='small')

	plt.ylabel(ytxt)
	plt.xlabel(xtxt)
	plt.title(title)

	plt.grid(True)
	
	print plt.gca().get_ylim()
	x_limits, y_limits = plt.gca().get_ylim()
	plt.ylim(0, y_limits * 1.15 )


	formatter = FuncFormatter(to_percent)
	plt.gca().yaxis.set_major_formatter(formatter)

	plt.savefig('./'+ title + '_' + ratio + '.png')
	plt.show()

	del timing_1[:]
	del timing_2[:]

	del values_1[:]
	del values_2[:]


# key_1 : DataSwichingEnergy
def showTwoVirNwsSwitchingEnergyImage(  key_1, limits, record_1, record_2, ytxt, xtxt, title, ratio ):
	timing_1 = []
	timing_2 = []

	values_1 = []
	values_2 = []


	
	timing_1.append(0)
	timing_2.append(0)

	values_1.append(0)
	values_2.append(0)

	sum_1 = 0
	index = 0
	for item_1 in record_1[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_1.append(index)
			values_1.append(float(sum_1) / float(limits))
			sum_1 = 0

	sum_1 = 0
	index = 0
	for item_1 in record_2[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_2.append(index)
			values_2.append(float(sum_1) / float(limits))
			sum_1 = 0

	

	print len(timing_1)
	print timing_1
	print len(values_1)
	print values_1
	print len(timing_2)
	print timing_2
	print len(values_2)
	print values_2

	col = 'y'
	if ratio == '20':
		col = 'g'

	if ratio == '30':
		col = 'r'

	if ratio == '40':
		col = 'c'

	if ratio == '50':
		col = 'm'

	plt.plot(timing_1, values_1,label='NVE#1-No-Split',marker='o', markersize=3, color='b' )
	plt.plot(timing_2, values_2,label='NVE#3-SplitRatio:' + ratio + '%',marker='o', markersize=3, color=col )

	pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='small')

	plt.ylabel(ytxt)
	plt.xlabel(xtxt)
	plt.title(title)

	plt.grid(True)
	
	print plt.gca().get_ylim()
	x_limits, y_limits = plt.gca().get_ylim()
	plt.ylim(0, y_limits * 1.15 )

	plt.savefig('./'+ title + '_' + ratio + '.png')
	plt.show()


	del timing_1[:]
	del timing_2[:]

	del values_1[:]
	del values_2[:]

# key_1 : EmbeddedBandwidth
# key_2 : EmbeddedNodes (1 vnode : 1 cpu)
# VirNwsRevenue = EmbeddedBandwidth + sum(embeddedNodes'cpu)
def showAllVirNwsRevenueImage( key_1, key_2, limits, record_1, record_2, record_3, record_4, record_5, ytxt, xtxt, title):
	timing_1 = []
	timing_2 = []
	timing_3 = []
	timing_4 = []
	timing_5 = []

	values_1 = []
	values_2 = []
	values_3 = []
	values_4 = []
	values_5 = []


	
	timing_1.append(0)
	timing_2.append(0)
	timing_3.append(0)
	timing_4.append(0)
	timing_5.append(0)

	values_1.append(0)
	values_2.append(0)
	values_3.append(0)
	values_4.append(0)
	values_5.append(0)

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_1[key_1], record_1[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_1.append(index)
			values_1.append(float(sum_1 + sum_2) / float(limits))
			sum_1 = 0
			sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_2[key_1], record_2[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_2.append(index)
			values_2.append(float(sum_1 + sum_2) / float(limits))
			sum_1 = 0
			sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_3[key_1], record_3[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_3.append(index)
			values_3.append(float(sum_1 + sum_2) / float(limits))
			sum_1 = 0
			sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_4[key_1], record_4[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_4.append(index)
			values_4.append(float(sum_1 + sum_2) / float(limits))
			sum_1 = 0
			sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_5[key_1], record_5[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_5.append(index)
			values_5.append(float(sum_1 + sum_2) / float(limits))
			sum_1 = 0
			sum_2 = 0


	print len(timing_1)
	print timing_1
	print len(values_1)
	print values_1
	print len(timing_2)
	print timing_2
	print len(values_2)
	print values_2
	print len(timing_3)
	print timing_3
	print len(values_3)
	print values_3
	print len(timing_4)
	print timing_4
	print len(values_4)
	print values_4
	print len(timing_5)
	print timing_5
	print len(values_5)
	print values_5

	plt.plot(timing_1, values_1,label='NVE#1-No-Split',marker='o', markersize=3, color='b' )
	plt.plot(timing_2, values_2,label='NVE#3-SplitRatio:20%',marker='o', markersize=3, color='g' )
	plt.plot(timing_3, values_3,label='NVE#3-SplitRatio:30%',marker='o', markersize=3, color='r' )
	plt.plot(timing_4, values_4,label='NVE#3-SplitRatio:40%',marker='o', markersize=3, color='c' )
	plt.plot(timing_5, values_5,label='NVE#3-SplitRatio:50%',marker='o', markersize=3, color='m')

	pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='small')

	plt.ylabel(ytxt)
	plt.xlabel(xtxt)
	plt.title(title)

	plt.grid(True)
	
	print plt.gca().get_ylim()
	x_limits, y_limits = plt.gca().get_ylim()
	plt.ylim(0, y_limits * 1.15 )

	plt.savefig('./'+ title + '.png')
	plt.show()

	del timing_1[:]
	del timing_2[:]
	del timing_3[:]
	del timing_4[:]
	del timing_5[:]

	del values_1[:]
	del values_2[:]
	del values_3[:]
	del values_4[:]
	del values_5[:]


# key_1 : SublinkCost
# key_2 : EmbeddedNodes (1 vnode : 1 cpu)
# VirNwsCost = SublinkCost + sum(embeddedNodes'cpu)
def showAllVirNwsSubCostImage( key_1, key_2, limits, record_1, record_2, record_3, record_4, record_5, ytxt, xtxt, title):
	timing_1 = []
	timing_2 = []
	timing_3 = []
	timing_4 = []
	timing_5 = []

	values_1 = []
	values_2 = []
	values_3 = []
	values_4 = []
	values_5 = []


	
	timing_1.append(0)
	timing_2.append(0)
	timing_3.append(0)
	timing_4.append(0)
	timing_5.append(0)

	values_1.append(0)
	values_2.append(0)
	values_3.append(0)
	values_4.append(0)
	values_5.append(0)

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_1[key_1], record_1[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_1.append(index)
			values_1.append(float(sum_1 + sum_2) / float(limits) )
			sum_1 = 0
			sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_2[key_1], record_2[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_2.append(index)
			values_2.append(float(sum_1 + sum_2) / float(limits))
			sum_1 = 0
			sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_3[key_1], record_3[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_3.append(index)
			values_3.append(float(sum_1 + sum_2) / float(limits))
			sum_1 = 0
			sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_4[key_1], record_4[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_4.append(index)
			values_4.append(float(sum_1 + sum_2) / float(limits))
			sum_1 = 0
			sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_5[key_1], record_5[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_5.append(index)
			values_5.append(float(sum_1 + sum_2) / float(limits))
			sum_1 = 0
			sum_2 = 0


	print len(timing_1)
	print timing_1
	print len(values_1)
	print values_1
	print len(timing_2)
	print timing_2
	print len(values_2)
	print values_2
	print len(timing_3)
	print timing_3
	print len(values_3)
	print values_3
	print len(timing_4)
	print timing_4
	print len(values_4)
	print values_4
	print len(timing_5)
	print timing_5
	print len(values_5)
	print values_5

	plt.plot(timing_1, values_1,label='NVE#1-No-Split',marker='o', markersize=3, color='b' )
	plt.plot(timing_2, values_2,label='NVE#3-SplitRatio:20%',marker='o', markersize=3, color='g' )
	plt.plot(timing_3, values_3,label='NVE#3-SplitRatio:30%',marker='o', markersize=3, color='r' )
	plt.plot(timing_4, values_4,label='NVE#3-SplitRatio:40%',marker='o', markersize=3, color='c' )
	plt.plot(timing_5, values_5,label='NVE#3-SplitRatio:50%',marker='o', markersize=3, color='m')

	pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='small')

	plt.ylabel(ytxt)
	plt.xlabel(xtxt)
	plt.title(title)

	plt.grid(True)
	
	print plt.gca().get_ylim()
	x_limits, y_limits = plt.gca().get_ylim()
	plt.ylim(0, y_limits * 1.15 )

	plt.savefig('./'+ title + '.png')
	plt.show()

	del timing_1[:]
	del timing_2[:]
	del timing_3[:]
	del timing_4[:]
	del timing_5[:]

	del values_1[:]
	del values_2[:]
	del values_3[:]
	del values_4[:]
	del values_5[:]

#key_1 = 'EmbeddedBandwidth', 
#key_2 = 'EmbeddedNodes'
#key_11 = 'SublinkCost'
#key_22 = 'EmbeddedNodes'
#Revenue to subcost = Revenue / SubCost
## key_1 and key_2 to calculate revenue
## key_11 and key_22 to calcuate subcost

def showAllVirNwsRevenueToSubCostImage( key_1, key_2, key_11, key_22, limits, record_1, record_2, record_3, record_4, record_5, ytxt, xtxt, title):
	timing_1 = []
	timing_2 = []
	timing_3 = []
	timing_4 = []
	timing_5 = []

	values_1 = []
	values_2 = []
	values_3 = []
	values_4 = []
	values_5 = []


	
	timing_1.append(0)
	timing_2.append(0)
	timing_3.append(0)
	timing_4.append(0)
	timing_5.append(0)

	values_1.append(0)
	values_2.append(0)
	values_3.append(0)
	values_4.append(0)
	values_5.append(0)

	sum_1 = 0
	sum_2 = 0
	sum_3 = 0
	sum_4 = 0

	index = 0
	for item_1, item_2, item_11, item_22 in zip(record_1[key_1], record_1[key_2],record_1[key_11], record_1[key_22]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		sum_3 = sum_3 + item_11['Total']
		sum_4 = sum_4 + item_22['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_1.append(index)
			if float(sum_1 + sum_2) == 0.0 or float(sum_3 + sum_4) == 0.0:
				values_1.append( 0.0 )
			else:
				
				values_1.append(  float(sum_1 + sum_2) / float(sum_3 + sum_4) )
			sum_1 = 0
			sum_2 = 0
			sum_3 = 0
			sum_4 = 0

	sum_1 = 0
	sum_2 = 0
	sum_3 = 0
	sum_4 = 0

	index = 0
	for item_1, item_2, item_11, item_22 in zip(record_2[key_1], record_2[key_2],record_2[key_11], record_2[key_22]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		sum_3 = sum_3 + item_11['Total']
		sum_4 = sum_4 + item_22['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_2.append(index)
			if float(sum_1 + sum_2) == 0.0 or float(sum_3 + sum_4) == 0.0:
				values_2.append( 0.0 )
			else:
				
				values_2.append(  float(sum_1 + sum_2) / float(sum_3 + sum_4) )
			sum_1 = 0
			sum_2 = 0
			sum_3 = 0
			sum_4 = 0

	sum_1 = 0
	sum_2 = 0
	sum_3 = 0
	sum_4 = 0

	index = 0
	for item_1, item_2, item_11, item_22 in zip(record_3[key_1], record_3[key_2],record_3[key_11], record_3[key_22]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		sum_3 = sum_3 + item_11['Total']
		sum_4 = sum_4 + item_22['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_3.append(index)
			if float(sum_1 + sum_2) == 0.0 or float(sum_3 + sum_4) == 0.0:
				values_3.append( 0.0 )
			else:
				
				values_3.append(  float(sum_1 + sum_2) / float(sum_3 + sum_4) )
			sum_1 = 0
			sum_2 = 0
			sum_3 = 0
			sum_4 = 0

	sum_1 = 0
	sum_2 = 0
	sum_3 = 0
	sum_4 = 0

	index = 0
	for item_1, item_2, item_11, item_22 in zip(record_4[key_1], record_4[key_2],record_4[key_11], record_4[key_22]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		sum_3 = sum_3 + item_11['Total']
		sum_4 = sum_4 + item_22['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_4.append(index)
			if float(sum_1 + sum_2) == 0.0 or float(sum_3 + sum_4) == 0.0:
				values_4.append( 0.0 )
			else:
				
				values_4.append(  float(sum_1 + sum_2) / float(sum_3 + sum_4) )
			sum_1 = 0
			sum_2 = 0
			sum_3 = 0
			sum_4 = 0

	sum_1 = 0
	sum_2 = 0
	sum_3 = 0
	sum_4 = 0

	index = 0
	for item_1, item_2, item_11, item_22 in zip(record_5[key_1], record_5[key_2],record_5[key_11], record_5[key_22]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		sum_3 = sum_3 + item_11['Total']
		sum_4 = sum_4 + item_22['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_5.append(index)
			if float(sum_1 + sum_2) == 0.0 or float(sum_3 + sum_4) == 0.0:
				values_5.append( 0.0 )
			else:
				
				values_5.append(  float(sum_1 + sum_2) / float(sum_3 + sum_4) )
			sum_1 = 0
			sum_2 = 0
			sum_3 = 0
			sum_4 = 0


	print len(timing_1)
	print timing_1
	print len(values_1)
	print values_1
	print len(timing_2)
	print timing_2
	print len(values_2)
	print values_2
	print len(timing_3)
	print timing_3
	print len(values_3)
	print values_3
	print len(timing_4)
	print timing_4
	print len(values_4)
	print values_4
	print len(timing_5)
	print timing_5
	print len(values_5)
	print values_5

	plt.plot(timing_1, values_1,label='NVE#1-No-Split',marker='o', markersize=3, color='b' )
	plt.plot(timing_2, values_2,label='NVE#3-SplitRatio:20%',marker='o', markersize=3, color='g' )
	plt.plot(timing_3, values_3,label='NVE#3-SplitRatio:30%',marker='o', markersize=3, color='r' )
	plt.plot(timing_4, values_4,label='NVE#3-SplitRatio:40%',marker='o', markersize=3, color='c' )
	plt.plot(timing_5, values_5,label='NVE#3-SplitRatio:50%',marker='o', markersize=3, color='m')

	pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='small')

	plt.ylabel(ytxt)
	plt.xlabel(xtxt)
	plt.title(title)

	plt.grid(True)
	
	print plt.gca().get_ylim()
	x_limits, y_limits = plt.gca().get_ylim()
	plt.ylim(0, y_limits * 1.15 )

	formatter = FuncFormatter(to_percent)
	plt.gca().yaxis.set_major_formatter(formatter)

	plt.savefig('./'+ title + '.png')
	plt.show()

	del timing_1[:]
	del timing_2[:]
	del timing_3[:]
	del timing_4[:]
	del timing_5[:]

	del values_1[:]
	del values_2[:]
	del values_3[:]
	del values_4[:]
	del values_5[:]



# key_1 : DataSwichingEnergy
def showAllVirNwsSwitchingEnergyImage( key_1, limits, record_1, record_2, record_3, record_4, record_5, ytxt, xtxt, title):
	timing_1 = []
	timing_2 = []
	timing_3 = []
	timing_4 = []
	timing_5 = []

	values_1 = []
	values_2 = []
	values_3 = []
	values_4 = []
	values_5 = []


	
	timing_1.append(0)
	timing_2.append(0)
	timing_3.append(0)
	timing_4.append(0)
	timing_5.append(0)

	values_1.append(0)
	values_2.append(0)
	values_3.append(0)
	values_4.append(0)
	values_5.append(0)

	sum_1 = 0
	index = 0
	for item_1 in record_1[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_1.append(index)
			values_1.append(float(sum_1) / float(limits))
			sum_1 = 0

	sum_1 = 0
	index = 0
	for item_1 in record_2[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_2.append(index)
			values_2.append(float(sum_1) / float(limits))
			sum_1 = 0

	sum_1 = 0
	index = 0
	for item_1 in record_3[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_3.append(index)
			values_3.append(float(sum_1) / float(limits))
			sum_1 = 0


	sum_1 = 0
	index = 0
	for item_1 in record_4[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_4.append(index)
			values_4.append(float(sum_1) / float(limits))
			sum_1 = 0

	sum_1 = 0
	index = 0
	for item_1 in record_5[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_5.append(index)
			values_5.append(float(sum_1) / float(limits))
			sum_1 = 0


	print len(timing_1)
	print timing_1
	print len(values_1)
	print values_1
	print len(timing_2)
	print timing_2
	print len(values_2)
	print values_2
	print len(timing_3)
	print timing_3
	print len(values_3)
	print values_3
	print len(timing_4)
	print timing_4
	print len(values_4)
	print values_4
	print len(timing_5)
	print timing_5
	print len(values_5)
	print values_5

	plt.plot(timing_1, values_1,label='NVE#1-No-Split',marker='o', markersize=3, color='b' )
	plt.plot(timing_2, values_2,label='NVE#3-SplitRatio:20%',marker='o', markersize=3, color='g' )
	plt.plot(timing_3, values_3,label='NVE#3-SplitRatio:30%',marker='o', markersize=3, color='r' )
	plt.plot(timing_4, values_4,label='NVE#3-SplitRatio:40%',marker='o', markersize=3, color='c' )
	plt.plot(timing_5, values_5,label='NVE#3-SplitRatio:50%',marker='o', markersize=3, color='m')

	pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='small')

	plt.ylabel(ytxt)
	plt.xlabel(xtxt)
	plt.title(title)

	plt.grid(True)
	
	print plt.gca().get_ylim()
	x_limits, y_limits = plt.gca().get_ylim()
	plt.ylim(0, y_limits * 1.15 )

	plt.savefig('./'+ title + '.png')
	plt.show()

	del timing_1[:]
	del timing_2[:]
	del timing_3[:]
	del timing_4[:]
	del timing_5[:]

	del values_1[:]
	del values_2[:]
	del values_3[:]
	del values_4[:]
	del values_5[:]

# key_1 = 'CurrentSubLinkResourceMinInfo', 

# key_2 : 2500
# AvaliableResoruceUtilization = 1 - CurrentSubLinkResourceMinInfo / 2500
def showAllSubstrateNetworkResoruceUtilizationMinImage( key_1, subLinks, limits, record_1, record_2, record_3, record_4, record_5, ytxt, xtxt, title):
	timing_1 = []
	timing_2 = []
	timing_3 = []
	timing_4 = []
	timing_5 = []

	values_1 = []
	values_2 = []
	values_3 = []
	values_4 = []
	values_5 = []


	
	timing_1.append(0)
	timing_2.append(0)
	timing_3.append(0)
	timing_4.append(0)
	timing_5.append(0)

	values_1.append(0)
	values_2.append(0)
	values_3.append(0)
	values_4.append(0)
	values_5.append(0)

	sum_1 = 0
	index = 0
	for item_1 in record_1[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_1.append(index)
			values_1.append(float(sum_1)/float(limits))
			sum_1 = 0

	sum_1 = 0
	index = 0
	for item_1 in record_2[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_2.append(index)
			values_2.append(float(sum_1)/float(limits))
			sum_1 = 0

	sum_1 = 0
	index = 0
	for item_1 in record_3[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_3.append(index)
			values_3.append(float(sum_1)/float(limits))
			sum_1 = 0
	sum_1 = 0
	index = 0
	for item_1 in record_4[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_4.append(index)
			values_4.append(float(sum_1)/float(limits))
			sum_1 = 0

	sum_1 = 0
	index = 0
	for item_1 in record_5[key_1]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_5.append(index)
			values_5.append(float(sum_1)/float(limits)) 
			sum_1 = 0


	print len(timing_1)
	print timing_1
	print len(values_1)
	print values_1
	print len(timing_2)
	print timing_2
	print len(values_2)
	print values_2
	print len(timing_3)
	print timing_3
	print len(values_3)
	print values_3
	print len(timing_4)
	print timing_4
	print len(values_4)
	print values_4
	print len(timing_5)
	print timing_5
	print len(values_5)
	print values_5

	plt.plot(timing_1, values_1,label='NVE#1-No-Split',marker='o', markersize=3, color='b' )
	plt.plot(timing_2, values_2,label='NVE#3-SplitRatio:20%',marker='o', markersize=3, color='g' )
	plt.plot(timing_3, values_3,label='NVE#3-SplitRatio:30%',marker='o', markersize=3, color='r' )
	plt.plot(timing_4, values_4,label='NVE#3-SplitRatio:40%',marker='o', markersize=3, color='c' )
	plt.plot(timing_5, values_5,label='NVE#3-SplitRatio:50%',marker='o', markersize=3, color='m')

	pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='small')

	plt.ylabel(ytxt)
	plt.xlabel(xtxt)
	plt.title(title)

	plt.grid(True)
	
	print plt.gca().get_ylim()
	x_limits, y_limits = plt.gca().get_ylim()
	plt.ylim(0, y_limits * 1.15 )


	plt.savefig('./'+ title + '.png')
	plt.show()

	del timing_1[:]
	del timing_2[:]
	del timing_3[:]
	del timing_4[:]
	del timing_5[:]

	del values_1[:]
	del values_2[:]
	del values_3[:]
	del values_4[:]
	del values_5[:]

recordJson_1 = json.loads(open(nve_1_file).read())
recordJson_2 = json.loads(open(nve_2_file).read())
recordJson_3 = json.loads(open(nve_3_file).read())
recordJson_4 = json.loads(open(nve_4_file).read())
recordJson_5 = json.loads(open(nve_5_file).read())

limits = 200



# key_1 = 'CurrentSubLinkResourceMinInfo', 

# key_2 : 2500
# AvaliableResoruceUtilization = 1 - CurrentSubLinkResourceMinInfo / 2500
showAllSubstrateNetworkResoruceUtilizationMinImage( 'CurrentSubLinkResourceMinInfo', 2500, limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Substrate Link(s)', 'Time Unit(s)', 'Evaluation of Substrate Network Resoruce Utilization (Less than 30M)')

showAllSubstrateNetworkResoruceUtilizationMinImage( 'CurrentSubLinkResourceMaxInfo', 2500, limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Substrate Link(s)', 'Time Unit(s)', 'Evaluation of Substrate Network Resoruce Utilization (More than 100M)')

showAllSubstrateNetworkResoruceUtilizationMinImage( 'EmbeddableSubLinkResourceInfo', 2500, limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Substrate Link(s)', 'Time Unit(s)', 'Evaluation of Substrate Network Resoruce Utilization (among 30M to 100M)')


# key_1 : FailureEmbedding
# key_1 : RequestEmbedding
# AccetpionRatio = 1 - FailureEmbedding / RequestEmbedding
showTwoAcceptionRatioImage( 'FailureEmbedding', 'RequestEmbedding', limits, recordJson_1, recordJson_2, 'Accetpion Ratio', 'Time Unit(s)', 'Evaluation of Virtual Network Request Accetpion Ratio', '20')

showTwoAcceptionRatioImage( 'FailureEmbedding', 'RequestEmbedding', limits, recordJson_1, recordJson_3, 'Accetpion Ratio', 'Time Unit(s)', 'Evaluation of Virtual Network Request Accetpion Ratio', '30')

showTwoAcceptionRatioImage( 'FailureEmbedding', 'RequestEmbedding', limits, recordJson_1, recordJson_4, 'Accetpion Ratio', 'Time Unit(s)', 'Evaluation of Virtual Network Request Accetpion Ratio', '40')

showTwoAcceptionRatioImage( 'FailureEmbedding', 'RequestEmbedding', limits, recordJson_1, recordJson_5, 'Accetpion Ratio', 'Time Unit(s)', 'Evaluation of Virtual Network Request Accetpion Ratio', '50')


showAllAcceptionRatioImage( 'FailureEmbedding', 'RequestEmbedding', limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Accetpion Ratio', 'Time Unit(s)', 'Evaluation of Virtual Network Request Accetpion Ratio')


# total virtual neworks Revenue
showTwoVirNwsRevenueImage( 'EmbeddedBandwidth', 'EmbeddedNodes', limits, recordJson_1, recordJson_2, 'Revenue', 'Time Unit(s)', 'Evaluation of Virtual Network Revenue', '20')

showTwoVirNwsRevenueImage( 'EmbeddedBandwidth', 'EmbeddedNodes', limits, recordJson_1, recordJson_3, 'Revenue', 'Time Unit(s)', 'Evaluation of Virtual Network Revenue', '30')

showTwoVirNwsRevenueImage( 'EmbeddedBandwidth', 'EmbeddedNodes', limits, recordJson_1, recordJson_4, 'Revenue', 'Time Unit(s)', 'Evaluation of Virtual Network Revenue', '40')

showTwoVirNwsRevenueImage( 'EmbeddedBandwidth', 'EmbeddedNodes', limits, recordJson_1, recordJson_5, 'Revenue', 'Time Unit(s)', 'Evaluation of Virtual Network Revenue', '50')

showAllVirNwsRevenueImage( 'EmbeddedBandwidth', 'EmbeddedNodes', limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Revenue', 'Time Unit(s)', 'Evaluation of Virtual Network Revenue')
# total virtual neworks Revenue

## same virtual networks Revenue
showTwoVirNwsRevenueImage( 'SameVirNwEmbeddedBandwidth', 'SameVirNwVNodes', limits, recordJson_1, recordJson_2, 'Revenue', 'Time Unit(s)', 'Evaluation of Same Virtual Network Revenue', '20')

showTwoVirNwsRevenueImage( 'SameVirNwEmbeddedBandwidth', 'SameVirNwVNodes', limits, recordJson_1, recordJson_3, 'Revenue', 'Time Unit(s)', 'Evaluation of Same Virtual Network Revenue', '30')

showTwoVirNwsRevenueImage( 'SameVirNwEmbeddedBandwidth', 'SameVirNwVNodes', limits, recordJson_1, recordJson_4, 'Revenue', 'Time Unit(s)', 'Evaluation of Same Virtual Network Revenue', '40')

showTwoVirNwsRevenueImage( 'SameVirNwEmbeddedBandwidth', 'SameVirNwVNodes', limits, recordJson_1, recordJson_5, 'Revenue', 'Time Unit(s)', 'Evaluation of Same Virtual Network Revenue', '50')

showAllVirNwsRevenueImage( 'SameVirNwEmbeddedBandwidth', 'SameVirNwVNodes', limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Revenue', 'Time Unit(s)', 'Evaluation of Same Virtual Network Revenue')
## same virtual networks Revenue

## total virtual neworks substrate cost
showTwoVirNwsSubCostImage( 'SublinkCost', 'EmbeddedNodes', limits, recordJson_1, recordJson_2, 'Cost', 'Time Unit(s)', 'Evaluation of Virtual Network Cost', '20')

showTwoVirNwsSubCostImage( 'SublinkCost', 'EmbeddedNodes', limits, recordJson_1, recordJson_3, 'Cost', 'Time Unit(s)', 'Evaluation of Virtual Network Cost', '30')

showTwoVirNwsSubCostImage( 'SublinkCost', 'EmbeddedNodes', limits, recordJson_1, recordJson_4, 'Cost', 'Time Unit(s)', 'Evaluation of Virtual Network Cost', '40')

showTwoVirNwsSubCostImage( 'SublinkCost', 'EmbeddedNodes', limits, recordJson_1, recordJson_5, 'Cost', 'Time Unit(s)', 'Evaluation of Virtual Network Cost', '50')

showAllVirNwsSubCostImage( 'SublinkCost', 'EmbeddedNodes', limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Cost', 'Time Unit(s)', 'Evaluation of Virtual Network Cost')
## total virtual neworks substrate cost

## same virtual networks substrate cost
showTwoVirNwsSubCostImage( 'SameVirNwSubCost', 'SameVirNwVNodes', limits, recordJson_1, recordJson_2, 'Cost', 'Time Unit(s)', 'Evaluation of Same Virtual Network Cost', '20')

showTwoVirNwsSubCostImage( 'SameVirNwSubCost', 'SameVirNwVNodes', limits, recordJson_1, recordJson_3, 'Cost', 'Time Unit(s)', 'Evaluation of Same Virtual Network Cost', '30')

showTwoVirNwsSubCostImage( 'SameVirNwSubCost', 'SameVirNwVNodes', limits, recordJson_1, recordJson_4, 'Cost', 'Time Unit(s)', 'Evaluation of Same Virtual Network Cost', '40')

showTwoVirNwsSubCostImage( 'SameVirNwSubCost', 'SameVirNwVNodes', limits, recordJson_1, recordJson_5, 'Cost', 'Time Unit(s)', 'Evaluation of Same Virtual Network Cost', '50')

showAllVirNwsSubCostImage( 'SameVirNwSubCost', 'SameVirNwVNodes', limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Cost', 'Time Unit(s)', 'Evaluation of Same Virtual Network Cost')
## same virtual networks substrate cost


## total virtual network revenue to cost ratio
showTowVirNwsRevenueToSubCostImage( 'EmbeddedBandwidth', 'EmbeddedNodes', 'SublinkCost', 'EmbeddedNodes', limits, recordJson_1, recordJson_2, 'Ratio', 'Time Unit(s)', 'Evaluation of Virtual Network Revenue to Cost Ratio', '20')

showTowVirNwsRevenueToSubCostImage( 'EmbeddedBandwidth', 'EmbeddedNodes', 'SublinkCost', 'EmbeddedNodes', limits, recordJson_1, recordJson_3, 'Ratio', 'Time Unit(s)', 'Evaluation of Virtual Network Revenue to Cost Ratio', '30')

showTowVirNwsRevenueToSubCostImage( 'EmbeddedBandwidth', 'EmbeddedNodes', 'SublinkCost', 'EmbeddedNodes', limits, recordJson_1, recordJson_4, 'Ratio', 'Time Unit(s)', 'Evaluation of Virtual Network Revenue to Cost Ratio', '40')

showTowVirNwsRevenueToSubCostImage( 'EmbeddedBandwidth', 'EmbeddedNodes', 'SublinkCost', 'EmbeddedNodes', limits, recordJson_1, recordJson_5, 'Ratio', 'Time Unit(s)', 'Evaluation of Virtual Network Revenue to Cost Ratio', '50')

showAllVirNwsRevenueToSubCostImage( 'EmbeddedBandwidth', 'EmbeddedNodes', 'SublinkCost', 'EmbeddedNodes', limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Ratio', 'Time Unit(s)', 'Evaluation of Virtual Network Revenue to Cost Ratio')
## total virtual network revenue to cost ratio

## Same virtual networks revenue to cost ratio

showTowVirNwsRevenueToSubCostImage( 'SameVirNwEmbeddedBandwidth', 'SameVirNwVNodes', 'SameVirNwSubCost', 'SameVirNwVNodes', limits, recordJson_1, recordJson_2, 'Ratio', 'Time Unit(s)', 'Evaluation of Same Virtual Network Revenue to Cost Ratio', '20')

showTowVirNwsRevenueToSubCostImage( 'SameVirNwEmbeddedBandwidth', 'SameVirNwVNodes', 'SameVirNwSubCost', 'SameVirNwVNodes', limits, recordJson_1, recordJson_3, 'Ratio', 'Time Unit(s)', 'Evaluation of Same Virtual Network Revenue to Cost Ratio', '30')

showTowVirNwsRevenueToSubCostImage( 'SameVirNwEmbeddedBandwidth', 'SameVirNwVNodes', 'SameVirNwSubCost', 'SameVirNwVNodes', limits, recordJson_1, recordJson_4, 'Ratio', 'Time Unit(s)', 'Evaluation of Same Virtual Network Revenue to Cost Ratio', '40')

showTowVirNwsRevenueToSubCostImage( 'SameVirNwEmbeddedBandwidth', 'SameVirNwVNodes', 'SameVirNwSubCost', 'SameVirNwVNodes', limits, recordJson_1, recordJson_5, 'Ratio', 'Time Unit(s)', 'Evaluation of Same Virtual Network Revenue to Cost Ratio', '50')

showAllVirNwsRevenueToSubCostImage( 'SameVirNwEmbeddedBandwidth', 'SameVirNwVNodes', 'SameVirNwSubCost', 'SameVirNwVNodes', limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Ratio', 'Time Unit(s)', 'Evaluation of Same Virtual Network Revenue to Cost Ratio')
## Same virtual networks revenue to cost ratio

limits = 100
## total data swiching energy

showTwoVirNwsSwitchingEnergyImage( 'DataSwichingEnergy', limits, recordJson_1, recordJson_2, 'Switching Energy(Joule)','Time Unit(s)','Evaluation of Total Virtual Network Data Switching Energy', '20' )

showTwoVirNwsSwitchingEnergyImage( 'DataSwichingEnergy', limits, recordJson_1, recordJson_3, 'Switching Energy(Joule)','Time Unit(s)','Evaluation of Total Virtual Network Data Switching Energy', '30' )

showTwoVirNwsSwitchingEnergyImage( 'DataSwichingEnergy', limits, recordJson_1, recordJson_4, 'Switching Energy(Joule)','Time Unit(s)','Evaluation of Total Virtual Network Data Switching Energy', '40' )

showTwoVirNwsSwitchingEnergyImage( 'DataSwichingEnergy', limits, recordJson_1, recordJson_5, 'Switching Energy(Joule)','Time Unit(s)','Evaluation of Total Virtual Network Data Switching Energy', '50' )

showAllVirNwsSwitchingEnergyImage('DataSwichingEnergy', limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Switching Energy(Joule)','Time Unit(s)','Evaluation of Total Virtual Network Data Switching Energy')
## total data swiching energy

## same virtual network data switching energy
showTwoVirNwsSwitchingEnergyImage( 'SameVirNwDataSwitchingEnergy', limits, recordJson_1, recordJson_2, 'Switching Energy(Joule)','Time Unit(s)','Evaluation of Same Virtual Network Data Switching Energy', '20' )

showTwoVirNwsSwitchingEnergyImage( 'SameVirNwDataSwitchingEnergy', limits, recordJson_1, recordJson_3, 'Switching Energy(Joule)','Time Unit(s)','Evaluation of Same Virtual Network Data Switching Energy', '30' )

showTwoVirNwsSwitchingEnergyImage( 'SameVirNwDataSwitchingEnergy', limits, recordJson_1, recordJson_4, 'Switching Energy(Joule)','Time Unit(s)','Evaluation of Same Virtual Network Data Switching Energy', '40' )

showTwoVirNwsSwitchingEnergyImage( 'SameVirNwDataSwitchingEnergy', limits, recordJson_1, recordJson_5, 'Switching Energy(Joule)','Time Unit(s)','Evaluation of Same Virtual Network Data Switching Energy', '50' )

showAllVirNwsSwitchingEnergyImage('SameVirNwDataSwitchingEnergy', limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Switching Energy(Joule)','Time Unit(s)','Evaluation of Same Virtual Network Data Switching Energy')
## same virtual network data switching energy

#exit()
showImage( 'AmountVirNws', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Virtual Network(s)','Time Unit(s)','Evaluation of Embedded Virtual Network(s)')

showImage( 'FailureEmbedding', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Virtual Network(s)','Time Unit(s)','Evaluation of Failure Embedding Virtual Network(s)')

showImage( 'AvailableVirNws', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Virtual Network(s)','Time Unit(s)','Evaluation of Available Virtual Network(s)')

showImage('CurrentEndingVirNws', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Virtual Network(s)','Time Unit(s)','Evaluation of Ending Virtual Network(s)')

showImage('EmbeddedLinks', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Virtual Link(s)','Time Unit(s)','Evaluation of Embedded Virtual Link(s)')

showImage('EmbeddedNodes', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Virtual Node(s)','Time Unit(s)','Evaluation of Embedded Virtual Node(s)')

showImage('EmbeddedBandwidth', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Virtual Bandwidth(Mbps)','Time Unit(s)','Evaluation of Embedded Virtual Bandwidth')

showImage('CurrentSubLinkResourceMinInfo', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Substrate Link(s)','Time Unit(s)','Evaluation of Embeddable Substrate Links(Less than 30M)')

showImage('CurrentSubLinkResourceMaxInfo', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Substrate Link(s)','Time Unit(s)','Evaluation of Embeddable Substrate Links(more than 100M)')

showImage('EmbeddableSubLinkResourceInfo', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Substrate Link(s)','Time Unit(s)','Evaluation of Embeddable Substrate Links(among 30M and 100M)')

showImage('DataSwichingEnergy', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Switching Energy(Joule)','Time Unit(s)','Evaluation of Data Switching Energy')

showImage('ComDataSwichingEnergy', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Switching Energy(Joule)','Time Unit(s)','Evaluation of Common Virtural Networks'' Data Switching Energy')

showImage('SameVirNwDataSwitchingEnergy', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Switching Energy(Joule)','Time Unit(s)','Evaluation of Same Virtual Networks'' Data Switching Energy')


showImage('TransportedDataVolume', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Data Volume(Megabits)','Time Unit(s)','Evaluation of Switching Data Volume')

showImage('ComTransportedDataVolume', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Data Volume(Megabits)','Time Unit(s)','Evaluation of Common Virtual Networks'' Switching Data Volume')

showImage('SameVirNwTransportedDataVolume', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Data Volume(Megabits)','Time Unit(s)','Evaluation of Same Virtual Networks'' Switching Data Volume')

showImage('CurrentEndUserRequests', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'End-user Request(s)','Time Unit(s)','Evaluation of End-user Requests')

showImage('CurrentCommonEndUserReqs', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'End-user Request(s)','Time Unit(s)','Evaluation of Common End-user Requests')

showImage('CurrentEndingEndUserReqs', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'End-user Request(s)','Time Unit(s)','Evaluation of Ending End-user Requests')

showImage('CongestionRecords', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Congestion Time(s)','Time Unit(s)','Evaluation of End-User Request Congestions')

showImage('CurrentComVirNws', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Virtual Network(s)','Time Unit(s)','Evaluation of Common Virtual Networks')

showImage('CurrentSameVirNws', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Virtual Network(s)','Time Unit(s)','Evaluation of Same Virtual Networks')

showImage('SublinkCost', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Cost(s)','Time Unit(s)','Evaluation of Substrate Networks Cost')


showImage('SameVirNwSubCost', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Cost(s)','Time Unit(s)','Evaluation of Same Virtual Network Cost')

showImage('SameVirNwEmbeddedBandwidth', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Virtual Bandwidth(s)','Time Unit(s)','Evaluation of Embedded Same Virtual Network Bandwidth')

showImage('SameVirNwEmbeddedLinks', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Virtual Link(s)','Time Unit(s)','Evaluation of Same Virtual Network Links')

showImage('SameVirNwVNodes', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Virtual Node(s)','Time Unit(s)','Evaluation of Same Virtual Network Nodes')

showImage('RequestEmbedding', recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5, 'Request(s)','Time Unit(s)','Evaluation of Virtual Network Requests')

