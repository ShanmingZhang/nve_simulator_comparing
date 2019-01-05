import json
import pylab
import numpy as np
from matplotlib.ticker import FuncFormatter

import matplotlib

import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import matplotlib.ticker as mtick

subname = '2017-05-1815:03:36_recordsOutput.json'

dirname = './'


nve_1_file = dirname + 'NVE#1_' + subname

nve_2_file = dirname + 'NVE#3_20_' + subname

nve_3_file = dirname + 'NVE#3_30_' + subname

nve_4_file = dirname + 'NVE#3_40_' + subname

nve_5_file = dirname + 'NVE#3_50_' + subname






##key_1 = SameVirNwDataSwitchingEnergy 
##key_2 = SameVirNwTransportedDataVolume
def showAllVirNwsSwitchingEnergyImage( key_1, key_2, limits, record_1, record_2, record_3, record_4, record_5, ytxt, xtxt, title):
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

	data_volume = []
	data_volume.append(0)
	data_volume_0 = []
	data_volume_0.append(0)

	sum_1 = 0
	index = 0
	for item_1 in record_1[key_2]:
		index = index + 1
		sum_1 = sum_1 + item_1['Total']

		if (index > 1 ) and ((index % limits) == 0):
			data_volume.append(float(sum_1) / float(limits))
			data_volume_0.append(0)
			sum_1 = 0



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

	fig, ax1 = plt.subplots()
	
	ax1.plot(timing_5, data_volume_0,label='NVE#1-TrafficVolume',linestyle='solid', linewidth='2', marker='o', markersize=0, color='y')


	ax1.plot(timing_1, values_1,label='NVE#1-No-Split',marker='o', markersize=0, color='b' )
	ax1.plot(timing_2, values_2,label='NVE#3-SplitRatio:20%',marker='o', markersize=0, color='g' )
	ax1.plot(timing_3, values_3,label='NVE#3-SplitRatio:30%',marker='o', markersize=0, color='r' )
	ax1.plot(timing_4, values_4,label='NVE#3-SplitRatio:40%',marker='o', markersize=0, color='c' )
	ax1.plot(timing_5, values_5,label='NVE#3-SplitRatio:50%',marker='o', markersize=0, color='m')
	


	ax1.set_ylabel(ytxt)
	ax1.set_xlabel(xtxt)
	ax1.tick_params('y', colors='k')
	

	ax1.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='small')
	ax1.set_ylim(0, 120 )

	plt.ylim(0, 120 )




	plt.title(title)

	ax2 = ax1.twinx()

	print len(timing_1)
	print len(data_volume)
	ax2.plot(timing_1, data_volume, label='NVE#1-TrafficVolume', linestyle='solid', linewidth='2', marker='o', markersize=0, color='y')
	ax2.set_ylabel('Traffic Volume(Megabits)')

	ax2.tick_params('y', colors='k')
	#ax2.legend(loc='center right')
	ax2.set_ylim(0, 1000 )

	ax1.grid(True)
	

	fig.tight_layout()
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


limits = 100
## total data swiching energy
##key_1 = SameVirNwDataSwitchingEnergy 
##key_2 = SameVirNwTransportedDataVolume

showAllVirNwsSwitchingEnergyImage('SameVirNwDataSwitchingEnergy', 'SameVirNwTransportedDataVolume', limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Switching Energy(Joule)','Time Unit','A5 Evaluation of Same Data Transmission Switching Energy')
## total data swiching energy



