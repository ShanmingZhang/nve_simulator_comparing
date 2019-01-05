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

	VirtualNetworkEmbedding *nve_1 = new VirtualNetworkEmbedding(fileName);

	int timing = 0;

//	while (true) {
//
//		if (0 == nve_1->InitiateEmbeddingVirtualNetworkEnvironment(timing)) {
//
//			cout
//					<< " A Virtual Network embedded successfully (Virtual Networks:"
//					<< nve_1->getNws().size() << ")." << endl;
//			break;
//		} else {
//			cout
//					<< " The Embedding Initiation of Virtual Network Environment Finished (Virtual Networks:"
//					<< nve_1->getNws().size() << ")." << endl;
//			SubNwGraph::checkSubstrateLinksResource(nve_1->getSubNw());
//			break;
//		}
//
//	}
//
//	/*
//	 * for comparing
//	 */
//	for (map<int, VirNwGraph*>::iterator vnIter = nve_1->getNws().begin();
//			vnIter != nve_1->getNws().end(); ++vnIter) {
//		nve_1->addComVirNwNos(vnIter->second->getVirNwNo(),
//				vnIter->second->getVirNwNo());
//
//		vnIter->second->setSameFlag(1);
//	}

	VirtualNetworkEmbedding *nve_3 =
			nve_1->copyVirtualNetworkEmbeddingEnvironment();
	SubNwGraph::checkSubstrateLinksResource(nve_3->getSubNw());

	map<string, EndUserRequest*> euRequests_default;
	map<string, EndUserRequest*> euRequests_dynamic;

	map<string, EndUserRequest*> euRequests_common;

	vector<int> vNwRequests = CommonFunctions::generateVirtualNetworkRequests();

	for (int timing = 0; timing < CommonConstants::VNE_ELAPSED_TIME_UNITS;
			++timing) {

		cout << " Current time :" << timing << endl;

		vector<int>::iterator iter = find(vNwRequests.begin(),
				vNwRequests.end(), timing);

		if (timing != 0 && iter != vNwRequests.end()) {

			//add #1
			nve_1->updateVirNwRequestRecords(timing, 1);
			nve_3->updateVirNwRequestRecords(timing, 1);

			bool flag_1 = false;
			bool flag_2 = false;

			VirNwGraph* virNwSingle = nve_1->constructVirtualNetwork(timing);
			VirNwGraph* virNwDynamic = virNwSingle->copyVirtualNetwork();

			if (0 == nve_1->EmbeddingVirtualNetwork(virNwSingle, timing)) {
				cout
						<< " A Virtual Network Embedded into NVE#1 successfully (Virtual Networks:"
						<< nve_1->getNws().size() << ")." << endl;
				flag_1 = true;

			}

			if (flag_1 == false) {
				VirNwGraph::ReleaseVirtualNetworkResource(virNwSingle);

				nve_1->updateFailureEmbeddingRecords(timing, 1);
			}

			if (0 == nve_3->EmbeddingVirtualNetwork(virNwDynamic, timing)) {
				cout
						<< " A Virtual Network Embedded into NVE#3 successfully (Virtual Networks:"
						<< nve_3->getNws().size() << ")." << endl;
				flag_2 = true;

			}

			if (flag_2 == false) {
				VirNwGraph::ReleaseVirtualNetworkResource(virNwDynamic);

				nve_3->updateFailureEmbeddingRecords(timing, 1);
			}

			if (flag_1 == true && flag_1 == flag_2) {
				/*
				 *  common virtual network including virtual topology
				 */
				nve_1->addComVirNwNos(virNwSingle->getVirNwNo(),
						virNwSingle->getVirNwNo());

				nve_3->addComVirNwNos(virNwDynamic->getVirNwNo(),
						virNwSingle->getVirNwNo());
				/*
				 *  completely common virtual networks including mapping
				 */
				if (1
						== VirNwGraph::compareTwoVirtualNetworks(virNwSingle,
								virNwDynamic)) {
					cout << " There are two completely virtual network."
							<< endl;

					virNwSingle->setSameFlag(1);
					virNwDynamic->setSameFlag(1);
				}
			}

			cout << " Currently, there are virtual networks ("
					<< nve_1->getNws().size() << ") embedded into NVE#1."
					<< endl;

			cout << " Currently, there are virtual networks ("
					<< nve_3->getNws().size() << ") embedded into NVE#3."
					<< endl;

		}

		// add #2
		nve_1->updateVirNwRequestRecords(timing, 0);
		nve_3->updateVirNwRequestRecords(timing, 0);

		//
		nve_1->updateFailureEmbeddingRecords(timing, 0);
		nve_3->updateFailureEmbeddingRecords(timing, 0);

// generate new end user request
		int requestAmount =
				RandomGenerator::getUserVideoRequestsAmountWithPoissonDistribution();

// place before perform end-user request function
		nve_1->updateNveDataSwitchingEnergy(timing);
		euRequests_default =
				nve_1->generateEndUserVideoRequestsForVirtualNetwork(timing,
						requestAmount);

		cout << " orginal reqeust size: " << euRequests_default.size() << endl;
		euRequests_common = nve_3->getComEndUserRequest(euRequests_default);
		cout << " common reqeust size: " << euRequests_common.size() << endl;

		nve_1->performVirtualNetworkEnvironment(timing, euRequests_default);

		nve_1->updateCurrentCommonEndUserReqs(timing, euRequests_common.size());

		nve_1->addEndUserVideoRequestIntoRecords(
				nve_1->getAvaliableEndUserRequests(timing, euRequests_default));

		SubNwGraph::checkSubstrateLinksResource(nve_1->getSubNw());

		nve_1->updateAmountOfVnsRecords(timing);
		nve_1->updateCurrentNumberOfVns(timing);
		nve_1->updateCurrentRevenueVirLinkAndNodeRecords(timing);
		nve_1->updateCurrentSubLinkEmbeddingResourceInfo(timing,
				CommonConstants::MIN_VNW_LINK_BANDWIDTH,
				CommonConstants::MAX_VNW_LINK_BANDWIDTH);
		nve_1->updateCurrentSameVirNws(timing);
		nve_1->updateCurrentComVirNws(timing);
		//
		nve_3->updateNveDataSwitchingEnergy(timing);
		map<string, EndUserRequest*> euRequests_3 =
				nve_3->generateEndUserVideoRequestsForVirtualNetwork(timing,
						requestAmount);

		cout << "  step0 Size: " << euRequests_3.size() << endl;
		euRequests_dynamic = nve_3->removeEndUserRequestofComVirNw(
				euRequests_3);
		cout << "  befor Size: " << euRequests_dynamic.size() << endl;

		for (map<string, EndUserRequest*>::iterator iter =
				euRequests_common.begin(); iter != euRequests_common.end();
				++iter) {
			map<string, EndUserRequest*>::iterator eIter =
					euRequests_dynamic.begin();
			euRequests_dynamic.insert(eIter,
					make_pair(iter->first, iter->second));
		}

		nve_3->performVirtualNetworkEnvironmentWithVirtualLinkSplittingRatio(
				timing, euRequests_dynamic,
				CommonConstants::NO_EQUA_ENDUSERL_DATARATE_SPLIT_FLAG_FOR_SUBSTRATE_PATH_OF_VIRTUAL_LINK);
		nve_3->updateCurrentCommonEndUserReqs(timing, euRequests_common.size());
		cout << "  after Size: " << euRequests_dynamic.size() << endl;
		nve_3->addEndUserVideoRequestIntoRecords(
				nve_3->getAvaliableEndUserRequests(timing, euRequests_dynamic));

		SubNwGraph::checkSubstrateLinksResource(nve_3->getSubNw());

		nve_3->updateAmountOfVnsRecords(timing);
		nve_3->updateCurrentNumberOfVns(timing);
		nve_3->updateCurrentRevenueVirLinkAndNodeRecords(timing);
		nve_3->updateCurrentSubLinkEmbeddingResourceInfo(timing,
				CommonConstants::MIN_VNW_LINK_BANDWIDTH,
				CommonConstants::MAX_VNW_LINK_BANDWIDTH);

		nve_3->updateCurrentSameVirNws(timing);
		nve_3->updateCurrentComVirNws(timing);

		euRequests_default.clear();
		euRequests_dynamic.clear();
		euRequests_common.clear();

		if (timing >= 100 && timing % 100 == 0) {

			timestr = timer->getEndTiming();

			//add #3
			VirtualNetworkEmbedding::OutputNveInfoToJson("NVE#1_" + timestr,
					"NVE#1",
					"NVE with Single Substrate Transport Paths: Each virtual link mapped into a static substrate data transport path. ",
					nve_1);

			VirtualNetworkEmbedding::OutputNveInfoToJson("NVE#3_" + timestr,
					"NVE#3",
					"NVE with Dynamic Substrate Transport Paths: Each virtual link mapped into a substrate data transport path and may dynamically reallocate a new substrate data transport path. ",
					nve_3);
		}
	}

	timestr = timer->getEndTiming();

	cout << " Currently, there are virtual networks (" << nve_1->getNws().size()
			<< ") embedded into NVE#1." << endl;

	SubNwGraph::checkSubstrateLinksResource(nve_1->getSubNw());
	SubNwGraph::checkSubstrateLinksResourceStatus(nve_1->getSubNw());

	// add #4
	VirtualNetworkEmbedding::OutputNveInfoToJson("NVE#1_" + timestr,
						"NVE#1",
						"NVE with Single Substrate Transport Paths: Each virtual link mapped into a static substrate data transport path. ",
						nve_1);


	cout << " Currently, there are virtual networks (" << nve_3->getNws().size()
			<< ") embedded into NVE#1." << endl;

	SubNwGraph::printSubstrateNetwork(nve_3->getSubNw());
	SubNwGraph::checkSubstrateLinksResource(nve_3->getSubNw());

	//add #5
	VirtualNetworkEmbedding::OutputNveInfoToJson("NVE#3_" + timestr,
						"NVE#3",
						"NVE with Dynamic Substrate Transport Paths: Each virtual link mapped into a substrate data transport path and may dynamically reallocate a new substrate data transport path. ",
						nve_3);

	// add #6
	VirtualNetworkEmbedding::OutPutNveInfoToImageFile("NVE#1", "NVE#3",
			nve_1, nve_3);


	timer->endTiming();
	timer->elapsedTime();
	delete timer;
	cout << " --- OK ---" << endl;
	return 0;
}
