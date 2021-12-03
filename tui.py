from util import screen_clear, results, ganttChart
from algorithms import Fcfs, Sjf, priorityAlgo, RR

class Tui:
	def __init__(self):
		print("""
Welcome User!
This Terminal application will calculate minimum waiting time,
respone time and turnaround time using one of the following Scheduling
Algorithms:
-First Come, First Served
-Shortest Job First
-Priority Scheduling
-Round-Robin Scheduling

Note: Write exti() anywhere to quit!

Press any key to resume""")
		input()
		screen_clear()

		while True:
			try:
				desiredAlgo = int(input("""
Please select one algorithm from the list:
1-First Come, First Served.
2-Shortest-Remaining-Time-First()
3-Priority Scheduling
4-Round-Robin, time quantum = 5
5-Exit

Note: all Algorthims are non-preemptive.
"""))		
				screen_clear()
				break
			except:
				print('Sorry, only numbers!')
				screen_clear()

		if desiredAlgo == 5:
			exit()

		while True:
			try:
				numOfProcesses = int(input("Please enter Number of processes: "))
				screen_clear()
				break
			except:
				print('Sorry, only numbers!')

		Processes = []		
		for x in range(numOfProcesses):
			Processes.append({'cpuburst': 0,
								  'priority': 0,
								  'waiting' : 0})

		print("Please Enter Processes information here:")
		processPointer = 0

		if desiredAlgo == 3:
			while True:
				try:
					cpuburst = int(input(f"Please Enter CPU burst of P{processPointer}:"))
					Processes[processPointer]["cpuburst"] = cpuburst
					processPointer +=1
				except:
					print('Sorry, only numbers!')

				if processPointer == numOfProcesses:
					break

			processPointer = 0	

			while True:
				try:
					priority = int(input(f"Please Enter priority of P{processPointer}:"))
					print("Please note that 0 is the highest priority.")
					Processes[processPointer]["priority"] = priority
					processPointer +=1
				except:
					print('Sorry, only numbers!')

				if processPointer == numOfProcesses:
					break

		else:
			while True:
				try:
					cpuburst = int(input(f"Please Enter CPU burst of P{processPointer}:"))
					Processes[processPointer]["cpuburst"] = cpuburst
					processPointer +=1
				except:
					print('Sorry, only numbers!')

				if processPointer == numOfProcesses:
					break

		screen_clear()

		if desiredAlgo == 1:
			result = Fcfs(Processes)
			results(result)
			print(ganttChart(result))
		elif desiredAlgo == 2:
			result = Sjf(Processes)
			results(result)
			print(ganttChart(result))
		elif desiredAlgo == 3:
			result = priorityAlgo(Processes)
			results(result)
			print(ganttChart(result))
		elif desiredAlgo == 4:
			result = RR(Processes)
			results(result)
			

