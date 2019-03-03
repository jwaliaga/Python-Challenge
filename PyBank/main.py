import os
import csv
import numpy as np

def getInfoCSVFile(Input):
# Read in the CSV file
    InputFileCSV = Input
    MyList = []
    with open(InputFileCSV, 'r') as csvfile:

        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')        
        csv_header = next(csvreader, None)        
        for row in csvreader:            
            MyList.append(row)

    return MyList

def TotalAmount(MyList,Col):
    y = [float(x[Col]) for x in MyList]
    return sum(y)

def AverageVal(MyList,Col):
    y = np.asarray([float(x[Col]) for x in MyList])
    z = y[range(1,len(y),1)]-y[range(0,len(y)-1,1)]
    return np.average(z)
    
def MaxVal(MyList,Col):
    y = np.asarray([float(x[Col]) for x in MyList])
    z = y[range(1,len(y),1)]-y[range(0,len(y)-1,1)]    
    index_max = ([i for i in range(0,len(z),1) if z[i]==max(z)])
    return max(z), MyList[index_max[0]+1][0]

def MinVal(MyList,Col):
    y = np.asarray([float(x[Col]) for x in MyList])
    z = y[range(1,len(y),1)]-y[range(0,len(y)-1,1)]
    index_min = ([i for i in range(0,len(z),1) if z[i]==min(z)])
    return min(z), MyList[index_min[0]+1][0]

InputFile = "budget_data.csv"
MyList = getInfoCSVFile(InputFile)
#print(MyList)

TotNumMonths =len(MyList)
TotPLChng = TotalAmount(MyList,1)
AvgPLChng = AverageVal(MyList,1)
MaxPLChng, DateMax = MaxVal(MyList,1)
MinPLChng, DateMin = MinVal(MyList,1)


#MaxPLChng = '${:,.0f}'.format(MaxPLChng)
#MinPLChng = '${:,.0f}'.format(MinPLChng)
#TotPLChng = '${:,.0f}'.format(TotPLChng)

MaxPLChng = '${:.0f}'.format(MaxPLChng)
MinPLChng = '${:.0f}'.format(MinPLChng)
TotPLChng = '${:.0f}'.format(TotPLChng)
AvgPLChng = '${:.2f}'.format(AvgPLChng)

print(f'Financial Analysis')
print(f'--------------------------------')
print(f'Total Months: {TotNumMonths}')
print(f'Total: {TotPLChng}')
print(f'Average Change: {AvgPLChng}')
print(f'Greatest Increase in Profits: {DateMax} ({MaxPLChng})')
print(f'Greatest Decrease in Profits: {DateMin} ({MinPLChng})')


file = open("Report-Budget.txt","w+") 


file.write('Financial Analysis\n')
file.write(f'--------------------------------\n')
file.write(f'Total Months: {TotNumMonths}\n')
file.write(f'Total: {TotPLChng}\n')
file.write(f'Average Change: {AvgPLChng}\n')
file.write(f'Greatest Increase in Profits: {DateMax} ({MaxPLChng})\n')
file.write(f'Greatest Decrease in Profits: {DateMin} ({MinPLChng})\n')

file.close() 

#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
