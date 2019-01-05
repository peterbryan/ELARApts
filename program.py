#
# Point System for Torres High School
# Created by PBR
#
import csv


with open('srsqtr2raw.csv', encoding='utf-8-sig') as exampleFile:
    exampleReader = csv.reader(exampleFile)
    exampleData= list(exampleReader)

#QTR1=0       #QTR3=2
#QTR2=1       #QTR4=3
qtr=0
data={}

########Variables
goodACAD=['M','A','B','C']
goodCOOP=['E','S']



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
    data[currentStudent]['class'][currentPeriod][exampleData[i][34]]=exampleData[i][35+qtr]
    data[currentStudent]['class'][currentPeriod]['ABS']=exampleData[i][30]
    data[currentStudent]['class'][currentPeriod]['TAR']=exampleData[i][31]
    data[currentStudent]['class'][currentPeriod]['pts']=0


print('ready')


def Module1():
    for currentStudent in data:
        print(currentStudent)
        data[currentStudent]['points']=0
        for j in range(1,7):
            try:
                if data[currentStudent]['class'][str(j)][' ACAD'] in goodACAD:
                    data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+3
                elif data[currentStudent]['class'][str(j)][' ACAD'] is 'D':
                    data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+1
                if data[currentStudent]['class'][str(j)]['COOP'] in goodCOOP:
                    data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+2
                wh =False;
                if data[currentStudent]['class'][str(j)]['ABS'] is '0' and int(data[currentStudent]['class'][str(j)]['TAR']) < 3:
                    wh=True
                    data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+2
                if wh is True:
                    data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+2
               #HomeRoom Below.
            except KeyError:
                print('Error with '+currentStudent+' could not find course: '+ str(j))
                continue
        try:    
            if data[currentStudent]['class']['H'][' ACAD'] in goodACAD:
                    data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+1.5
            elif data[currentStudent]['class']['H'][' ACAD'] is 'D':
                    data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+0.5
            if data[currentStudent]['class']['H']['COOP'] in goodCOOP:
                data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+1
            wh =False;
            if data[currentStudent]['class']['H']['ABS'] is '0' and int(data[currentStudent]['class']['H']['TAR']) < 3:
                wh=True
                data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+1
            if wh is True:
                data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+1
        except KeyError:
            print('Error with '+currentStudent+' could not find course: H or points to add')
            continue
            #Now Tally individual student totals.
        try:
            for j in range(1,7):
                data[currentStudent]['Tpts']=data[currentStudent]['Tpts']+data[currentStudent]['class'][str(j)]['pts']
            data[currentStudent]['Tpts']=data[currentStudent]['Tpts']+data[currentStudent]['class']['H']['pts']
        except KeyError:
            continue
    
######Module 2

def Module2():
    for currentStudent in data:
        print(currentStudent)
        data[currentStudent]['points']=0
        for j in range(1,7):
            try:
                if data[currentStudent]['class'][str(j)][' ACAD'] in goodACAD:
                    data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+3
                elif data[currentStudent]['class'][str(j)][' ACAD'] is 'D':
                    data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+1
                if data[currentStudent]['class'][str(j)]['COOP'] in goodCOOP:
                    data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+1
                if int(data[currentStudent]['class'][str(j)]['ABS']) < 3 and int(data[currentStudent]['class'][str(j)]['TAR']) < 2:
                    data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+3
                if ' TRAB' in data[currentStudent]['class'][str(j)].keys(): #########
                    if data[currentStudent]['class'][str(j)][' TRAB'] in goodCOOP:
                        data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+1
                elif data[currentStudent]['class'][str(j)][' W.H'] in goodCOOP:
                    data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+1
               #HomeRoom Below.
            except KeyError:
                print('Error with '+currentStudent+' could not find course: '+ str(j))
                continue
        try:    
            if data[currentStudent]['class']['H'][' ACAD'] in goodACAD:
                    data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+1.5
            elif data[currentStudent]['class']['H'][' ACAD'] is 'D':
                    data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+0.5
            if data[currentStudent]['class']['H']['COOP'] in goodCOOP:
                data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+0.5
            if int(data[currentStudent]['class']['H']['ABS']) < 3 and int(data[currentStudent]['class']['H']['TAR']) < 2:
                data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+1.5
            if ' TRAB' in data[currentStudent]['class']['H'].keys(): #########
                if data[currentStudent]['class']['H'][' TRAB'] in goodCOOP:
                    data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+0.5
            elif data[currentStudent]['class']['H'][' W.H'] in goodCOOP:
                    data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+0.5
        except KeyError:
            print('Error with '+currentStudent+' could not find course: H or points to add')
            continue
            #Now Tally individual student totals.
        try:
            for j in range(1,7):
                data[currentStudent]['Tpts']=data[currentStudent]['Tpts']+data[currentStudent]['class'][str(j)]['pts']
        except KeyError:
            continue
        try:
            data[currentStudent]['Tpts']=data[currentStudent]['Tpts']+data[currentStudent]['class']['H']['pts']
        except KeyError:
            continue

######Module 3 I have not changed anything for this one from 2.

def Module3():
    for currentStudent in data:
        print(currentStudent)
        data[currentStudent]['points']=0
        for j in range(1,7):
            try:
                if data[currentStudent]['class'][str(j)][' ACAD'] in goodACAD:
                    data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+3
                elif data[currentStudent]['class'][str(j)][' ACAD'] is 'D':
                    data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+1
                if data[currentStudent]['class'][str(j)]['COOP'] in goodCOOP:
                    data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+1
                if int(data[currentStudent]['class'][str(j)]['ABS']) < 4 and int(data[currentStudent]['class'][str(j)]['TAR']) < 3:
                    data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+3
                if ' TRAB' in data[currentStudent]['class'][str(j)].keys(): #########
                    if data[currentStudent]['class'][str(j)][' TRAB'] in goodCOOP:
                        data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+1
                elif data[currentStudent]['class'][str(j)][' W.H'] in goodCOOP:
                    data[currentStudent]['class'][str(j)]['pts']=data[currentStudent]['class'][str(j)]['pts']+1
               #HomeRoom Below.
            except KeyError:
                print('Error with '+currentStudent+' could not find course: '+ str(j))
                continue
        try:    
            if data[currentStudent]['class']['H'][' ACAD'] in goodACAD:
                    data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+1.5
            elif data[currentStudent]['class']['H'][' ACAD'] is 'D':
                    data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+0.5
            if data[currentStudent]['class']['H']['COOP'] in goodCOOP:
                data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+0.5
            if int(data[currentStudent]['class']['H']['ABS']) < 4 and int(data[currentStudent]['class']['H']['TAR']) < 3:
                data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+1.5
            if ' TRAB' in data[currentStudent]['class']['H'].keys(): #########
                if data[currentStudent]['class']['H'][' TRAB'] in goodCOOP:
                    data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+0.5
            elif data[currentStudent]['class']['H'][' W.H'] in goodCOOP:
                    data[currentStudent]['class']['H']['pts']=data[currentStudent]['class']['H']['pts']+0.5
        except KeyError:
            print('Error with '+currentStudent+' could not find course: H or points to add')
            continue
            #Now Tally individual student totals.
        try:
            for j in range(1,7):
                data[currentStudent]['Tpts']=data[currentStudent]['Tpts']+data[currentStudent]['class'][str(j)]['pts']
        except KeyError:
            continue
        try:
            data[currentStudent]['Tpts']=data[currentStudent]['Tpts']+data[currentStudent]['class']['H']['pts']
        except KeyError:
            continue

def WriteOut():
    outputFile=open('Output.csv','w',newline='')
    outputWriter=csv.writer(outputFile)
    outputWriter.writerow(['Student Name','Id','Advisory','Total Points'])
    for currentStudent in data:
        #print('about to write: ',currentStudent)
        try:
            outputWriter.writerow([currentStudent,data[currentStudent]['id'],data[currentStudent]['class']['H']['Teacher Name'],data[currentStudent]['Tpts'] ])
        except KeyError:
            continue
    outputFile.close()
