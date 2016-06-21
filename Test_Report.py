import csv

def report():
	mylist = ["ID", "Test Condition", "Expected Result", "Actual Result", "Procedure", "Pass/Fail"]
	with open('Test_Case_d8.csv', 'wb') as csvfile:
		wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
		wr.writerow(mylist)

report()