#Laura Davis
#1 May 2016
#This program will calculate the energy difference after of going green by 
#comparing energy bills from the year prior to making the switch and the year
#following the switch. It will aggregate two years' worth of data and 
#compute the savings. The data will be saved in file savings.txt and 
#data can be imported from that file.

#CGP145 Ch10 Lab-4 Going Green

def main():
	#declare variables
	endProgram = "no"
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	option = 0
	
	while endProgram == "no":
		print "1 - Load data to file"
		print "2 - Load data from file"
		option = input("Select your option --> ")
		
		#function calls
		if option == 1:
			notGreenCost = getNotGreen(months)
			goneGreenCost = getGoneGreen(months)
			savings = energySaved(notGreenCost, goneGreenCost)
			writeToFile(savings, notGreenCost, goneGreenCost)
			
		else:
			savings, notGreenCost, goneGreenCost = readFromfile()
			displayInfo(notGreenCost, goneGreenCost, savings, months)
			
		endProgram = raw_input('Do you want to end program? (Enter no or yes) --> ')

#the writeToFile function
def writeToFile(savings, notGreenCost, goneGreenCost):
	outFile = open('savings.txt', 'w')
	print >> outFile, 'Savings'
	counter = 0
	while counter < 12:
		outFile.write(str(savings[counter]) + '\n')
		outFile.write(str(notGreenCost[counter]) + '\n')
		outFile.write(str(goneGreenCost[counter]) + '\n')
		counter = counter + 1
	outFile.close()

#the readFromfile function
def readFromfile():
	notGreenCost = [0] * 12
	goneGreenCost = [0] * 12
	savings = [0] * 12
	inFile = open('savings.txt', 'r')
	str1 = inFile.readline()
	lstr = len(str1)
	str1 = str1[0:lstr-1]
	print str1
	counter = 0
	while counter < 12:
		str3 = inFile.readline()
		lstr = len(str3)
		savings[counter] = str3[0:lstr-1]
		str4 = inFile.readline()
		lstr = len(str4)
		notGreenCost[counter] = str4[0:lstr-1]
		str5 = inFile.readline()
		lstr = len(str5)
		goneGreenCost[counter] = str5[0:lstr-1]
		counter = counter + 1
	inFile.close()
	return savings, notGreenCost, goneGreenCost
	
#the getNotGreen function
def getNotGreen(months):
	notGreenCost = [0] * 12
	counter = 0
	while counter < 12:
		notGreenCost[counter] = input('Enter NOT GREEN energy costs for ' + months[counter] +' --> ')
		counter = counter + 1
	return notGreenCost
	
#the getGoneGreen function
def getGoneGreen(months):
	goneGreenCost = [0] * 12
	counter = 0
	while counter < 12:
		goneGreenCost[counter] = input('Enter GONE GREEN energy costs for ' + months[counter] +' --> ')
		counter = counter + 1
	return goneGreenCost

#the energySaved function
def energySaved(notGreenCost, goneGreenCost):
	savings = [0] * 12
	counter = 0
	while counter < 12:
		savings[counter] = notGreenCost[counter] - goneGreenCost[counter]
		counter = counter + 1
	return savings

#the displayInfo function		
def displayInfo(notGreenCost, goneGreenCost, savings, months):
	counter = 0
	while counter < 12:
		print "Information for " + months[counter]
		print "\t Savings \t\t$" + str(savings[counter])
		print "\t Not Green Costs \t$" + str(notGreenCost[counter])
		print "\t Gone Green Costs \t$" + str(goneGreenCost[counter])
		counter = counter + 1

#calls main
main()

