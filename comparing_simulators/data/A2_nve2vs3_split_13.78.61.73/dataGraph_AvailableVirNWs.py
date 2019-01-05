import json
import pylab
import numpy as np
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as ticker

import matplotlib

import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import matplotlib.ticker as mtick

subname = '2017-05-1806:06:30_recordsOutput.json'

#dirname = './nve1vs3_split_104.41.184.98/'
dirname = './'


nve_1_file = dirname + 'NVE#2_' + subname

nve_2_file = dirname + 'NVE#3_20_' + subname

nve_3_file = dirname + 'NVE#3_30_' + subname

nve_4_file = dirname + 'NVE#3_40_' + subname

nve_5_file = dirname + 'NVE#3_50_' + subname



# key_1 : AvailableVirNws
# key_2 : RequestEmbedding
# key_3 : CurrentSameVirNws
# 
def showAllAcceptionRatioImage_3( key_1, key_2, key_3, limits, xlimits, record_1, record_2, record_3, record_4, record_5, ytxt, xtxt, title):
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

#RequestEmbedding
	data_volume = []
	data_volume_0 = []

#CurrentSameVirNws
	data_volume_1 = []
	data_volume_10 = []


	sum_1 = 0
	index = 0
	for item_1 in record_1['CurrentSameVirNws']:
		index = index + 1
		if index > xlimits:
			break
		#sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			data_volume_1.append(item_1['Total'])
			data_volume_10.append(0)
			#sum_1 = 0


	sum_1 = 0
	index = 0
	for item_1 in record_1[key_2]:
		index = index + 1
		if index > xlimits:
			break
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			data_volume.append(sum_1)
			data_volume_0.append(0)
			#sum_1 = 0

	sum_1 = 0
	index = 0
	for item_1 in record_1[key_1]:
		index = index + 1
		if index > xlimits:
			break
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_1.append(index)
			values_1.append(item_1['Total'])
			sum_1 = 0

	sum_1 = 0
	index = 0
	for item_1 in record_2[key_1]:
		index = index + 1
		if index > xlimits:
			break
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_2.append(index)
			values_2.append(item_1['Total'])
			sum_1 = 0

	sum_1 = 0
	index = 0
	for item_1 in record_3[key_1]:
		index = index + 1
		if index > xlimits:
			break
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_3.append(index)
			values_3.append(item_1['Total'])
			sum_1 = 0

	sum_1 = 0
	index = 0
	for item_1 in record_4[key_1]:
		index = index + 1
		if index > xlimits:
			break
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_4.append(index)
			values_4.append(item_1['Total'])
			sum_1 = 0

	sum_1 = 0
	index = 0
	for item_1 in record_5[key_1]:
		index = index + 1
		if index > xlimits:
			break
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_5.append(index)
			values_5.append(item_1['Total'])
			sum_1 = 0


	print len(timing_1)
	#print timing_1
	print len(values_1)
	#print values_1
	print len(timing_2)
	#print timing_2
	print len(values_2)
	#print values_2
	print len(timing_3)
	#print timing_3
	print len(values_3)
	#print values_3
	print len(timing_4)
	#print timing_4
	print len(values_4)
	#print values_4
	print len(timing_5)
	#print timing_5
	print len(values_5)
	#print values_5


	fig, ax1 = plt.subplots()
 
	n_groups = len(timing_1)
	index = np.arange(n_groups)

	bar_width = 0.17

	opacity = 0.4

	ax1.bar(index, values_1, bar_width,
		color='b', edgecolor='none',
		label='NVE#1:2')


	ax1.bar(index + bar_width, values_2, bar_width,
                 color='g',edgecolor='none',
                 label='NVE#1:2+eE+20%')

	ax1.bar(index + (2 * bar_width), values_3, bar_width,
                 color='r',edgecolor='none',
                 label='NVE#1:2+eE+30%')

	ax1.bar(index + (3 * bar_width), values_4, bar_width,
                 color='c',edgecolor='none',
                 label='NVE#1:2+eE+40%')

	ax1.bar(index + (4 * bar_width), values_5, bar_width,
                 color='m',edgecolor='none',
                 label='NVE#1:2+eE+50%')

	ax1.set_ylabel(ytxt, color='k',fontsize=17)
	ax1.set_xlabel(xtxt,fontsize=17)

	ax1.set_xticks(index + 3 * bar_width)
	ax1.set_xticklabels(timing_1)

	ax1.plot(ax1.get_xticks(), data_volume_0, label='VNRequests', linestyle='solid', linewidth=2, marker='o', markersize=4, color='y')
	ax1.plot(ax1.get_xticks(), data_volume_10, label='SameVNs', linestyle='solid', linewidth=2, marker='o', markersize=4, color='k')
	ax1.plot(ax1.get_xticks(), data_volume_1, linestyle='solid', linewidth=3, marker='o', markersize=5, color='k')
	
	plt.grid(True)
	ax1.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='12')
	#legend.get_frame().set_facecolor('#00FFCC')

	axes2 = ax1.twinx()
	axes2.plot(ax1.get_xticks(), data_volume, label='VNRequests', linestyle='solid', linewidth=3, marker='o', markersize=5, color='y')


	axes2.set_ylabel('Virtual Network Requests', color='k',fontsize=17)
	


	[tl.set_color('k') for tl in ax1.get_yticklabels()]
	[tl.set_color('k') for tl in axes2.get_yticklabels()]
	
	ax1.set_ylim(0, 60 )
	ax1.yaxis.set_major_locator(ticker.MultipleLocator(5))

	axes2.set_ylim(0, 150 )
	axes2.yaxis.set_major_locator(ticker.MultipleLocator(20))
	x_limits, y_limits = plt.gca().get_ylim()
	plt.ylim(0, 150 )
	
	#plt.title('(A) Available Virtual Networks',fontsize=17)
	plt.savefig(dirname + title + '.png')
	plt.close()


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




limits = 250


xlimits = 3000


showAllAcceptionRatioImage_3( 'AvailableVirNws', 'RequestEmbedding', 'CurrentSameVirNws', limits, xlimits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Virtual Networks', 'Time Unit', 'A1 Evaluation of Available Virtual Networks')


