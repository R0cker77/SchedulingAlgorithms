from util import remove_items_from_list
import copy

def Fcfs(Processes):
	averagewait = 0
	for process in range(len(Processes)):
		Processes[process]['waiting'] = averagewait
		if process == len(Processes):
			pass
		else:
			averagewait += Processes[process]['cpuburst']

	return [Processes, (averagewait/len(Processes))]


def Sjf(Processes):
	finishedjobs = []
	averagewait = 0
	length = len(Processes)
	for index in range(len(Processes)):
		shortestjob = Processes[0]
		indexofshortestjob = 0
		for process in range(len(Processes)):

			if len(Processes) == 1:
				shortestjob = Processes[process]
				indexofshortestjob = process

			elif process == len(Processes):
				if Processes[process]["cpuburst"] < shortestjob["cpuburst"]:
					pass

			elif Processes[process]["cpuburst"] < shortestjob["cpuburst"]:
				shortestjob = Processes[process]
				indexofshortestjob = process

		Processes.pop(indexofshortestjob)

		finishedjobs.append({'cpuburst': shortestjob["cpuburst"],
							 'priority': 0,
							 'waiting' : averagewait})
		averagewait += shortestjob["cpuburst"]

	return [finishedjobs, averagewait/length] 

def priorityAlgo(Processes):
	finishedjobs = []
	averagewait = 0
	length = len(Processes)

	for index in range(len(Processes)):
		shortestjob = Processes[0]
		indexofshortestjob = 0

		for process in range(len(Processes)):

			if len(Processes) == 1:
				shortestjob = Processes[process]
				indexofshortestjob = process

			elif process == len(Processes):
				if Processes[process]["priority"] < shortestjob["priority"]:
					pass

			elif Processes[process]["priority"] < shortestjob["priority"]:
				shortestjob = Processes[process]
				indexofshortestjob = process

		Processes.pop(indexofshortestjob)


		finishedjobs.append({'cpuburst': shortestjob["cpuburst"],
							 'priority': shortestjob["priority"],
							 'waiting' : averagewait})
		averagewait += shortestjob["cpuburst"]

	return [finishedjobs, averagewait/length] 


def RR(Processes):
	averagewait = 0
	timequantum = 5
	length = len(Processes)
	finishedjobs = []
	unfinishedjobs = copy.deepcopy(Processes)

	while True:
		if not unfinishedjobs:
			break

		for index in range(len(unfinishedjobs)):

			beforesubtraction = copy.deepcopy(unfinishedjobs)

			unfinishedjobs[index]["cpuburst"] -= timequantum
			waitingtime = averagewait - Processes[index]["waiting"]
			Processes[index]["waiting"] = waitingtime

			if beforesubtraction[index]["cpuburst"] >= 5:
				averagewait += timequantum
			else:
				averagewait += beforesubtraction[index]["cpuburst"]

		undesiredindex = []

		for index in range(len(unfinishedjobs)):
			if unfinishedjobs[index]["cpuburst"] <= 0:
				undesiredindex.append(index)

		unfinishedjobs = remove_items_from_list(unfinishedjobs, undesiredindex)

	return [Processes, (averagewait/length)]
