#
# Point System for Torres High School
# Created by PBR
#
import csv


with open('srsqtr4raw.csv', encoding='utf-8-sig') as exampleFile:
    exampleReader = csv.reader(exampleFile)
  
    exampleData= list(exampleReader)
#print(exampleData[0])
#print(exampleData[1])
#print(exampleData[2])

data={}
#####Load Data###
#for i in range(1,1000,1):
for i in range(1,len(exampleData)-1):
    currentStudent=exampleData[i][7].split('\n')[0][9:]
    currentStudentId=exampleData[i][7].split('\n')[1][9:19]
    currentPeriod=exampleData[i][26]
    if currentStudent not in data:
        data[currentStudent]={'id':currentStudentId}
    if 'class' not in data[currentStudent]:
        data[currentStudent]['class']={currentPeriod:{}}
    if currentPeriod not in data[currentStudent]['class']:
        data[currentStudent]['class'][currentPeriod]={}
    if 'Tpts' not in data[currentStudent]:
        data[currentStudent]['Tpts']=0
    data[currentStudent]['class'][currentPeriod]['Class Name']=exampleData[i][27]
    data[currentStudent]['class'][currentPeriod]['Teacher Name']=exampleData[i][28]
    data[currentStudent]['class'][currentPeriod][exampleData[i][34]]=exampleData[i][35]
    data[currentStudent]['class'][currentPeriod]['ABS']=exampleData[i][30]
    data[currentStudent]['class'][currentPeriod]['TAR']=exampleData[i][31]
    data[currentStudent]['class'][currentPeriod]['pts']=0

##### Work with each student now
##### module 1 / QTR 1 #######
print('ready')
for currentStudent in data:
    print(currentStudent)
    data[currentStudent]['points']=0
    for j in range(1,7):
        if data[currentStudent]['class'][str(j)][' ACAD'] is 'M' or 'A' or 'B' or 'C':
            data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+3
        elif data[currentStudent]['class'][str(j)][' ACAD'] is 'D':
            data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+1
        if data[currentStudent]['class'][str(j)]['COOP'] is 'E' or 'S':
            data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+2
        wh =False;
        if data[currentStudent]['class'][str(j)]['ABS'] is '0' and int(data[currentStudent]['class'][str(j)]['TAR']) < 3:
            wh=True
            data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+2
        if wh is True:
            data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+2
       #HomeRoom Below.
    if data[currentStudent]['class']['H'][' ACAD'] is 'M' or 'A' or 'B' or 'C':
            data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+1.5
    elif data[currentStudent]['class']['H'][' ACAD'] is 'D':
            data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+0.5
    if data[currentStudent]['class']['H']['COOP'] is 'E' or 'S':
        data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+1
    wh =False;
    if data[currentStudent]['class']['H']['ABS'] is '0' and int(data[currentStudent]['class']['H']['TAR']) < 3:
        wh=True
        data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+1
    if wh is True:
        data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+1
        #Now Tally individual student totals.
    for j in range(1,7):
        data[currentStudent]['Tpts']=data[currentStudent]['Tpts']+data[currentStudent]['class'][str(j)]['pts']
    data[currentStudent]['Tpts']=data[currentStudent]['Tpts']+data[currentStudent]['class']['H']['pts']
            
