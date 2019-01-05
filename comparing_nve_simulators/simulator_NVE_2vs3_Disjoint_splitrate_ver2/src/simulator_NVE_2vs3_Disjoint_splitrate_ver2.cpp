//============================================================================
// Name        : simulator.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <iterator>
#include <map>
#include <vector>

#include <fstream>

#include "algorithms/KShortestPaths.h"
#include "algorithms/ShortestPath.h"
#include "algorithms/ShortestPathWithFloyd.h"
#include "embed/VirtualNetworkEmbedding.h"
#include "generator/RandomGenerator.h"
#include "graphs/BaseGraph.h"
#include "graphs/SubNwGraph.h"
#include "graphs/BasePath.h"
#include "com/Timer.h"
#include "com/CommonConstants.h"

using namespace std;

template<class T1, class T2>
void printMapVector(const map<T1, vector<T2> > vtr) {
	cout << " printed map< string, vector>'s size: " << vtr.size() << endl;
	for (typename map<T1, vector<T2> >::const_iterator it = vtr.begin();
			it != vtr.end(); ++it) {
		cout << it->first << " : ";
		printVector(it->second);
		cout << endl;
	}
	cout << endl;
}

int main() {

	Timer * timer = new Timer();
	timer->startTiming();
	string timestr;

	string fileName = "./topologies/SubNW_50_5.brite";

	VirtualNetworkEmbedding *nve_2 = new VirtualNetworkEmbedding(fileName);

	int timing = 0;

	while (true) {

		if (0
				== nve_2->InitiateEmbeddingVirtualNetworkEnvironmentWithVirtualLinkSplittingRatio(
						timing,
						CommonConstants::DISJOINT_SUBSTRATE_PATH_TYPE_OF_VIRTUAL_LINK)) {

			cout
					<< " A Virtual Network embedded successfully (Virtual Networks:"
					<< nve_2->getNws().size() << ")." << endl;
			//break;
		} else {
			cout
					<< " The Embedding Initiation of Virtual Network Environment Finished (Virtual Networks:"
					<< nve_2->getNws().size() << ")." << endl;
			SubNwGraph::checkSubstrateLinksResource(nve_2->getSubNw());
			break;
		}
	}

	/*
	 * for comparing
	 */
	for (map<int, VirNwGraph*>::iterator vnIter = nve_2->getNws().begin();
			vnIter != nve_2->getNws().end(); ++vnIter) {
		nve_2->addComVirNwNos(vnIter->second->getVirNwNo(),
				vnIter->second->getVirNwNo());

		vnIter->second->setSameFlag(1);

	}

	VirtualNetworkEmbedding *nve_3_20 =
			nve_2->copyVirtualNetworkEmbeddingEnvironment();
	SubNwGraph::checkSubstrateLinksResource(nve_3_20->getSubNw());

	VirtualNetworkEmbedding *nve_3_30 =
			nve_2->copyVirtualNetworkEmbeddingEnvironment();
	SubNwGraph::checkSubstrateLinksResource(nve_3_30->getSubNw());

	VirtualNetworkEmbedding *nve_3_40 =
			nve_2->copyVirtualNetworkEmbeddingEnvironment();
	SubNwGraph::checkSubstrateLinksResource(nve_3_40->getSubNw());

	VirtualNetworkEmbedding *nve_3_50 =
			nve_2->copyVirtualNetworkEmbeddingEnvironment();
	SubNwGraph::checkSubstrateLinksResource(nve_3_50->getSubNw());

	map<string, EndUserRequest*> euReqs_nve_2;

	map<string, EndUserRequest*> euReqs_nve_3_20;
	map<string, EndUserRequest*> euReqs_nve_3_30;
	map<string, EndUserRequest*> euReqs_nve_3_40;
	map<string, EndUserRequest*> euReqs_nve_3_50;

	map<string, EndUserRequest*> com_euReqs_nve_3_20;
	map<string, EndUserRequest*> com_euReqs_nve_3_30;
	map<string, EndUserRequest*> com_euReqs_nve_3_40;
	map<string, EndUserRequest*> com_euReqs_nve_3_50;

	vector<int> vNwRequests = CommonFunctions::generateVirtualNetworkRequests();

	for (int timing = 0; timing < CommonConstants::VNE_ELAPSED_TIME_UNITS;
			++timing) {

		cout << " Current time :" << timing << endl;

		vector<int>::iterator iter = find(vNwRequests.begin(),
				vNwRequests.end(), timing);


		if (timing != 0 && iter != vNwRequests.end()) {

			bool flag_2 = false;
			bool flag_3_20 = false;
			bool flag_3_30 = false;
			bool flag_3_40 = false;
			bool flag_3_50 = false;

			VirNwGraph* virNw_2 = nve_2->constructVirtualNetwork(timing);
			VirNwGraph* virNw_3_20 = virNw_2->copyVirtualNetwork();
			VirNwGraph* virNw_3_30 = virNw_2->copyVirtualNetwork();
			VirNwGraph* virNw_3_40 = virNw_2->copyVirtualNetwork();
			VirNwGraph* virNw_3_50 = virNw_2->copyVirtualNetwork();

			if (0
					== nve_2->EmbeddingVirtualNetworkWithVirtualLinkSplittingRatio(
							virNw_2, timing,
							CommonConstants::DISJOINT_SUBSTRATE_PATH_TYPE_OF_VIRTUAL_LINK)) {
				cout
						<< " A Virtual Network Embedded into NVE#2 successfully (Virtual Networks:"
						<< nve_2->getNws().size() << ")." << endl;
				flag_2 = true;

			}

			if (flag_2 == false) {
				VirNwGraph::ReleaseVirtualNetworkResource(virNw_2);
				nve_2->updateFailureEmbeddingRecords(timing, 1);
			}

			//
			if (0
					== nve_3_20->EmbeddingVirtualNetworkWithVirtualLinkSplittingRatio(
							virNw_3_20, timing,
							CommonConstants::DISJOINT_SUBSTRATE_PATH_TYPE_OF_VIRTUAL_LINK)) {
				cout
						<< " A Virtual Network Embedded into NVE#3_20 successfully (Virtual Networks:"
						<< nve_3_20->getNws().size() << ")." << endl;
				flag_3_20 = true;
			}

			if (flag_3_20 == false) {
				VirNwGraph::ReleaseVirtualNetworkResource(virNw_3_20);
				nve_3_20->updateFailureEmbeddingRecords(timing, 1);
			}

			//
			if (0
					== nve_3_30->EmbeddingVirtualNetworkWithVirtualLinkSplittingRatio(
							virNw_3_30, timing,
							CommonConstants::DISJOINT_SUBSTRATE_PATH_TYPE_OF_VIRTUAL_LINK)) {
				cout
						<< " A Virtual Network Embedded into NVE#3_30 successfully (Virtual Networks:"
						<< nve_3_30->getNws().size() << ")." << endl;
				flag_3_30 = true;
			}

			if (flag_3_30 == false) {
				VirNwGraph::ReleaseVirtualNetworkResource(virNw_3_30);
				nve_3_30->updateFailureEmbeddingRecords(timing, 1);
			}

			//
			if (0
					== nve_3_40->EmbeddingVirtualNetworkWithVirtualLinkSplittingRatio(
							virNw_3_40, timing,
							CommonConstants::DISJOINT_SUBSTRATE_PATH_TYPE_OF_VIRTUAL_LINK)) {
				cout
						<< " A Virtual Network Embedded into NVE#3_40 successfully (Virtual Networks:"
						<< nve_3_40->getNws().size() << ")." << endl;
				flag_3_40 = true;
			}

			if (flag_3_40 == false) {
				VirNwGraph::ReleaseVirtualNetworkResource(virNw_3_40);
				nve_3_40->updateFailureEmbeddingRecords(timing, 1);
			}

			//
			if (0
					== nve_3_50->EmbeddingVirtualNetworkWithVirtualLinkSplittingRatio(
							virNw_3_50, timing,
							CommonConstants::DISJOINT_SUBSTRATE_PATH_TYPE_OF_VIRTUAL_LINK)) {
				cout
						<< " A Virtual Network Embedded into NVE#3_50 successfully (Virtual Networks:"
						<< nve_3_50->getNws().size() << ")." << endl;
				flag_3_50 = true;
			}

			if (flag_3_50 == false) {
				VirNwGraph::ReleaseVirtualNetworkResource(virNw_3_50);

				nve_3_50->updateFailureEmbeddingRecords(timing, 1);
			}
			//
			if (flag_2 == true && flag_2 == flag_3_20 && flag_2 == flag_3_30
					&& flag_2 == flag_3_40 && flag_2 == flag_3_50) {
				/*
				 *  common virtual network including virtual topology
				 */
				nve_2->addComVirNwNos(virNw_2->getVirNwNo(),
						virNw_2->getVirNwNo());

				nve_3_20->addComVirNwNos(virNw_3_20->getVirNwNo(),
						virNw_2->getVirNwNo());

				nve_3_30->addComVirNwNos(virNw_3_30->getVirNwNo(),
						virNw_2->getVirNwNo());

				nve_3_40->addComVirNwNos(virNw_3_40->getVirNwNo(),
						virNw_2->getVirNwNo());

				nve_3_50->addComVirNwNos(virNw_3_50->getVirNwNo(),
						virNw_2->getVirNwNo());

				/*
				 *  completely common virtual networks including mapping
				 */
				if ((1
						== VirNwGraph::compareTwoVirtualNetworks(virNw_2,
								virNw_3_20))
						&& (1
								== VirNwGraph::compareTwoVirtualNetworks(
										virNw_2, virNw_3_30))
						&& (1
								== VirNwGraph::compareTwoVirtualNetworks(
										virNw_2, virNw_3_40))
						&& (1
								== VirNwGraph::compareTwoVirtualNetworks(
										virNw_2, virNw_3_50))) {
					cout
							<< " There is a completely common virtual networks in virNw_1 and virNw_3_20 - 50."
							<< endl;

					virNw_2->setSameFlag(1);
					virNw_3_20->setSameFlag(1);
					virNw_3_30->setSameFlag(1);
					virNw_3_40->setSameFlag(1);
					virNw_3_50->setSameFlag(1);
				}
			}

			cout << " Currently, there are virtual networks in nve_2 ("
					<< nve_2->getNws().size() << ") embedded into NVE#2."
					<< endl;

			cout << " Currently, there are virtual networks in nve_3_20 ("
					<< nve_3_20->getNws().size() << ") embedded into NVE#3_20."
					<< endl;

			cout << " Currently, there are virtual networks in nve_3_30 ("
					<< nve_3_30->getNws().size() << ") embedded into NVE#3_30."
					<< endl;

			cout << " Currently, there are virtual networks in nve_3_40 ("
					<< nve_3_40->getNws().size() << ") embedded into NVE#3_40."
					<< endl;

			cout << " Currently, there are virtual networks in nve_3_50 ("
					<< nve_3_50->getNws().size() << ") embedded into NVE#3_50."
					<< endl;

		}


		nve_2->updateFailureEmbeddingRecords(timing, 0);

		nve_3_20->updateFailureEmbeddingRecords(timing, 0);

		nve_3_30->updateFailureEmbeddingRecords(timing, 0);

		nve_3_40->updateFailureEmbeddingRecords(timing, 0);

		nve_3_50->updateFailureEmbeddingRecords(timing, 0);
// generate new end user request
		int requestAmount =
				RandomGenerator::getUserVideoRequestsAmountWithPoissonDistribution();

// place before perform end-user request function
		nve_2->updateNveDataSwitchingEnergy(timing);
		euReqs_nve_2 = nve_2->generateEndUserVideoRequestsForVirtualNetwork(
				timing, requestAmount);

		com_euReqs_nve_3_20 = nve_3_20->getComEndUserRequest(euReqs_nve_2);
		com_euReqs_nve_3_30 = nve_3_30->getComEndUserRequest(euReqs_nve_2);
		com_euReqs_nve_3_40 = nve_3_40->getComEndUserRequest(euReqs_nve_2);
		com_euReqs_nve_3_50 = nve_3_50->getComEndUserRequest(euReqs_nve_2);

		nve_2->performVirtualNetworkEnvironmentWithVirtualLinkSplittingRatio(
				timing, euReqs_nve_2,
				CommonConstants::EQUAL_ENDUSER_DATARATE_SPLIT_FLAG_FOR_SUBSTRATE_PATH_OF_VIRTUAL_LINK);

		nve_2->updateCurrentCommonEndUserReqs(timing,
				com_euReqs_nve_3_20.size());

		nve_2->addEndUserVideoRequestIntoRecords(
				nve_2->getAvaliableEndUserRequests(timing, euReqs_nve_2));

		//nve_2->releaseEndUserVideoRequestsForVirtualNetwork(timing);

		SubNwGraph::checkSubstrateLinksResource(nve_2->getSubNw());

		nve_2->updateAmountOfVnsRecords(timing);
		nve_2->updateCurrentNumberOfVns(timing);
		nve_2->updateCurrentRevenueVirLinkAndNodeRecords(timing);
		nve_2->updateCurrentSubLinkEmbeddingResourceInfo(timing,
				CommonConstants::MIN_VNW_LINK_BANDWIDTH / 2,
				CommonConstants::MAX_VNW_LINK_BANDWIDTH / 2);
		nve_2->updateCurrentSameVirNws(timing);
		nve_2->updateCurrentComVirNws(timing);

		//
		CommonConstants::DYNAMIC_VIRTUAL_LINK_RESOURCE_ALLOCATION_SPLITTING_RATIO =
				0.2;
		cout << " 0.2 ratio: "
				<< CommonConstants::DYNAMIC_VIRTUAL_LINK_RESOURCE_ALLOCATION_SPLITTING_RATIO
				<< endl;
		nve_3_20->updateNveDataSwitchingEnergy(timing);
		map<string, EndUserRequest*> euReqs_3_20 =
				nve_3_20->generateEndUserVideoRequestsForVirtualNetwork(timing,
						requestAmount);

		euReqs_nve_3_20 = nve_3_20->removeEndUserRequestofComVirNw(euReqs_3_20);

		for (map<string, EndUserRequest*>::iterator iter =
				com_euReqs_nve_3_20.begin(); iter != com_euReqs_nve_3_20.end();
				++iter) {
			map<string, EndUserRequest*>::iterator eIter =
					euReqs_nve_3_20.begin();
			euReqs_nve_3_20.insert(eIter, make_pair(iter->first, iter->second));
		}

		nve_3_20->performVirtualNetworkEnvironmentWithVirtualLinkSplittingRatio(
				timing, euReqs_nve_3_20,
				CommonConstants::NO_EQUA_ENDUSERL_DATARATE_SPLIT_FLAG_FOR_SUBSTRATE_PATH_OF_VIRTUAL_LINK);
		nve_3_20->updateCurrentCommonEndUserReqs(timing,
				com_euReqs_nve_3_20.size());

		nve_3_20->addEndUserVideoRequestIntoRecords(
				nve_3_20->getAvaliableEndUserRequests(timing, euReqs_nve_3_20));

		SubNwGraph::checkSubstrateLinksResource(nve_3_20->getSubNw());

		nve_3_20->updateAmountOfVnsRecords(timing);
		nve_3_20->updateCurrentNumberOfVns(timing);
		nve_3_20->updateCurrentRevenueVirLinkAndNodeRecords(timing);
		nve_3_20->updateCurrentSubLinkEmbeddingResourceInfo(timing,
				CommonConstants::MIN_VNW_LINK_BANDWIDTH / 2,
				CommonConstants::MAX_VNW_LINK_BANDWIDTH / 2);
		nve_3_20->updateCurrentSameVirNws(timing);
		nve_3_20->updateCurrentComVirNws(timing);

		//
		CommonConstants::DYNAMIC_VIRTUAL_LINK_RESOURCE_ALLOCATION_SPLITTING_RATIO =
				0.3;
		cout << " 0.3 ratio: "
				<< CommonConstants::DYNAMIC_VIRTUAL_LINK_RESOURCE_ALLOCATION_SPLITTING_RATIO
				<< endl;

		nve_3_30->updateNveDataSwitchingEnergy(timing);
		map<string, EndUserRequest*> euReqs_3_30 =
				nve_3_30->generateEndUserVideoRequestsForVirtualNetwork(timing,
						requestAmount);

		euReqs_nve_3_30 = nve_3_30->removeEndUserRequestofComVirNw(euReqs_3_30);

		for (map<string, EndUserRequest*>::iterator iter =
				com_euReqs_nve_3_30.begin(); iter != com_euReqs_nve_3_30.end();
				++iter) {
			map<string, EndUserRequest*>::iterator eIter =
					euReqs_nve_3_30.begin();
			euReqs_nve_3_30.insert(eIter, make_pair(iter->first, iter->second));
		}

		nve_3_30->performVirtualNetworkEnvironmentWithVirtualLinkSplittingRatio(
				timing, euReqs_nve_3_30,
				CommonConstants::NO_EQUA_ENDUSERL_DATARATE_SPLIT_FLAG_FOR_SUBSTRATE_PATH_OF_VIRTUAL_LINK);
		nve_3_30->updateCurrentCommonEndUserReqs(timing,
				com_euReqs_nve_3_30.size());

		nve_3_30->addEndUserVideoRequestIntoRecords(
				nve_3_30->getAvaliableEndUserRequests(timing, euReqs_nve_3_30));

		SubNwGraph::checkSubstrateLinksResource(nve_3_30->getSubNw());

		nve_3_30->updateAmountOfVnsRecords(timing);
		nve_3_30->updateCurrentNumberOfVns(timing);
		nve_3_30->updateCurrentRevenueVirLinkAndNodeRecords(timing);
		nve_3_30->updateCurrentSubLinkEmbeddingResourceInfo(timing,
				CommonConstants::MIN_VNW_LINK_BANDWIDTH / 2,
				CommonConstants::MAX_VNW_LINK_BANDWIDTH / 2);
		nve_3_30->updateCurrentSameVirNws(timing);
		nve_3_30->updateCurrentComVirNws(timing);

		//
		CommonConstants::DYNAMIC_VIRTUAL_LINK_RESOURCE_ALLOCATION_SPLITTING_RATIO =
				0.4;
		cout << " 0.4 ratio: "
				<< CommonConstants::DYNAMIC_VIRTUAL_LINK_RESOURCE_ALLOCATION_SPLITTING_RATIO
				<< endl;

		nve_3_40->updateNveDataSwitchingEnergy(timing);
		map<string, EndUserRequest*> euReqs_3_40 =
				nve_3_40->generateEndUserVideoRequestsForVirtualNetwork(timing,
						requestAmount);

		euReqs_nve_3_40 = nve_3_40->removeEndUserRequestofComVirNw(euReqs_3_40);

		for (map<string, EndUserRequest*>::iterator iter =
				com_euReqs_nve_3_40.begin(); iter != com_euReqs_nve_3_40.end();
				++iter) {
			map<string, EndUserRequest*>::iterator eIter =
					euReqs_nve_3_40.begin();
			euReqs_nve_3_40.insert(eIter, make_pair(iter->first, iter->second));
		}

		nve_3_40->performVirtualNetworkEnvironmentWithVirtualLinkSplittingRatio(
				timing, euReqs_nve_3_40,
				CommonConstants::NO_EQUA_ENDUSERL_DATARATE_SPLIT_FLAG_FOR_SUBSTRATE_PATH_OF_VIRTUAL_LINK);
		nve_3_40->updateCurrentCommonEndUserReqs(timing,
				com_euReqs_nve_3_40.size());

		nve_3_40->addEndUserVideoRequestIntoRecords(
				nve_3_40->getAvaliableEndUserRequests(timing, euReqs_nve_3_40));

		SubNwGraph::checkSubstrateLinksResource(nve_3_40->getSubNw());

		nve_3_40->updateAmountOfVnsRecords(timing);
		nve_3_40->updateCurrentNumberOfVns(timing);
		nve_3_40->updateCurrentRevenueVirLinkAndNodeRecords(timing);
		nve_3_40->updateCurrentSubLinkEmbeddingResourceInfo(timing,
				CommonConstants::MIN_VNW_LINK_BANDWIDTH / 2,
				CommonConstants::MAX_VNW_LINK_BANDWIDTH / 2);
		nve_3_40->updateCurrentSameVirNws(timing);
		nve_3_40->updateCurrentComVirNws(timing);

		//
		CommonConstants::DYNAMIC_VIRTUAL_LINK_RESOURCE_ALLOCATION_SPLITTING_RATIO =
				0.5;
		cout << " 0.5 ratio: "
				<< CommonConstants::DYNAMIC_VIRTUAL_LINK_RESOURCE_ALLOCATION_SPLITTING_RATIO
				<< endl;

		nve_3_50->updateNveDataSwitchingEnergy(timing);
		map<string, EndUserRequest*> euReqs_3_50 =
				nve_3_50->generateEndUserVideoRequestsForVirtualNetwork(timing,
						requestAmount);

		euReqs_nve_3_50 = nve_3_50->removeEndUserRequestofComVirNw(euReqs_3_50);

		for (map<string, EndUserRequest*>::iterator iter =
				com_euReqs_nve_3_50.begin(); iter != com_euReqs_nve_3_50.end();
				++iter) {
			map<string, EndUserRequest*>::iterator eIter =
					euReqs_nve_3_50.begin();
			euReqs_nve_3_50.insert(eIter, make_pair(iter->first, iter->second));
		}

		nve_3_50->performVirtualNetworkEnvironmentWithVirtualLinkSplittingRatio(
				timing, euReqs_nve_3_50,
				CommonConstants::NO_EQUA_ENDUSERL_DATARATE_SPLIT_FLAG_FOR_SUBSTRATE_PATH_OF_VIRTUAL_LINK);
		nve_3_50->updateCurrentCommonEndUserReqs(timing,
				com_euReqs_nve_3_50.size());

		nve_3_50->addEndUserVideoRequestIntoRecords(
				nve_3_50->getAvaliableEndUserRequests(timing, euReqs_nve_3_50));

		SubNwGraph::checkSubstrateLinksResource(nve_3_50->getSubNw());

		nve_3_50->updateAmountOfVnsRecords(timing);
		nve_3_50->updateCurrentNumberOfVns(timing);
		nve_3_50->updateCurrentRevenueVirLinkAndNodeRecords(timing);
		nve_3_50->updateCurrentSubLinkEmbeddingResourceInfo(timing,
				CommonConstants::MIN_VNW_LINK_BANDWIDTH / 2,
				CommonConstants::MAX_VNW_LINK_BANDWIDTH / 2);
		nve_3_50->updateCurrentSameVirNws(timing);
		nve_3_50->updateCurrentComVirNws(timing);

		euReqs_nve_2.clear();
		euReqs_nve_3_20.clear();
		euReqs_nve_3_30.clear();
		euReqs_nve_3_40.clear();
		euReqs_nve_3_50.clear();

		com_euReqs_nve_3_20.clear();
		com_euReqs_nve_3_30.clear();
		com_euReqs_nve_3_40.clear();
		com_euReqs_nve_3_50.clear();

		if (timing >= 100 && timing % 100 == 0) {

			timestr = timer->getEndTiming();

			CommonFunctions::OutputRecordsIntoJsonFile("NVE#2_" + timestr,
					"NVE#2",
					"NVE with Single Substrate Transport Paths: Each virtual link mapped into a static substrate data transport path. ",
					nve_2->getCongestionRecords(), nve_2->getAmountVnsRecords(),
					nve_2->getCurrentNumberOfVns(),
					nve_2->getCurrentRevenueVirLinkRecords(),
					nve_2->getCurrentRevenueVirNodeRecords(),
					nve_2->getDataSwitchingEnergy(),
					nve_2->getTransportedDataVolume(),
					nve_2->getComDataSwitchingEnergy(),
					nve_2->getComTransportedDataVolume(),
					nve_2->getCurrentAvailableEndUserRequests(),

					nve_2->getSameVirNwDataSwitchingEnergy(),
					nve_2->getSameVirNwTransportedDataVolume(),
					nve_2->getCurrentCommonEndUserReqs(),
					nve_2->getCurrentEndingEndUserReqs(),
					nve_2->getCurrentEndingVirNws(),
					nve_2->getCurrentSubLinkResourceInfo(),

					nve_2->getCurrentEmbeddableSubLinksInfo(),

					nve_2->getCurrentSameVirNws(),
					nve_2->getCurrentComVirNws(),

					nve_2->getCurrentCostSubLinkRecords(),

			nve_2->getFailureEmbeddingRecords());

			CommonFunctions::OutputRecordsIntoJsonFile("NVE#3_20_" + timestr,
					"NVE#3_20",
					"NVE with Dynamic Substrate Transport Paths: Each virtual link mapped into a substrate data transport path and may dynamically reallocate a new substrate data transport path. ",
					nve_3_20->getCongestionRecords(),
					nve_3_20->getAmountVnsRecords(),
					nve_3_20->getCurrentNumberOfVns(),
					nve_3_20->getCurrentRevenueVirLinkRecords(),
					nve_3_20->getCurrentRevenueVirNodeRecords(),
					nve_3_20->getDataSwitchingEnergy(),
					nve_3_20->getTransportedDataVolume(),
					nve_3_20->getComDataSwitchingEnergy(),
					nve_3_20->getComTransportedDataVolume(),
					nve_3_20->getCurrentAvailableEndUserRequests(),

					nve_3_20->getSameVirNwDataSwitchingEnergy(),
					nve_3_20->getSameVirNwTransportedDataVolume(),
					nve_3_20->getCurrentCommonEndUserReqs(),
					nve_3_20->getCurrentEndingEndUserReqs(),
					nve_3_20->getCurrentEndingVirNws(),
					nve_3_20->getCurrentSubLinkResourceInfo(),

					nve_3_20->getCurrentEmbeddableSubLinksInfo(),

					nve_3_20->getCurrentSameVirNws(),
					nve_3_20->getCurrentComVirNws(),

					nve_3_20->getCurrentCostSubLinkRecords(),

					nve_3_20->getFailureEmbeddingRecords());

			CommonFunctions::OutputRecordsIntoJsonFile("NVE#3_30_" + timestr,
					"NVE#3_30",
					"NVE with Dynamic Substrate Transport Paths: Each virtual link mapped into a substrate data transport path and may dynamically reallocate a new substrate data transport path. ",
					nve_3_30->getCongestionRecords(),
					nve_3_30->getAmountVnsRecords(),
					nve_3_30->getCurrentNumberOfVns(),
					nve_3_30->getCurrentRevenueVirLinkRecords(),
					nve_3_30->getCurrentRevenueVirNodeRecords(),
					nve_3_30->getDataSwitchingEnergy(),
					nve_3_30->getTransportedDataVolume(),
					nve_3_30->getComDataSwitchingEnergy(),
					nve_3_30->getComTransportedDataVolume(),
					nve_3_30->getCurrentAvailableEndUserRequests(),

					nve_3_30->getSameVirNwDataSwitchingEnergy(),
					nve_3_30->getSameVirNwTransportedDataVolume(),
					nve_3_30->getCurrentCommonEndUserReqs(),
					nve_3_30->getCurrentEndingEndUserReqs(),
					nve_3_30->getCurrentEndingVirNws(),
					nve_3_30->getCurrentSubLinkResourceInfo(),

					nve_3_30->getCurrentEmbeddableSubLinksInfo(),

					nve_3_30->getCurrentSameVirNws(),
					nve_3_30->getCurrentComVirNws(),

					nve_3_30->getCurrentCostSubLinkRecords(),

					nve_3_30->getFailureEmbeddingRecords());

			CommonFunctions::OutputRecordsIntoJsonFile("NVE#3_40_" + timestr,
					"NVE#3_40",
					"NVE with Dynamic Substrate Transport Paths: Each virtual link mapped into a substrate data transport path and may dynamically reallocate a new substrate data transport path. ",
					nve_3_40->getCongestionRecords(),
					nve_3_40->getAmountVnsRecords(),
					nve_3_40->getCurrentNumberOfVns(),
					nve_3_40->getCurrentRevenueVirLinkRecords(),
					nve_3_40->getCurrentRevenueVirNodeRecords(),
					nve_3_40->getDataSwitchingEnergy(),
					nve_3_40->getTransportedDataVolume(),
					nve_3_40->getComDataSwitchingEnergy(),
					nve_3_40->getComTransportedDataVolume(),
					nve_3_40->getCurrentAvailableEndUserRequests(),

					nve_3_40->getSameVirNwDataSwitchingEnergy(),
					nve_3_40->getSameVirNwTransportedDataVolume(),
					nve_3_40->getCurrentCommonEndUserReqs(),
					nve_3_40->getCurrentEndingEndUserReqs(),
					nve_3_40->getCurrentEndingVirNws(),
					nve_3_40->getCurrentSubLinkResourceInfo(),

					nve_3_40->getCurrentEmbeddableSubLinksInfo(),

					nve_3_40->getCurrentSameVirNws(),
					nve_3_40->getCurrentComVirNws(),
					nve_3_40->getCurrentCostSubLinkRecords(),

					nve_3_40->getFailureEmbeddingRecords());

			CommonFunctions::OutputRecordsIntoJsonFile("NVE#3_50_" + timestr,
					"NVE#3_50",
					"NVE with Dynamic Substrate Transport Paths: Each virtual link mapped into a substrate data transport path and may dynamically reallocate a new substrate data transport path. ",
					nve_3_50->getCongestionRecords(),
					nve_3_50->getAmountVnsRecords(),
					nve_3_50->getCurrentNumberOfVns(),
					nve_3_50->getCurrentRevenueVirLinkRecords(),
					nve_3_50->getCurrentRevenueVirNodeRecords(),
					nve_3_50->getDataSwitchingEnergy(),
					nve_3_50->getTransportedDataVolume(),
					nve_3_50->getComDataSwitchingEnergy(),
					nve_3_50->getComTransportedDataVolume(),
					nve_3_50->getCurrentAvailableEndUserRequests(),

					nve_3_50->getSameVirNwDataSwitchingEnergy(),
					nve_3_50->getSameVirNwTransportedDataVolume(),
					nve_3_50->getCurrentCommonEndUserReqs(),
					nve_3_50->getCurrentEndingEndUserReqs(),
					nve_3_50->getCurrentEndingVirNws(),
					nve_3_50->getCurrentSubLinkResourceInfo(),

					nve_3_50->getCurrentEmbeddableSubLinksInfo(),

					nve_3_50->getCurrentSameVirNws(),
					nve_3_50->getCurrentComVirNws(),

					nve_3_50->getCurrentCostSubLinkRecords(),

					nve_3_50->getFailureEmbeddingRecords());

		}
	}

	timestr = timer->getEndTiming();

	SubNwGraph::checkSubstrateLinksResource(nve_2->getSubNw());
	SubNwGraph::checkSubstrateLinksResourceStatus(nve_2->getSubNw());

	CommonFunctions::OutputRecordsIntoJsonFile("NVE#2_" + timestr, "NVE#2",
			"NVE with Single Substrate Transport Paths: Each virtual link mapped into a static substrate data transport path. ",
			nve_2->getCongestionRecords(), nve_2->getAmountVnsRecords(),
			nve_2->getCurrentNumberOfVns(),
			nve_2->getCurrentRevenueVirLinkRecords(),
			nve_2->getCurrentRevenueVirNodeRecords(),
			nve_2->getDataSwitchingEnergy(), nve_2->getTransportedDataVolume(),
			nve_2->getComDataSwitchingEnergy(),
			nve_2->getComTransportedDataVolume(),
			nve_2->getCurrentAvailableEndUserRequests(),

			nve_2->getSameVirNwDataSwitchingEnergy(),
			nve_2->getSameVirNwTransportedDataVolume(),
			nve_2->getCurrentCommonEndUserReqs(),
			nve_2->getCurrentEndingEndUserReqs(),
			nve_2->getCurrentEndingVirNws(),
			nve_2->getCurrentSubLinkResourceInfo(),
			nve_2->getCurrentEmbeddableSubLinksInfo(),

			nve_2->getCurrentSameVirNws(), nve_2->getCurrentComVirNws(),

			nve_2->getCurrentCostSubLinkRecords(),

			nve_2->getFailureEmbeddingRecords());

	SubNwGraph::checkSubstrateLinksResource(nve_3_20->getSubNw());
	SubNwGraph::checkSubstrateLinksResourceStatus(nve_3_20->getSubNw());

	CommonFunctions::OutputRecordsIntoJsonFile("NVE#3_20_" + timestr,
			"NVE#3_20",
			"NVE with Dynamic Substrate Transport Paths: Each virtual link mapped into a substrate data transport path and may dynamically reallocate a new substrate data transport path. ",
			nve_3_20->getCongestionRecords(), nve_3_20->getAmountVnsRecords(),
			nve_3_20->getCurrentNumberOfVns(),
			nve_3_20->getCurrentRevenueVirLinkRecords(),
			nve_3_20->getCurrentRevenueVirNodeRecords(),
			nve_3_20->getDataSwitchingEnergy(),
			nve_3_20->getTransportedDataVolume(),
			nve_3_20->getComDataSwitchingEnergy(),
			nve_3_20->getComTransportedDataVolume(),
			nve_3_20->getCurrentAvailableEndUserRequests(),

			nve_3_20->getSameVirNwDataSwitchingEnergy(),
			nve_3_20->getSameVirNwTransportedDataVolume(),
			nve_3_20->getCurrentCommonEndUserReqs(),
			nve_3_20->getCurrentEndingEndUserReqs(),
			nve_3_20->getCurrentEndingVirNws(),
			nve_3_20->getCurrentSubLinkResourceInfo(),
			nve_3_20->getCurrentEmbeddableSubLinksInfo(),
			nve_3_20->getCurrentSameVirNws(), nve_3_20->getCurrentComVirNws(),

			nve_3_20->getCurrentCostSubLinkRecords(),

			nve_3_20->getFailureEmbeddingRecords());

	SubNwGraph::checkSubstrateLinksResource(nve_3_30->getSubNw());
	SubNwGraph::checkSubstrateLinksResourceStatus(nve_3_30->getSubNw());

	CommonFunctions::OutputRecordsIntoJsonFile("NVE#3_30_" + timestr,
			"NVE#3_30",
			"NVE with Dynamic Substrate Transport Paths: Each virtual link mapped into a substrate data transport path and may dynamically reallocate a new substrate data transport path. ",
			nve_3_30->getCongestionRecords(), nve_3_30->getAmountVnsRecords(),
			nve_3_30->getCurrentNumberOfVns(),
			nve_3_30->getCurrentRevenueVirLinkRecords(),
			nve_3_30->getCurrentRevenueVirNodeRecords(),
			nve_3_30->getDataSwitchingEnergy(),
			nve_3_30->getTransportedDataVolume(),
			nve_3_30->getComDataSwitchingEnergy(),
			nve_3_30->getComTransportedDataVolume(),
			nve_3_30->getCurrentAvailableEndUserRequests(),

			nve_3_30->getSameVirNwDataSwitchingEnergy(),
			nve_3_30->getSameVirNwTransportedDataVolume(),
			nve_3_30->getCurrentCommonEndUserReqs(),
			nve_3_30->getCurrentEndingEndUserReqs(),
			nve_3_30->getCurrentEndingVirNws(),
			nve_3_30->getCurrentSubLinkResourceInfo(),
			nve_3_30->getCurrentEmbeddableSubLinksInfo(),
			nve_3_30->getCurrentSameVirNws(), nve_3_30->getCurrentComVirNws(),

			nve_3_30->getCurrentCostSubLinkRecords(),

			nve_3_30->getFailureEmbeddingRecords());

	SubNwGraph::checkSubstrateLinksResource(nve_3_40->getSubNw());
	SubNwGraph::checkSubstrateLinksResourceStatus(nve_3_40->getSubNw());

	CommonFunctions::OutputRecordsIntoJsonFile("NVE#3_40_" + timestr,
			"NVE#3_40",
			"NVE with Dynamic Substrate Transport Paths: Each virtual link mapped into a substrate data transport path and may dynamically reallocate a new substrate data transport path. ",
			nve_3_40->getCongestionRecords(), nve_3_40->getAmountVnsRecords(),
			nve_3_40->getCurrentNumberOfVns(),
			nve_3_40->getCurrentRevenueVirLinkRecords(),
			nve_3_40->getCurrentRevenueVirNodeRecords(),
			nve_3_40->getDataSwitchingEnergy(),
			nve_3_40->getTransportedDataVolume(),
			nve_3_40->getComDataSwitchingEnergy(),
			nve_3_40->getComTransportedDataVolume(),
			nve_3_40->getCurrentAvailableEndUserRequests(),

			nve_3_40->getSameVirNwDataSwitchingEnergy(),
			nve_3_40->getSameVirNwTransportedDataVolume(),
			nve_3_40->getCurrentCommonEndUserReqs(),
			nve_3_40->getCurrentEndingEndUserReqs(),
			nve_3_40->getCurrentEndingVirNws(),
			nve_3_40->getCurrentSubLinkResourceInfo(),
			nve_3_40->getCurrentEmbeddableSubLinksInfo(),
			nve_3_40->getCurrentSameVirNws(), nve_3_40->getCurrentComVirNws(),

			nve_3_40->getCurrentCostSubLinkRecords(),

			nve_3_40->getFailureEmbeddingRecords());

	SubNwGraph::checkSubstrateLinksResource(nve_3_50->getSubNw());
	SubNwGraph::checkSubstrateLinksResourceStatus(nve_3_50->getSubNw());

	CommonFunctions::OutputRecordsIntoJsonFile("NVE#3_50_" + timestr,
			"NVE#3_50",
			"NVE with Dynamic Substrate Transport Paths: Each virtual link mapped into a substrate data transport path and may dynamically reallocate a new substrate data transport path. ",
			nve_3_50->getCongestionRecords(), nve_3_50->getAmountVnsRecords(),
			nve_3_50->getCurrentNumberOfVns(),
			nve_3_50->getCurrentRevenueVirLinkRecords(),
			nve_3_50->getCurrentRevenueVirNodeRecords(),
			nve_3_50->getDataSwitchingEnergy(),
			nve_3_50->getTransportedDataVolume(),
			nve_3_50->getComDataSwitchingEnergy(),
			nve_3_50->getComTransportedDataVolume(),
			nve_3_50->getCurrentAvailableEndUserRequests(),

			nve_3_50->getSameVirNwDataSwitchingEnergy(),
			nve_3_50->getSameVirNwTransportedDataVolume(),
			nve_3_50->getCurrentCommonEndUserReqs(),
			nve_3_50->getCurrentEndingEndUserReqs(),
			nve_3_50->getCurrentEndingVirNws(),
			nve_3_50->getCurrentSubLinkResourceInfo(),
			nve_3_50->getCurrentEmbeddableSubLinksInfo(),
			nve_3_50->getCurrentSameVirNws(), nve_3_50->getCurrentComVirNws(),

			nve_3_50->getCurrentCostSubLinkRecords(),

			nve_3_50->getFailureEmbeddingRecords());

	CommonFunctions::OutputRecordsIntoImageFile("NVE#2", "NVE#3-20",
			nve_2->getCongestionRecords(), nve_3_20->getCongestionRecords(),
			nve_2->getAmountVnsRecords(), nve_3_20->getAmountVnsRecords(),
			nve_2->getCurrentNumberOfVns(), nve_3_20->getCurrentNumberOfVns(),
			nve_2->getCurrentRevenueVirLinkRecords(),
			nve_3_20->getCurrentRevenueVirLinkRecords(),
			nve_2->getCurrentRevenueVirNodeRecords(),
			nve_3_20->getCurrentRevenueVirNodeRecords(),
			nve_2->getDataSwitchingEnergy(), nve_3_20->getDataSwitchingEnergy(),
			nve_2->getTransportedDataVolume(),
			nve_3_20->getTransportedDataVolume(),

			nve_2->getComDataSwitchingEnergy(),
			nve_3_20->getComDataSwitchingEnergy(),
			nve_2->getComTransportedDataVolume(),
			nve_3_20->getComTransportedDataVolume(),

			nve_2->getCurrentAvailableEndUserRequests(),
			nve_3_20->getCurrentAvailableEndUserRequests(),

			nve_2->getSameVirNwDataSwitchingEnergy(),
			nve_3_20->getSameVirNwDataSwitchingEnergy(),

			nve_2->getSameVirNwTransportedDataVolume(),
			nve_3_20->getSameVirNwTransportedDataVolume(),

			nve_2->getCurrentCommonEndUserReqs(),
			nve_3_20->getCurrentCommonEndUserReqs(),

			nve_2->getCurrentEndingEndUserReqs(),
			nve_3_20->getCurrentEndingEndUserReqs(),

			nve_2->getCurrentEndingVirNws(), nve_3_20->getCurrentEndingVirNws(),

			nve_2->getCurrentSubLinkResourceInfo(),
			nve_3_20->getCurrentSubLinkResourceInfo(),

			nve_2->getCurrentEmbeddableSubLinksInfo(),
			nve_3_20->getCurrentEmbeddableSubLinksInfo(),

			nve_2->getCurrentSameVirNws(), nve_3_20->getCurrentSameVirNws(),

			nve_2->getCurrentComVirNws(), nve_3_20->getCurrentComVirNws(),

			nve_2->getCurrentCostSubLinkRecords(),
			nve_3_20->getCurrentCostSubLinkRecords(),

			nve_2->getFailureEmbeddingRecords(),
			nve_3_20->getFailureEmbeddingRecords());

	CommonFunctions::OutputRecordsIntoImageFile("NVE#2", "NVE#3-30",
			nve_2->getCongestionRecords(), nve_3_30->getCongestionRecords(),
			nve_2->getAmountVnsRecords(), nve_3_30->getAmountVnsRecords(),
			nve_2->getCurrentNumberOfVns(), nve_3_30->getCurrentNumberOfVns(),
			nve_2->getCurrentRevenueVirLinkRecords(),
			nve_3_30->getCurrentRevenueVirLinkRecords(),
			nve_2->getCurrentRevenueVirNodeRecords(),
			nve_3_30->getCurrentRevenueVirNodeRecords(),
			nve_2->getDataSwitchingEnergy(), nve_3_30->getDataSwitchingEnergy(),
			nve_2->getTransportedDataVolume(),
			nve_3_30->getTransportedDataVolume(),

			nve_2->getComDataSwitchingEnergy(),
			nve_3_30->getComDataSwitchingEnergy(),
			nve_2->getComTransportedDataVolume(),
			nve_3_30->getComTransportedDataVolume(),

			nve_2->getCurrentAvailableEndUserRequests(),
			nve_3_30->getCurrentAvailableEndUserRequests(),

			nve_2->getSameVirNwDataSwitchingEnergy(),
			nve_3_30->getSameVirNwDataSwitchingEnergy(),

			nve_2->getSameVirNwTransportedDataVolume(),
			nve_3_30->getSameVirNwTransportedDataVolume(),

			nve_2->getCurrentCommonEndUserReqs(),
			nve_3_30->getCurrentCommonEndUserReqs(),

			nve_2->getCurrentEndingEndUserReqs(),
			nve_3_30->getCurrentEndingEndUserReqs(),

			nve_2->getCurrentEndingVirNws(), nve_3_30->getCurrentEndingVirNws(),

			nve_2->getCurrentSubLinkResourceInfo(),
			nve_3_30->getCurrentSubLinkResourceInfo(),

			nve_2->getCurrentEmbeddableSubLinksInfo(),
			nve_3_30->getCurrentEmbeddableSubLinksInfo(),

			nve_2->getCurrentSameVirNws(), nve_3_30->getCurrentSameVirNws(),

			nve_2->getCurrentComVirNws(), nve_3_30->getCurrentComVirNws(),

			nve_2->getCurrentCostSubLinkRecords(),
			nve_3_30->getCurrentCostSubLinkRecords(),

			nve_2->getFailureEmbeddingRecords(),
			nve_3_30->getFailureEmbeddingRecords());

	CommonFunctions::OutputRecordsIntoImageFile("NVE#2", "NVE#3-40",
			nve_2->getCongestionRecords(), nve_3_40->getCongestionRecords(),
			nve_2->getAmountVnsRecords(), nve_3_40->getAmountVnsRecords(),
			nve_2->getCurrentNumberOfVns(), nve_3_40->getCurrentNumberOfVns(),
			nve_2->getCurrentRevenueVirLinkRecords(),
			nve_3_40->getCurrentRevenueVirLinkRecords(),
			nve_2->getCurrentRevenueVirNodeRecords(),
			nve_3_40->getCurrentRevenueVirNodeRecords(),
			nve_2->getDataSwitchingEnergy(), nve_3_40->getDataSwitchingEnergy(),
			nve_2->getTransportedDataVolume(),
			nve_3_40->getTransportedDataVolume(),

			nve_2->getComDataSwitchingEnergy(),
			nve_3_40->getComDataSwitchingEnergy(),
			nve_2->getComTransportedDataVolume(),
			nve_3_40->getComTransportedDataVolume(),

			nve_2->getCurrentAvailableEndUserRequests(),
			nve_3_40->getCurrentAvailableEndUserRequests(),

			nve_2->getSameVirNwDataSwitchingEnergy(),
			nve_3_40->getSameVirNwDataSwitchingEnergy(),

			nve_2->getSameVirNwTransportedDataVolume(),
			nve_3_40->getSameVirNwTransportedDataVolume(),

			nve_2->getCurrentCommonEndUserReqs(),
			nve_3_40->getCurrentCommonEndUserReqs(),

			nve_2->getCurrentEndingEndUserReqs(),
			nve_3_40->getCurrentEndingEndUserReqs(),

			nve_2->getCurrentEndingVirNws(), nve_3_40->getCurrentEndingVirNws(),

			nve_2->getCurrentSubLinkResourceInfo(),
			nve_3_40->getCurrentSubLinkResourceInfo(),

			nve_2->getCurrentEmbeddableSubLinksInfo(),
			nve_3_40->getCurrentEmbeddableSubLinksInfo(),

			nve_2->getCurrentSameVirNws(), nve_3_40->getCurrentSameVirNws(),

			nve_2->getCurrentComVirNws(), nve_3_40->getCurrentComVirNws(),

			nve_2->getCurrentCostSubLinkRecords(),
			nve_3_40->getCurrentCostSubLinkRecords(),

			nve_2->getFailureEmbeddingRecords(),
			nve_3_40->getFailureEmbeddingRecords());

	CommonFunctions::OutputRecordsIntoImageFile("NVE#2", "NVE#3-50",
			nve_2->getCongestionRecords(), nve_3_50->getCongestionRecords(),
			nve_2->getAmountVnsRecords(), nve_3_50->getAmountVnsRecords(),
			nve_2->getCurrentNumberOfVns(), nve_3_50->getCurrentNumberOfVns(),
			nve_2->getCurrentRevenueVirLinkRecords(),
			nve_3_50->getCurrentRevenueVirLinkRecords(),
			nve_2->getCurrentRevenueVirNodeRecords(),
			nve_3_50->getCurrentRevenueVirNodeRecords(),
			nve_2->getDataSwitchingEnergy(), nve_3_50->getDataSwitchingEnergy(),
			nve_2->getTransportedDataVolume(),
			nve_3_50->getTransportedDataVolume(),

			nve_2->getComDataSwitchingEnergy(),
			nve_3_50->getComDataSwitchingEnergy(),
			nve_2->getComTransportedDataVolume(),
			nve_3_50->getComTransportedDataVolume(),

			nve_2->getCurrentAvailableEndUserRequests(),
			nve_3_50->getCurrentAvailableEndUserRequests(),

			nve_2->getSameVirNwDataSwitchingEnergy(),
			nve_3_50->getSameVirNwDataSwitchingEnergy(),

			nve_2->getSameVirNwTransportedDataVolume(),
			nve_3_50->getSameVirNwTransportedDataVolume(),

			nve_2->getCurrentCommonEndUserReqs(),
			nve_3_50->getCurrentCommonEndUserReqs(),

			nve_2->getCurrentEndingEndUserReqs(),
			nve_3_50->getCurrentEndingEndUserReqs(),

			nve_2->getCurrentEndingVirNws(), nve_3_50->getCurrentEndingVirNws(),

			nve_2->getCurrentSubLinkResourceInfo(),
			nve_3_50->getCurrentSubLinkResourceInfo(),

			nve_2->getCurrentEmbeddableSubLinksInfo(),
			nve_3_50->getCurrentEmbeddableSubLinksInfo(),

			nve_2->getCurrentSameVirNws(), nve_3_50->getCurrentSameVirNws(),

			nve_2->getCurrentComVirNws(), nve_3_50->getCurrentComVirNws(),

			nve_2->getCurrentCostSubLinkRecords(),
			nve_3_50->getCurrentCostSubLinkRecords(),

			nve_2->getFailureEmbeddingRecords(),
			nve_3_50->getFailureEmbeddingRecords());

	timer->endTiming();
	timer->elapsedTime();
	delete timer;
	cout << " --- OK ---" << endl;
	return 0;
}
