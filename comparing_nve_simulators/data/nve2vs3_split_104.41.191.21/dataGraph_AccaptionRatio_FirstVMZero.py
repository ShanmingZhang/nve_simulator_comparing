import json
import pylab
import numpy as np
from matplotlib.ticker import FuncFormatter

import matplotlib

import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import matplotlib.ticker as mtick

subname = '2017-05-1813:01:10_recordsOutput.json'

#dirname = './nve1vs3_split_104.41.184.98/'
dirname = './'


nve_1_file = dirname + 'NVE#2_' + subname

nve_2_file = dirname + 'NVE#3_20_' + subname

nve_3_file = dirname + 'NVE#3_30_' + subname

nve_4_file = dirname + 'NVE#3_40_' + subname

nve_5_file = dirname + 'NVE#3_50_' + subname


def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return s + r'$\%$'
    else:
        return s + '%'


# key_1 : FailureEmbedding
# key_1 : RequestEmbedding
# AccetpionRatio = 1 - FailureEmbedding / RequestEmbedding
def showAllAcceptionRatioImage_1( key_1, key_2, limits, record_1, record_2, record_3, record_4, record_5, ytxt, xtxt, title):
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

	plt.plot(timing_1, values_1,label='NVE#1-No-Split',marker='o', markersize=0, color='b' )
	plt.plot(timing_2, values_2,label='NVE#3-SplitRatio:20%',marker='o', markersize=0, color='g' )
	plt.plot(timing_3, values_3,label='NVE#3-SplitRatio:30%',marker='o', markersize=0, color='r' )
	plt.plot(timing_4, values_4,label='NVE#3-SplitRatio:40%',marker='o', markersize=0, color='c' )
	plt.plot(timing_5, values_5,label='NVE#3-SplitRatio:50%',marker='o', markersize=0, color='m')

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

	print dirname + title + '.png'
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


# key_1 : FailureEmbedding
# key_1 : RequestEmbedding
# AccetpionRatio = 1 - FailureEmbedding / RequestEmbedding
def showAllAcceptionRatioImage_2( key_1, key_2, limits, record_1, record_2, record_3, record_4, record_5, ytxt, xtxt, title):
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


	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_1[key_1], record_1[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_1.append(index)
			values_1.append(sum_2-sum_1)
			#sum_1 = 0
			#sum_2 = 0


	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_2[key_1], record_2[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_2.append(index)
			values_2.append(sum_2-sum_1)
			#sum_1 = 0
			#sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_3[key_1], record_3[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_3.append(index)
			values_3.append(sum_2-sum_1)
			#sum_1 = 0
			#sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_4[key_1], record_4[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_4.append(index)
			values_4.append(sum_2-sum_1)
			#sum_1 = 0
			#sum_2 = 0

	sum_1 = 0
	sum_2 = 0
	index = 0
	for item_1, item_2 in zip(record_5[key_1], record_5[key_2]):
		index = index + 1
		sum_1 = sum_1 + item_1['Total']
		sum_2 = sum_2 + item_2['Total']

		if (index > 1 ) and ((index % limits) == 0):
			timing_5.append(index)
			values_5.append(sum_2-sum_1)
			#sum_1 = 0
			#sum_2 = 0


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

	fig, ax = plt.subplots()

	n_groups = len(timing_1)
	index = np.arange(n_groups)
	bar_width = 0.13

	opacity = 0.4
	error_config = {'ecolor': '0.3'}

	rects1 = plt.bar(index, values_1, bar_width,alpha=opacity,color='b',error_kw=error_config,label='NVE#2-TwoPath')


	rects2 = plt.bar(index + bar_width, values_2, bar_width,
                 alpha=opacity,
                 color='g',
                 #yerr=std_women,
                 error_kw=error_config,
                 label='NVE#3-SplitRatio:20%')

	rects3 = plt.bar(index + (2 * bar_width), values_3, bar_width,
                 alpha=opacity,
                 color='r',
                 #yerr=std_men,
                 error_kw=error_config,
                 label='NVE#3-SplitRatio:30%')

	rects4 = plt.bar(index + (3 * bar_width), values_4, bar_width,
                 alpha=opacity,
                 color='c',
                 #yerr=std_women,
                 error_kw=error_config,
                 label='NVE#3-SplitRatio:40%')

	rects5 = plt.bar(index + (4 * bar_width), values_5, bar_width,
                 alpha=opacity,
                 color='m',
                 #yerr=std_women,
                 error_kw=error_config,
                 label='NVE#3-SplitRatio:50%')

	pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='small')

	plt.ylabel(ytxt)
	plt.xlabel(xtxt)
	plt.title(title)

	x_limits, y_limits = plt.gca().get_ylim()
	plt.ylim(0, y_limits * 1.15 )


	plt.grid(True)

	plt.xticks(index + 2 * bar_width, timing_1)



	plt.tight_layout()


	print dirname + title + '.png'
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

# key_1 : FailureEmbedding
# key_1 : RequestEmbedding
# AccetpionRatio = 1 - FailureEmbedding / RequestEmbedding
def showAllAcceptionRatioImage_3( key_1, key_2, limits, record_1, record_2, record_3, record_4, record_5, ytxt, xtxt, title):
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


	
#	timing_1.append(0)
#	timing_2.append(0)
#	timing_3.append(0)
#	timing_4.append(0)
#	timing_5.append(0)

#	values_1.append(1)
#	values_2.append(1)
#	values_3.append(1)
#	values_4.append(1)
#	values_5.append(1)

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


	fig, ax = plt.subplots()

	n_groups = len(timing_1)
	index = np.arange(n_groups)
	bar_width = 0.1

	opacity = 0.4
	error_config = {'ecolor': '0.3'}

#	rects1 = plt.barh(index, values_1, bar_width,alpha=opacity,color='b',error_kw=error_config,label='men')
	print values_1

	rects1 = plt.bar(index, values_1, bar_width, label='NVE#1-No-SplitRatio')

	rects2 = plt.bar(index + bar_width, values_2, bar_width,
                 alpha=opacity,
                 color='g',
                 #yerr=std_women,
                 error_kw=error_config,
                 label='NVE#3-SplitRatio:20%')

	rects3 = plt.bar(index + (2 * bar_width), values_3, bar_width,
                 alpha=opacity,
                 color='r',
                 #yerr=std_men,
                 error_kw=error_config,
                 label='NVE#3-SplitRatio:30%')

	rects4 = plt.bar(index + (3 * bar_width), values_4, bar_width,
                 alpha=opacity,
                 color='c',
                 #yerr=std_women,
                 error_kw=error_config,
                 label='NVE#3-SplitRatio:40%')

	rects5 = plt.bar(index + (4 * bar_width), values_5, bar_width,
                 alpha=opacity,
                 color='m',
                 #yerr=std_women,
                 error_kw=error_config,
                 label='NVE#3-SplitRatio:50%')

	pylab.legend(loc='best', ncol=3, mode="expand", borderaxespad=0.,fontsize='small')

	plt.ylabel(ytxt)
	plt.xlabel(xtxt)
	plt.title(title)

	x_limits, y_limits = plt.gca().get_ylim()
	plt.ylim(0, y_limits * 1.15 )

	formatter = FuncFormatter(to_percent)
	plt.gca().yaxis.set_major_formatter(formatter)

	plt.grid(True)

	plt.xticks(index + 2 * bar_width, timing_1)



	plt.tight_layout()


	print dirname + title + '.png'
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

# key_1 : FailureEmbedding
# key_1 : RequestEmbedding
# AccetpionRatio = 1 - FailureEmbedding / RequestEmbedding


showAllAcceptionRatioImage_1( 'FailureEmbedding', 'RequestEmbedding', limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Accetpion Ratio', 'Time Unit(s)', 'Evaluation of Virtual Network Request Accetpion Ratio_1')

showAllAcceptionRatioImage_2( 'FailureEmbedding', 'RequestEmbedding', limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Accepted Virtual Network Request(s)', 'Time Unit', 'Evaluation of Accepted Virtual Network Request')


showAllAcceptionRatioImage_3( 'FailureEmbedding', 'RequestEmbedding', limits, recordJson_1, recordJson_2, recordJson_3, recordJson_4, recordJson_5,'Accetpion Ratio', 'Time Unit(s)', 'Evaluation of Virtual Network Request Accetpion Ratio_3')


