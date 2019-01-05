import json

from pyexcel_xlsx import save_data
from collections import OrderedDict


def getItemArray(list, name):
    itemList = []
    index = 0;
    for item in list:
        if index > 15000:
            break
        itemList.append(item[name])
        index = index + 1
    return itemList

subname = '2017-05-1515:03:27_recordsOutput.json'


nve_1_file = 'NVE#1_' + subname

nve_2_file = 'NVE#3_20_' + subname

nve_3_file = 'NVE#3_30_' + subname

nve_4_file = 'NVE#3_40_' + subname

nve_5_file = 'NVE#3_50_' + subname

recordJson_1 = json.loads(open(nve_1_file).read())
recordJson_2 = json.loads(open(nve_2_file).read())
recordJson_3 = json.loads(open(nve_3_file).read())
recordJson_4 = json.loads(open(nve_4_file).read())
recordJson_5 = json.loads(open(nve_5_file).read())


data = OrderedDict()

# print recordJson_1.keys()

 
# SublinkResourceUtilization

# SameVirNwSubCost
# DataSwichingEnergy
# CurrentSubLinkResourceMaxInfo
# SameVirNwEmbeddedBandwidth
# EmbeddedNodes
# Type
# AmountVirNws
# CurrentSubLinkResourceMinInfo
# CurrentEndingEndUserReqs
# Description
# ComTransportedDataVolume
# EmbeddedBandwidth
# SameVirNwTransportedDataVolume
# RequestEmbedding
# CurrentSameVirNws
# SameVirNwVNodes
# CongestionRecords
# FailureEmbedding
# TransportedDataVolume
# CurrentEndUserRequests
# EmbeddableSubLinkResourceInfo
# CurrentComVirNws
# ComDataSwichingEnergy
# SublinkCost
# AvailableVirNws
# SameVirNwDataSwitchingEnergy
# CurrentCommonEndUserReqs
# SameVirNwEmbeddedLinks
# CurrentEndingVirNws
# EmbeddedLinks

for key in recordJson_1.keys():
    if key != 'Type' and  key != 'Description'  and key != 'Type':
        print key
        data.update({key: 
             [
                 getItemArray(recordJson_1[key], 'Timing'), 
                 getItemArray(recordJson_1[key], 'Total'), 
                 getItemArray(recordJson_2[key], 'Total'), 
                 getItemArray(recordJson_3[key], 'Total'), 
                 getItemArray(recordJson_4[key], 'Total'), 
                 getItemArray(recordJson_5[key], 'Total')
             ]
            }
        )
    
# data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6]]})
# data.update({"Sheet 2": [["row 1", "row 2", "row 3"]]})
save_data("data_" + subname.replace('.json', '') + ".xlsx", data)
