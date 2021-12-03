import os

def screen_clear():
	if os.name == 'posix':
		_ = os.system('clear')

	else:
		_ = system('cls')

def remove_items_from_list(array, index):
	newArr = []
	for element in range(len(array)):
		if element not in index:
			newArr.append(array[element])

	return newArr
			

	

def results(results):
	print(f"""
|Name|CPU Burst|Priority|Waiting Time|
""")
	for result, index in zip(results[0], range(len(results[0]))):
		print(f"""
| {index}  |   {result['cpuburst']}    |    {result['priority']}   |     {result['waiting']}      |""")

	
	print(f"""Average Waiting time : {results[1]}ms""")

def ganttChart(results, algo=0):
	if algo == 3:
		pass
	else:
		print("Gantt Chart:")
		ghantchart = ""
		for element, index in zip(results[0], range(len(results[0]))):
			end = element["waiting"]
			if index == 0:
				ghantchart += f"[0]---Process {index}---"
			elif index == len(results[0]) - 1 :
				endburst = end + element["cpuburst"]
				ghantchart += f"[{end}]---Proces {index}---[{endburst}]"
			else:	
				ghantchart += f"[{end}]---Proces {index}---"

	return ghantchart
