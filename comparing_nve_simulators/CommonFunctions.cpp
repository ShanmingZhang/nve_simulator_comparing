/*
 * CommonFunctions.cpp
 *
 *  Created on: Dec 3, 2016
 *      Author: ubean
 */

#include "CommonFunctions.h"

#include "../matplot/matplotlibcpp.h"
using namespace std;

namespace plt = matplotlibcpp;
CommonFunctions::CommonFunctions() {
	// TODO Auto-generated constructor stub

}

CommonFunctions::~CommonFunctions() {
	// TODO Auto-generated destructor stub
}

/*
 * linkId format : from_to
 */
string CommonFunctions::makeLinkId(const string from, const string to) {
	string str;
	str = from + '_' + to;
	return str;
}

string CommonFunctions::makePathId(const string from, const string to) {
	string str;
	str = from + '_' + to;
	return str;
}

string CommonFunctions::makeEndUserRequestId(const string vNwNo,
		const string timing, const string seqNo) {
	string str;
	str = vNwNo + '_' + timing + '_' + seqNo;
	return str;
}

vector<string> CommonFunctions::stringSplit(const string &str, char sep) {
	vector<string> v;
	stringstream ss(str);
	string buffer;
	while (getline(ss, buffer, sep)) {
		v.push_back(buffer);
	}
	return v;

}

string CommonFunctions::CoverIntegerToString(const int integer) {
	stringstream ss;
	ss << integer;
	return ss.str();
}

string CommonFunctions::CoverDoubleToString(const double data) {
	stringstream ss;
	ss << data;
	return ss.str();
}

void CommonFunctions::SleepThread(int hours, int minutes, int seconds) {
	using std::chrono::system_clock;
	time_t tt = system_clock::to_time_t(system_clock::now());

	struct tm * ptm = std::localtime(&tt);
	cout << "Current time: " << put_time(ptm, "%X") << '\n';

	cout << "Waiting for the " << hours << " hours " << minutes << " minutes "
			<< seconds << " seconds to begin...\n";
	ptm->tm_hour = ptm->tm_hour + hours;
	ptm->tm_min = ptm->tm_min + minutes;
	ptm->tm_sec = ptm->tm_sec + seconds;
	this_thread::sleep_until(system_clock::from_time_t(mktime(ptm)));

	cout << put_time(ptm, "%X") << " reached!\n";
}

void CommonFunctions::FAILURE_EXIT() {
	exit(1);
}

void CommonFunctions::printVector(vector<string> vtr) {
	cout << " printed vector's size: " << vtr.size() << endl;
	for (typename vector<string>::const_iterator it = vtr.begin();
			it != vtr.end(); ++it) {
		cout << *it << " ";
	}
	cout << endl;
}

void CommonFunctions::printMap(map<string, string> vtr) {
	cout << " printed map's size: " << vtr.size() << endl;
	for (typename map<string, string>::iterator it = vtr.begin();
			it != vtr.end(); ++it) {
		cout << it->first << " : " << it->second << endl;
	}
	cout << endl;
}

void CommonFunctions::printMapInteger(map<int, int> vtr) {
	cout << " printed map's size: " << vtr.size() << endl;
	for (typename map<int, int>::iterator it = vtr.begin(); it != vtr.end();
			++it) {
		cout << it->first << " : " << it->second << endl;
	}
	cout << endl;
}

void CommonFunctions::printMultimapMapIntegerString(multimap<int, string> vtr) {
	cout << " printed multimap's size: " << vtr.size() << endl;
	for (typename multimap<int, string>::iterator it = vtr.begin();
			it != vtr.end(); ++it) {
		cout << it->first << " : " << it->second << endl;
	}
	cout << endl;
}

vector<int> CommonFunctions::generateVirtualNetworkRequests() {
	//return RandomGenerator::getVirtualNetworkEmebeddingRequestsWithExponentialDistribution();
	return RandomGenerator::getVirtualNetworkEmebeddingRequestsWithUniformDistribution();
}

void CommonFunctions::printFailureMessageAndExit(const string errorMessage,
		const string functionName) {
	MessageSet::printErrorMessage(errorMessage);
	MessageSet::printFailureExitMessage(functionName);
	CommonFunctions::FAILURE_EXIT();
}

void CommonFunctions::printWarningMessage(const string warningMessage) {
	MessageSet::printWarningMessage(warningMessage);
}

void CommonFunctions::printInfoMessage(const string infoMessage) {
	MessageSet::printInfoMessage(infoMessage);
}

void CommonFunctions::OutputRecordsIntoImageFile(const string type_1,
		const string type_2, multimap<int, string> congestionRecords_1,
		multimap<int, string> congestionRecords_2,
		map<int, int> amountVirNwsRecords_1,
		map<int, int> amountVirNwsRecords_2, map<int, int> currentNumberOfVns_1,
		map<int, int> currentNumberOfVns_2,
		map<int, pair<int, double>> currentRevenueVirLinkRecords_1,
		map<int, pair<int, double>> currentRevenueVirLinkRecords_2,
		map<int, int> currentRevenueVirNodeRecords_1,
		map<int, int> currentRevenueVirNodeRecords_2,
		map<int, double> dataSwitchingEnergy_1,
		map<int, double> dataSwitchingEnergy_2,
		map<int, double> transportedDataVolume_1,
		map<int, double> transportedDataVolume_2,

		map<int, double> comDataSwitchingEnergy_1,
		map<int, double> comDataSwitchingEnergy_2,
		map<int, double> comTransportedDataVolume_1,
		map<int, double> comTransportedDataVolume_2,

		map<int, int> currentEndUserRequests_1,
		map<int, int> currentEndUserRequests_2,

		map<int, double> sameVirNwDataSwitchingEnergy_1,
		map<int, double> sameVirNwDataSwitchingEnergy_2,

		map<int, double> sameVirNwTransportedDataVolume_1,
		map<int, double> sameVirNwTransportedDataVolume_2,

		map<int, unsigned int> currentCommonEndUserReqs_1,
		map<int, unsigned int> currentCommonEndUserReqs_2,

		map<int, int> currentEndingEndUserReqs_1,
		map<int, int> currentEndingEndUserReqs_2,

		map<int, int> currentEndingVirNws_1,
		map<int, int> currentEndingVirNws_2,

		map<int, pair<int, int>> currentSubLinkResourceInfo_1,
		map<int, pair<int, int>> currentSubLinkResourceInfo_2,

		map<int, int> currentEmbeddableSubLinksInfo_1,
		map<int, int> currentEmbeddableSubLinksInfo_2,

		map<int, int> currentSameVirNws_1, map<int, int> currentSameVirNws_2,

		map<int, int> currentComVirNws_1, map<int, int> currentComVirNws_2,
		map<int, double> currentCostSubLinkRecords_1,
		map<int, double> currentCostSubLinkRecords_2,

		map<int, int> failureEmbeddingRecords_1,
		map<int, int> failureEmbeddingRecords_2,

		//
		map<int, int> virNwRequestRecords_1,
		map<int, int> virNwRequestRecords_2,

		map<int, pair<int, double>> currentSameVirNwsRevenueVirLinkRecords_1,
		map<int, pair<int, double>> currentSameVirNwsRevenueVirLinkRecords_2,

		map<int, int> currentSameVirNwsRevenueVirNodeRecords_1,
		map<int, int> currentSameVirNwsRevenueVirNodeRecords_2,

		map<int, double> currentSameVirNwsCostSubLinkRecords_1,
		map<int, double> currentSameVirNwsCostSubLinkRecords_2,

		map<int, double> currentSubLinksResourceUtilization_1,
		map<int, double> currentSubLinksResourceUtilization_2) {

	vector<double>::iterator cIter;
	vector<double> congestion1;
	vector<double> congestion2;
	vector<double> timing;

	for (int index = 0; index < CommonConstants::VNE_ELAPSED_TIME_UNITS;
			++index) {
		cIter = timing.begin();
		timing.insert(cIter, index);
		cIter = congestion1.begin();
		congestion1.insert(cIter, congestionRecords_1.count(index));
	}

	for (int index = 0; index < CommonConstants::VNE_ELAPSED_TIME_UNITS;
			++index) {
		cIter = congestion2.begin();
		congestion2.insert(cIter, congestionRecords_2.count(index));
	}

	plt::named_plot(type_1, timing, congestion1);
	plt::named_plot(type_2, timing, congestion2);
	plt::title("Evaluation of End-user Request Congestion(s)");

	plt::xlabel("Time Unit(s)");
	plt::ylabel("Congestion(s)");
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> AmountNws_1;
	for (map<int, int>::iterator iter = amountVirNwsRecords_1.begin();
			iter != amountVirNwsRecords_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, (iter->first));

		cIter = AmountNws_1.begin();
		AmountNws_1.insert(cIter, iter->second);
	}

	vector<double> AmountNws_2;
	for (map<int, int>::iterator iter = amountVirNwsRecords_2.begin();
			iter != amountVirNwsRecords_2.end(); ++iter) {
		cIter = AmountNws_2.begin();
		AmountNws_2.insert(cIter, iter->second);
	}

	plt::named_plot(type_1, timing, AmountNws_1);
	plt::named_plot(type_2, timing, AmountNws_2);
	//plt::ylim(0, 60);
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::title("Evaluation of Embedded Virtual Network(s)");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Virtual Network(s)");
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> AvailableNws_1;
	for (map<int, int>::iterator iter = currentNumberOfVns_1.begin();
			iter != currentNumberOfVns_1.end(); ++iter) {

		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = AvailableNws_1.begin();
		AvailableNws_1.insert(cIter, iter->second);

	}

	vector<double> AvailableNws_2;
	for (map<int, int>::iterator iter = currentNumberOfVns_2.begin();
			iter != currentNumberOfVns_2.end(); ++iter) {

		cIter = AvailableNws_2.begin();
		AvailableNws_2.insert(cIter, iter->second);

	}

	plt::named_plot(type_1, timing, AvailableNws_1);
	plt::named_plot(type_2, timing, AvailableNws_2);

	plt::title("Evaluation of Available Virtual Network(s)");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Virtual Network(s)");
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	//plt::ylim(0, 60);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> embedlinks_1;
	for (map<int, int>::iterator iter = currentEmbeddableSubLinksInfo_1.begin();
			iter != currentEmbeddableSubLinksInfo_1.end(); ++iter) {

		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = embedlinks_1.begin();
		embedlinks_1.insert(cIter, iter->second);

	}

	vector<double> embedlinks_2;
	for (map<int, int>::iterator iter = currentEmbeddableSubLinksInfo_2.begin();
			iter != currentEmbeddableSubLinksInfo_2.end(); ++iter) {

		cIter = embedlinks_2.begin();
		embedlinks_2.insert(cIter, iter->second);

	}

	plt::named_plot(type_1 + "-among 30M and 100M", timing, embedlinks_1);
	plt::named_plot(type_2 + "-among 30M and 100M", timing, embedlinks_2);

	plt::title("Evaluation of Embeddable Bandwidth for Substrate Links");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Substrate Link(s)");
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	//plt::ylim(0, 60);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> swichingEnergy_1;
	for (map<int, double>::iterator iter = dataSwitchingEnergy_1.begin();
			iter != dataSwitchingEnergy_1.end(); ++iter) {

		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = swichingEnergy_1.begin();
		swichingEnergy_1.insert(cIter, iter->second);

	}

	vector<double> swichingEnergy_2;
	for (map<int, double>::iterator iter = dataSwitchingEnergy_2.begin();
			iter != dataSwitchingEnergy_2.end(); ++iter) {

		cIter = swichingEnergy_2.begin();
		swichingEnergy_2.insert(cIter, iter->second);

	}

	plt::named_plot(type_1, timing, swichingEnergy_1);
	plt::named_plot(type_2, timing, swichingEnergy_2);

	plt::title("Evaluation of Data Switching Energy Consumption");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Switching Energy(Joule)");
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> sameSwichingEnergy_1;
	for (map<int, double>::iterator iter =
			sameVirNwDataSwitchingEnergy_1.begin();
			iter != sameVirNwDataSwitchingEnergy_1.end(); ++iter) {

		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = sameSwichingEnergy_1.begin();
		sameSwichingEnergy_1.insert(cIter, iter->second);

	}

	vector<double> sameSwichingEnergy_2;
	for (map<int, double>::iterator iter =
			sameVirNwDataSwitchingEnergy_2.begin();
			iter != sameVirNwDataSwitchingEnergy_2.end(); ++iter) {

		cIter = sameSwichingEnergy_2.begin();
		sameSwichingEnergy_2.insert(cIter, iter->second);

	}

	plt::named_plot(type_1, timing, sameSwichingEnergy_1);
	plt::named_plot(type_2, timing, sameSwichingEnergy_2);

	plt::title(
			"Evaluation of Data Switching Energy Consumption for The Same Virtual Networks");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Switching Energy(Joule)");
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> comSwichingEnergy_1;
	for (map<int, double>::iterator iter = comDataSwitchingEnergy_1.begin();
			iter != comDataSwitchingEnergy_1.end(); ++iter) {

		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = comSwichingEnergy_1.begin();
		comSwichingEnergy_1.insert(cIter, iter->second);

	}

	vector<double> comSwichingEnergy_2;
	for (map<int, double>::iterator iter = comDataSwitchingEnergy_2.begin();
			iter != comDataSwitchingEnergy_2.end(); ++iter) {

		cIter = comSwichingEnergy_2.begin();
		comSwichingEnergy_2.insert(cIter, iter->second);

	}

	plt::named_plot(type_1, timing, comSwichingEnergy_1);
	plt::named_plot(type_2, timing, comSwichingEnergy_2);

	plt::title(
			"Evaluation of Data Switching Energy Consumption for Common Virtual Networks");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Switching Energy(Joule)");
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> EmbeddedLinks_1;
	for (map<int, pair<int, double>>::iterator iter =
			currentRevenueVirLinkRecords_1.begin();
			iter != currentRevenueVirLinkRecords_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = EmbeddedLinks_1.begin();
		EmbeddedLinks_1.insert(cIter, iter->second.first);

	}

	vector<double> EmbeddedLinks_2;
	for (map<int, pair<int, double>>::iterator iter =
			currentRevenueVirLinkRecords_2.begin();
			iter != currentRevenueVirLinkRecords_2.end(); ++iter) {

		cIter = EmbeddedLinks_2.begin();
		EmbeddedLinks_2.insert(cIter, iter->second.first);

	}

	plt::named_plot(type_1, timing, EmbeddedLinks_1);
	plt::named_plot(type_2, timing, EmbeddedLinks_2);

	plt::title("Evaluation of Embedded Virtual Link(s)");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Virtual Link(s)");
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> EmbeddedNodes_1;
	for (map<int, int>::iterator iter = currentRevenueVirNodeRecords_1.begin();
			iter != currentRevenueVirNodeRecords_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = EmbeddedNodes_1.begin();
		EmbeddedNodes_1.insert(cIter, iter->second);

	}

	vector<double> EmbeddedNodes_2;
	for (map<int, int>::iterator iter = currentRevenueVirNodeRecords_2.begin();
			iter != currentRevenueVirNodeRecords_2.end(); ++iter) {

		cIter = EmbeddedNodes_2.begin();
		EmbeddedNodes_2.insert(cIter, iter->second);

	}

	plt::named_plot(type_1, timing, EmbeddedNodes_1);
	plt::named_plot(type_2, timing, EmbeddedNodes_2);

	plt::title("Evaluation of Embedded Virtual Node(s)");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Virtual Node(s)");
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> EmbeddedBandwidth_1;
	for (map<int, pair<int, double>>::iterator iter =
			currentRevenueVirLinkRecords_1.begin();
			iter != currentRevenueVirLinkRecords_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = EmbeddedBandwidth_1.begin();
		EmbeddedBandwidth_1.insert(cIter, iter->second.second);

	}
	vector<double> EmbeddedBandwidth_2;
	for (map<int, pair<int, double>>::iterator iter =
			currentRevenueVirLinkRecords_2.begin();
			iter != currentRevenueVirLinkRecords_2.end(); ++iter) {
		cIter = EmbeddedBandwidth_2.begin();
		EmbeddedBandwidth_2.insert(cIter, iter->second.second);
	}

	plt::named_plot(type_1, timing, EmbeddedBandwidth_1);
	plt::named_plot(type_2, timing, EmbeddedBandwidth_2);

	plt::title("Evaluation of Embedded Bandwidth");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Bandwidth(Mbps)");
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> dataVolume_1;
	for (map<int, double>::iterator iter = transportedDataVolume_1.begin();
			iter != transportedDataVolume_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = dataVolume_1.begin();
		dataVolume_1.insert(cIter, iter->second);

	}
	vector<double> dataVolume_2;
	for (map<int, double>::iterator iter = transportedDataVolume_2.begin();
			iter != transportedDataVolume_2.end(); ++iter) {
		cIter = dataVolume_2.begin();
		dataVolume_2.insert(cIter, iter->second);
	}

	plt::named_plot(type_1, timing, dataVolume_1);
	plt::named_plot(type_2, timing, dataVolume_2);

	plt::title("Evaluation of Switching Data Volume");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Data Volume(Megabits)");
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> sameDataVolume_1;
	for (map<int, double>::iterator iter =
			sameVirNwTransportedDataVolume_1.begin();
			iter != sameVirNwTransportedDataVolume_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = sameDataVolume_1.begin();
		sameDataVolume_1.insert(cIter, iter->second);

	}
	vector<double> sameDataVolume_2;
	for (map<int, double>::iterator iter =
			sameVirNwTransportedDataVolume_2.begin();
			iter != sameVirNwTransportedDataVolume_2.end(); ++iter) {
		cIter = sameDataVolume_2.begin();
		sameDataVolume_2.insert(cIter, iter->second);
	}

	plt::named_plot(type_1, timing, sameDataVolume_1);
	plt::named_plot(type_2, timing, sameDataVolume_2);

	plt::title(
			"Evaluation of Switching Data Volume for The Same Virtual Networks");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Data Volume(Megabits)");
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> comDataVolume_1;
	for (map<int, double>::iterator iter = comTransportedDataVolume_1.begin();
			iter != comTransportedDataVolume_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = comDataVolume_1.begin();
		comDataVolume_1.insert(cIter, iter->second);

	}
	vector<double> comDataVolume_2;
	for (map<int, double>::iterator iter = comTransportedDataVolume_2.begin();
			iter != comTransportedDataVolume_2.end(); ++iter) {
		cIter = comDataVolume_2.begin();
		comDataVolume_2.insert(cIter, iter->second);
	}

	plt::named_plot(type_1, timing, comDataVolume_1);
	plt::named_plot(type_2, timing, comDataVolume_2);

	plt::title(
			"Evaluation of Switching Data Volume for Common Virtual Networks");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Data Volume(Megabits)");
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> request_1;
	for (map<int, int>::iterator iter = currentEndUserRequests_1.begin();
			iter != currentEndUserRequests_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = request_1.begin();
		request_1.insert(cIter, iter->second);

	}
	vector<double> request_2;
	for (map<int, int>::iterator iter = currentEndUserRequests_2.begin();
			iter != currentEndUserRequests_2.end(); ++iter) {
		cIter = request_2.begin();
		request_2.insert(cIter, iter->second);
	}

	plt::named_plot(type_1, timing, request_1);
	plt::named_plot(type_2, timing, request_2);

	plt::title("Evaluation of End-user Request(s)");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("End-user Request(s)");

	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> comRequest_1;
	for (map<int, unsigned int>::iterator iter =
			currentCommonEndUserReqs_1.begin();
			iter != currentCommonEndUserReqs_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = comRequest_1.begin();
		comRequest_1.insert(cIter, iter->second);

	}
	vector<double> comRequest_2;
	for (map<int, unsigned int>::iterator iter =
			currentCommonEndUserReqs_2.begin();
			iter != currentCommonEndUserReqs_2.end(); ++iter) {
		cIter = comRequest_2.begin();
		comRequest_2.insert(cIter, iter->second);
	}

	plt::named_plot(type_1, timing, comRequest_1);
	plt::named_plot(type_2, timing, comRequest_2);

	plt::title("Evaluation of End-user Request(s) for Common Virtual Networks");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("End-user Request(s)");

	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> endingRequest_1;
	for (map<int, int>::iterator iter = currentEndingEndUserReqs_1.begin();
			iter != currentEndingEndUserReqs_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = endingRequest_1.begin();
		endingRequest_1.insert(cIter, iter->second);

	}

	vector<double> endingRequest_2;
	for (map<int, int>::iterator iter = currentEndingEndUserReqs_2.begin();
			iter != currentEndingEndUserReqs_2.end(); ++iter) {
		cIter = endingRequest_2.begin();
		endingRequest_2.insert(cIter, iter->second);
	}

	plt::named_plot(type_1, timing, endingRequest_1);
	plt::named_plot(type_2, timing, endingRequest_2);

	plt::title("Evaluation of Ending End-user Request(s)");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("End-user Request(s)");

	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> endingVirNws_1;
	for (map<int, int>::iterator iter = currentEndingVirNws_1.begin();
			iter != currentEndingVirNws_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = endingVirNws_1.begin();
		endingVirNws_1.insert(cIter, iter->second);

	}
	vector<double> endingVirNws_2;
	for (map<int, int>::iterator iter = currentEndingVirNws_2.begin();
			iter != currentEndingVirNws_2.end(); ++iter) {
		cIter = endingVirNws_2.begin();
		endingVirNws_2.insert(cIter, iter->second);
	}

	plt::named_plot(type_1, timing, endingVirNws_1);
	plt::named_plot(type_2, timing, endingVirNws_2);

	plt::title("Evaluation of Ending Virtual Network(s)");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Virtual Network(s)");

	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> minSublinks_1;
	vector<double> maxSublinks_1;
	for (map<int, pair<int, int>>::iterator iter =
			currentSubLinkResourceInfo_1.begin();
			iter != currentSubLinkResourceInfo_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = minSublinks_1.begin();
		minSublinks_1.insert(cIter, iter->second.first);

		cIter = maxSublinks_1.begin();
		maxSublinks_1.insert(cIter, iter->second.second);

	}

	vector<double> minSublinks_2;
	vector<double> maxSublinks_2;
	for (map<int, pair<int, int>>::iterator iter =
			currentSubLinkResourceInfo_2.begin();
			iter != currentSubLinkResourceInfo_2.end(); ++iter) {

		cIter = minSublinks_2.begin();
		minSublinks_2.insert(cIter, iter->second.first);

		cIter = maxSublinks_2.begin();
		maxSublinks_2.insert(cIter, iter->second.second);

	}

	plt::named_plot(type_1 + "-less than 30 M", timing, minSublinks_1);
	plt::named_plot(type_2 + "-less than 30 M", timing, minSublinks_2);
	plt::named_plot(type_1 + "-more than 100 M", timing, maxSublinks_1);
	plt::named_plot(type_2 + "-more than 100 M", timing, maxSublinks_2);

	plt::title("Evaluation of Embeddable Bandwidth for Substrate Links");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Substrate Link(s)");

	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> sameVirNws_1;
	for (map<int, int>::iterator iter = currentSameVirNws_1.begin();
			iter != currentSameVirNws_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = sameVirNws_1.begin();
		sameVirNws_1.insert(cIter, iter->second);

	}
	vector<double> sameVirNws_2;
	for (map<int, int>::iterator iter = currentSameVirNws_2.begin();
			iter != currentSameVirNws_2.end(); ++iter) {
		cIter = sameVirNws_2.begin();
		sameVirNws_2.insert(cIter, iter->second);
	}

	plt::named_plot(type_1, timing, sameVirNws_1);
	plt::named_plot(type_2, timing, sameVirNws_2);

	plt::title("Evaluation of The Same Virtual Networks");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Virtual Network(s)");

	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> comVirNws_1;
	for (map<int, int>::iterator iter = currentComVirNws_1.begin();
			iter != currentComVirNws_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = comVirNws_1.begin();
		comVirNws_1.insert(cIter, iter->second);

	}
	vector<double> comVirNws_2;
	for (map<int, int>::iterator iter = currentComVirNws_2.begin();
			iter != currentComVirNws_2.end(); ++iter) {
		cIter = comVirNws_2.begin();
		comVirNws_2.insert(cIter, iter->second);
	}

	plt::named_plot(type_1, timing, comVirNws_1);
	plt::named_plot(type_2, timing, comVirNws_2);

	plt::title("Evaluation of Common Virtual Networks");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Virtual Network(s)");

	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> subLinkCost_1;
	for (map<int, double>::iterator iter = currentCostSubLinkRecords_1.begin();
			iter != currentCostSubLinkRecords_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = subLinkCost_1.begin();
		subLinkCost_1.insert(cIter, iter->second);

	}
	vector<double> subLinkCost_2;
	for (map<int, double>::iterator iter = currentCostSubLinkRecords_2.begin();
			iter != currentCostSubLinkRecords_2.end(); ++iter) {
		cIter = subLinkCost_2.begin();
		subLinkCost_2.insert(cIter, iter->second);
	}

	plt::named_plot(type_1, timing, subLinkCost_1);
	plt::named_plot(type_2, timing, subLinkCost_2);

	plt::title("Evaluation of Substrate Link Cost");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Cost(Megabits)");
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> failureEmbedding_1;
	for (map<int, int>::iterator iter = failureEmbeddingRecords_1.begin();
			iter != failureEmbeddingRecords_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, (iter->first));

		cIter = failureEmbedding_1.begin();
		failureEmbedding_1.insert(cIter, iter->second);
	}

	vector<double> failureEmbedding_2;
	for (map<int, int>::iterator iter = failureEmbeddingRecords_2.begin();
			iter != failureEmbeddingRecords_2.end(); ++iter) {
		cIter = failureEmbedding_2.begin();
		failureEmbedding_2.insert(cIter, iter->second);
	}

	plt::named_plot(type_1, timing, failureEmbedding_1);
	plt::named_plot(type_2, timing, failureEmbedding_2);
	//plt::ylim(0, 60);
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::title("Evaluation of Failure Embedded Virtual Network(s)");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Virtual Network(s)");
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> virNwRequest_1;
	for (map<int, int>::iterator iter = virNwRequestRecords_1.begin();
			iter != virNwRequestRecords_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, (iter->first));

		cIter = virNwRequest_1.begin();
		virNwRequest_1.insert(cIter, iter->second);
	}

	vector<double> virNwRequest_2;
	for (map<int, int>::iterator iter = virNwRequestRecords_2.begin();
			iter != virNwRequestRecords_2.end(); ++iter) {
		cIter = virNwRequest_2.begin();
		virNwRequest_2.insert(cIter, iter->second);
	}

	plt::named_plot(type_1, timing, virNwRequest_1);
	plt::named_plot(type_2, timing, virNwRequest_2);
	//plt::ylim(0, 60);
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::title("Evaluation of Virtual Network Requests");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Request(s)");
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> sameVirNwsVirNode_1;
	for (map<int, int>::iterator iter =
			currentSameVirNwsRevenueVirNodeRecords_1.begin();
			iter != currentSameVirNwsRevenueVirNodeRecords_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, (iter->first));

		cIter = sameVirNwsVirNode_1.begin();
		sameVirNwsVirNode_1.insert(cIter, iter->second);
	}

	vector<double> sameVirNwsVirNode_2;
	for (map<int, int>::iterator iter =
			currentSameVirNwsRevenueVirNodeRecords_2.begin();
			iter != currentSameVirNwsRevenueVirNodeRecords_2.end(); ++iter) {
		cIter = sameVirNwsVirNode_2.begin();
		sameVirNwsVirNode_2.insert(cIter, iter->second);
	}

	plt::named_plot(type_1, timing, sameVirNwsVirNode_1);
	plt::named_plot(type_2, timing, sameVirNwsVirNode_2);
	//plt::ylim(0, 60);
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::title("Evaluation of Same Virtual Network Embedded Virtual Node(s)");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Virtual Node(s)");
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> sameVirNwsCost_1;
	for (map<int, double>::iterator iter =
			currentSameVirNwsCostSubLinkRecords_1.begin();
			iter != currentSameVirNwsCostSubLinkRecords_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, (iter->first));

		cIter = sameVirNwsCost_1.begin();
		sameVirNwsCost_1.insert(cIter, iter->second);
	}

	vector<double> sameVirNwsCost_2;
	for (map<int, double>::iterator iter =
			currentSameVirNwsCostSubLinkRecords_2.begin();
			iter != currentSameVirNwsCostSubLinkRecords_2.end(); ++iter) {
		cIter = sameVirNwsCost_2.begin();
		sameVirNwsCost_2.insert(cIter, iter->second);
	}

	plt::named_plot(type_1, timing, sameVirNwsCost_1);
	plt::named_plot(type_2, timing, sameVirNwsCost_1);
	//plt::ylim(0, 60);
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::title("Evaluation of Same Virtual Network Substrate Cost");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Cost(s)");
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> sameVirNwEmbeddedLinks_1;
	for (map<int, pair<int, double>>::iterator iter =
			currentSameVirNwsRevenueVirLinkRecords_1.begin();
			iter != currentSameVirNwsRevenueVirLinkRecords_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = sameVirNwEmbeddedLinks_1.begin();
		sameVirNwEmbeddedLinks_1.insert(cIter, iter->second.first);

	}

	vector<double> sameVirNwEmbeddedLinks_2;
	for (map<int, pair<int, double>>::iterator iter =
			currentSameVirNwsRevenueVirLinkRecords_2.begin();
			iter != currentSameVirNwsRevenueVirLinkRecords_2.end(); ++iter) {

		cIter = sameVirNwEmbeddedLinks_2.begin();
		sameVirNwEmbeddedLinks_2.insert(cIter, iter->second.first);

	}

	plt::named_plot(type_1, timing, sameVirNwEmbeddedLinks_1);
	plt::named_plot(type_2, timing, sameVirNwEmbeddedLinks_2);

	plt::title("Evaluation of Embedded Virtual Link(s) Same Virtual Networks");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Virtual Link(s)");
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> sameVirNwsEmbeddedBandwidth_1;
	for (map<int, pair<int, double>>::iterator iter =
			currentSameVirNwsRevenueVirLinkRecords_1.begin();
			iter != currentSameVirNwsRevenueVirLinkRecords_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = sameVirNwsEmbeddedBandwidth_1.begin();
		sameVirNwsEmbeddedBandwidth_1.insert(cIter, iter->second.second);

	}
	vector<double> sameVirNwsEmbeddedBandwidth_2;
	for (map<int, pair<int, double>>::iterator iter =
			currentSameVirNwsRevenueVirLinkRecords_2.begin();
			iter != currentSameVirNwsRevenueVirLinkRecords_2.end(); ++iter) {
		cIter = sameVirNwsEmbeddedBandwidth_2.begin();
		sameVirNwsEmbeddedBandwidth_2.insert(cIter, iter->second.second);
	}

	plt::named_plot(type_1, timing, sameVirNwsEmbeddedBandwidth_1);
	plt::named_plot(type_2, timing, sameVirNwsEmbeddedBandwidth_2);

	plt::title(
			"Evaluation of Embedded Virtual Bandwidth for Same Virtual Networks");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Bandwidth(Mbps)");
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

	timing.clear();

	vector<double> subLinksResourceUtilization_1;
	for (map<int, double>::iterator iter =
			currentSubLinksResourceUtilization_1.begin();
			iter != currentSubLinksResourceUtilization_1.end(); ++iter) {
		cIter = timing.begin();
		timing.insert(cIter, iter->first);

		cIter = subLinksResourceUtilization_1.begin();
		subLinksResourceUtilization_1.insert(cIter, iter->second);

	}
	vector<double> subLinksResourceUtilization_2;
	for (map<int, double>::iterator iter =
			currentSubLinksResourceUtilization_2.begin();
			iter != currentSubLinksResourceUtilization_2.end(); ++iter) {
		cIter = subLinksResourceUtilization_2.begin();
		subLinksResourceUtilization_2.insert(cIter, iter->second);
	}

	plt::named_plot(type_1, timing, subLinksResourceUtilization_1);
	plt::named_plot(type_2, timing, subLinksResourceUtilization_2);

	plt::title("Evaluation of Substrate Links Resource utilization");
	plt::xlabel("Time Unit(s)");
	plt::ylabel("Utilization");
	plt::xlim(0, CommonConstants::VNE_ELAPSED_TIME_UNITS);
	plt::grid(true);
	plt::legend();
	plt::show();

}

void CommonFunctions::OutputRecordsIntoJsonFile(string fileName, string type,
		string description, multimap<int, string> congestionRecords,
		map<int, int> amountVirNwsRecords, map<int, int> currentNumberOfVns,
		map<int, pair<int, double>> currentRevenueVirLinkRecords,
		map<int, int> currentRevenueVirNodeRecords,
		map<int, double> dataSwitchingEnergy,
		map<int, double> transportedDataVolume,

		map<int, double> comDataSwitchingEnergy,
		map<int, double> comTransportedDataVolume,

		map<int, int> currentEndUserRequests,

		map<int, double> sameVirNwDataSwitchingEnergy,
		map<int, double> sameVirNwTransportedDataVolume,

		map<int, unsigned int> currentCommonEndUserReqs,
		map<int, int> currentEndingEndUserReqs,
		map<int, int> currentEndingVirNws,

		map<int, pair<int, int>> currentSubLinkResourceInfo,

		map<int, int> currentEmbeddableSubLinksInfo,

		map<int, int> currentSameVirNws, map<int, int> currentComVirNws,
		map<int, double> currentCostSubLinkRecords,

		map<int, int> failureEmbeddingRecords,

		map<int, int> virNwRequestRecords,
		map<int, pair<int, double>> currentSameVirNwsRevenueVirLinkRecords,
		map<int, int> currentSameVirNwsRevenueVirNodeRecords,
		map<int, double> currentSameVirNwsCostSubLinkRecords,

		map<int, double> currentSubLinksResourceUtilization

		) {

	StringBuffer strJson;
	Writer<StringBuffer> writer(strJson);

	writer.StartObject();          // Between StartObject()/EndObject(),

	writer.Key("Type");                // output a key,
	writer.String(type.c_str());             // follow by a value.

	writer.Key("Description");
	writer.String(description.c_str());

	writer.Key("CongestionRecords");
	writer.StartArray();

	for (int index = 0; index < CommonConstants::VNE_ELAPSED_TIME_UNITS;
			++index) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(index);

		writer.Key("Total");
		writer.Int(congestionRecords.count(index));

		writer.EndObject();

	}
	writer.EndArray();

	/*
	 * amount of substrate links whose available bandwidth is less than min
	 */
	writer.Key("CurrentSubLinkResourceMinInfo");
	writer.StartArray();

	for (map<int, pair<int, int>>::iterator iter =
			currentSubLinkResourceInfo.begin();
			iter != currentSubLinkResourceInfo.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second.first);

		writer.EndObject();
	}
	writer.EndArray();

	/*
	 * amount of substrate links whose available bandwidth is less than max
	 */
	writer.Key("CurrentSubLinkResourceMaxInfo");
	writer.StartArray();

	for (map<int, pair<int, int>>::iterator iter =
			currentSubLinkResourceInfo.begin();
			iter != currentSubLinkResourceInfo.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second.second);

		writer.EndObject();
	}
	writer.EndArray();

	/*
	 * amount of substrate links whose available bandwidth is less than max
	 */
	writer.Key("EmbeddableSubLinkResourceInfo");
	writer.StartArray();

	for (map<int, int>::iterator iter = currentEmbeddableSubLinksInfo.begin();
			iter != currentEmbeddableSubLinksInfo.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second);

		writer.EndObject();
	}
	writer.EndArray();

	writer.Key("SameVirNwDataSwitchingEnergy");
	writer.StartArray();

	for (map<int, double>::iterator iter = sameVirNwDataSwitchingEnergy.begin();
			iter != sameVirNwDataSwitchingEnergy.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Double(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("SameVirNwTransportedDataVolume");
	writer.StartArray();

	for (map<int, double>::iterator iter =
			sameVirNwTransportedDataVolume.begin();
			iter != sameVirNwTransportedDataVolume.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Double(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("CurrentCommonEndUserReqs");
	writer.StartArray();

	for (map<int, unsigned int>::iterator iter =
			currentCommonEndUserReqs.begin();
			iter != currentCommonEndUserReqs.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("CurrentEndingEndUserReqs");
	writer.StartArray();

	for (map<int, int>::iterator iter = currentEndingEndUserReqs.begin();
			iter != currentEndingEndUserReqs.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("CurrentEndingVirNws");
	writer.StartArray();

	for (map<int, int>::iterator iter = currentEndingVirNws.begin();
			iter != currentEndingVirNws.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second);

		writer.EndObject();
	}
	writer.EndArray();

	writer.Key("AmountVirNws");
	writer.StartArray();

	for (map<int, int>::iterator iter = amountVirNwsRecords.begin();
			iter != amountVirNwsRecords.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("AvailableVirNws");
	writer.StartArray();

	for (map<int, int>::iterator iter = currentNumberOfVns.begin();
			iter != currentNumberOfVns.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second);

		writer.EndObject();
	}
	writer.EndArray();

	writer.Key("DataSwichingEnergy");
	writer.StartArray();

	for (map<int, double>::iterator iter = dataSwitchingEnergy.begin();
			iter != dataSwitchingEnergy.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Double(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("ComDataSwichingEnergy");
	writer.StartArray();

	for (map<int, double>::iterator iter = comDataSwitchingEnergy.begin();
			iter != comDataSwitchingEnergy.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Double(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("EmbeddedLinks");
	writer.StartArray();

	for (map<int, pair<int, double>>::iterator iter =
			currentRevenueVirLinkRecords.begin();
			iter != currentRevenueVirLinkRecords.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second.first);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("EmbeddedNodes");
	writer.StartArray();

	for (map<int, int>::iterator iter = currentRevenueVirNodeRecords.begin();
			iter != currentRevenueVirNodeRecords.end(); ++iter) {

		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("EmbeddedBandwidth");
	writer.StartArray();

	for (map<int, pair<int, double>>::iterator iter =
			currentRevenueVirLinkRecords.begin();
			iter != currentRevenueVirLinkRecords.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Double(iter->second.second);

		writer.EndObject();
	}
	writer.EndArray();

	writer.Key("TransportedDataVolume");
	writer.StartArray();

	for (map<int, double>::iterator iter = transportedDataVolume.begin();
			iter != transportedDataVolume.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Double(iter->second);

		writer.EndObject();
	}
	writer.EndArray();

	writer.Key("ComTransportedDataVolume");
	writer.StartArray();

	for (map<int, double>::iterator iter = comTransportedDataVolume.begin();
			iter != comTransportedDataVolume.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Double(iter->second);

		writer.EndObject();
	}
	writer.EndArray();

	writer.Key("CurrentEndUserRequests");
	writer.StartArray();

	for (map<int, int>::iterator iter = currentEndUserRequests.begin();
			iter != currentEndUserRequests.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("CurrentSameVirNws");
	writer.StartArray();

	for (map<int, int>::iterator iter = currentSameVirNws.begin();
			iter != currentSameVirNws.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("CurrentComVirNws");
	writer.StartArray();

	for (map<int, int>::iterator iter = currentComVirNws.begin();
			iter != currentComVirNws.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("SublinkCost");
	writer.StartArray();

	for (map<int, double>::iterator iter = currentCostSubLinkRecords.begin();
			iter != currentCostSubLinkRecords.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Double(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("FailureEmbedding");
	writer.StartArray();

	for (map<int, int>::iterator iter = failureEmbeddingRecords.begin();
			iter != failureEmbeddingRecords.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("RequestEmbedding");
	writer.StartArray();

	for (map<int, int>::iterator iter = virNwRequestRecords.begin();
			iter != virNwRequestRecords.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("SameVirNwVNodes");
	writer.StartArray();

	for (map<int, int>::iterator iter =
			currentSameVirNwsRevenueVirNodeRecords.begin();
			iter != currentSameVirNwsRevenueVirNodeRecords.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("SameVirNwSubCost");
	writer.StartArray();

	for (map<int, double>::iterator iter =
			currentSameVirNwsCostSubLinkRecords.begin();
			iter != currentSameVirNwsCostSubLinkRecords.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Double(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("SameVirNwEmbeddedLinks");
	writer.StartArray();

	for (map<int, pair<int, double>>::iterator iter =
			currentSameVirNwsRevenueVirLinkRecords.begin();
			iter != currentSameVirNwsRevenueVirLinkRecords.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Int(iter->second.first);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("SameVirNwEmbeddedBandwidth");
	writer.StartArray();

	for (map<int, pair<int, double>>::iterator iter =
			currentSameVirNwsRevenueVirLinkRecords.begin();
			iter != currentSameVirNwsRevenueVirLinkRecords.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Double(iter->second.second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.Key("SublinkResourceUtilization");
	writer.StartArray();

	for (map<int, double>::iterator iter =
			currentSubLinksResourceUtilization.begin();
			iter != currentSubLinksResourceUtilization.end(); ++iter) {
		writer.StartObject();

		writer.Key("Timing");
		writer.Int(iter->first);

		writer.Key("Total");
		writer.Double(iter->second);

		writer.EndObject();

	}
	writer.EndArray();

	writer.EndObject();

	Document doc;
	doc.Parse(strJson.GetString());
	FILE* fp = fopen((fileName + "_recordsOutput.json").c_str(), "w");
	char writeBuffer[65536];
	FileWriteStream os(fp, writeBuffer, sizeof(writeBuffer));
	PrettyWriter<FileWriteStream> fileWriter(os);
	doc.Accept(fileWriter);
	fclose(fp);
}

string CommonFunctions::getNewCommonVirtuaNetworkID() {
	int virNo = ++CommonConstants::COMMON_VNW_ID;
	cout << " common no: " << CommonConstants::COMMON_VNW_ID << endl;
	cout << " no: " << virNo << endl;
	return CommonConstants::COMMON_VNW_ID_FLAG
			+ CommonFunctions::CoverIntegerToString(virNo);;

}
