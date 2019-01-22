#!/usr/bin/python3
#By PBR
#For ELARA
#### version 0.86
#################

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import csv


class Program:


    def __init__(self,master):
        master.option_add('*tearoff',False)
        master.title('Point System')
        self.menubar=Menu(master)
        master.config(menu = self.menubar)
        self.file=Menu(self.menubar)
        self.load=Menu(self.file)
        self.menubar.add_cascade(menu=self.file, label='File')
        self.file.add_command(label='Load',command=lambda:selectFile())
        self.file.add_command(label='Quit',command=lambda:master.destroy())

        self.frame_header= ttk.Frame(master)
        self.frame_header.pack(expand=TRUE)
        ttk.Label(self.frame_header, text = 'Module', style = 'Header.TLabel').grid(row = 0, column = 1)
        #radio buttons
        self.module=StringVar()
        ttk.Radiobutton(self.frame_header,text='Version 1', variable=self.module, value='v1').grid(row=1,column=1)
        ttk.Radiobutton(self.frame_header,text='Version 2', variable=self.module, value='v2').grid(row=2,column=1)
        ttk.Radiobutton(self.frame_header,text='Version 3', variable=self.module, value='v3').grid(row=3,column=1)
        ttk.Radiobutton(self.frame_header,text='Version 4', variable=self.module, value='v4').grid(row=4,column=1)

        
        #
        self.qtr=StringVar()
        ttk.Radiobutton(self.frame_header,text='Quarter 1', variable=self.qtr, value='0').grid(row=1,column=2)
        ttk.Radiobutton(self.frame_header,text='Quarter 2', variable=self.qtr, value='1').grid(row=2,column=2)
        ttk.Radiobutton(self.frame_header,text='Quarter 3', variable=self.qtr, value='2').grid(row=3,column=2)
        ttk.Radiobutton(self.frame_header,text='Quarter 4', variable=self.qtr, value='3').grid(row=4,column=2)

        self.dir_entry=ttk.Entry(self.frame_header,width=50)
        self.dir_entry.grid(row=2 ,column=3)
        self.load_button=ttk.Button(self.frame_header,text="Load File",command=lambda:selectFile())
        self.load_button.grid(row=2,column=5)
        self.run_button=ttk.Button(self.frame_header,text="RUN", command=lambda:loadFile(),state='disabled')
        self.run_button.grid(row=2,column=6)
        self.run_button.state(['disabled'])
        self.export_button=ttk.Button(self.frame_header,text="Export", command=lambda:WriteOut(), state='disabled')
        self.export_button.grid(row=3,column=5,columnspan=2)
        #self.export_button.state(['disabled'])


        
        ttk.Label(self.frame_header, text = 'Quarter Select', style = 'Header.TLabel').grid(row = 0, column = 2)

        self.filename=''
        self.advisory_teachers=[]
        self.data={}
        self.goodACAD=['M','A','B','C']
        self.goodCOOP=['E','S']
        def selectFile():
            self.filename=filedialog.askopenfile()
            self.dir_entry.insert(0,self.filename.name)
            self.run_button.state(['!disabled'])
        def loadFile():
            with open(self.filename.name, encoding='utf-8-sig') as exampleFile:
                exampleReader = csv.reader(exampleFile)
                exampleData= list(exampleReader)
            #QTR1=0       #QTR3=2
            #QTR2=1       #QTR4=3
            qtr=0
            #data={}
            qtr=int(self.qtr.get())
            ########Variables


            #####Load Data###
            #for i in range(1,1000,1):
            for i in range(1,len(exampleData)-1):
                currentStudent=exampleData[i][7].split('\n')[0][9:]
                currentStudentId=exampleData[i][7].split('\n')[1][9:19]
                currentPeriod=exampleData[i][26]
                if currentStudent not in self.data:
                    self.data[currentStudent]={'id':currentStudentId}
                if 'class' not in self.data[currentStudent]:
                    self.data[currentStudent]['class']={currentPeriod:{}}
                if currentPeriod not in self.data[currentStudent]['class']:
                    self.data[currentStudent]['class'][currentPeriod]={}
                if 'Tpts' not in self.data[currentStudent]:
                    self.data[currentStudent]['Tpts']=0
                self.data[currentStudent]['class'][currentPeriod]['Class Name']=exampleData[i][27]
                self.data[currentStudent]['class'][currentPeriod]['Teacher Name']=exampleData[i][28]
                self.data[currentStudent]['class'][currentPeriod][exampleData[i][34]]=exampleData[i][35+qtr]
                self.data[currentStudent]['class'][currentPeriod]['ABS']=exampleData[i][30]
                self.data[currentStudent]['class'][currentPeriod]['TAR']=exampleData[i][31]
                self.data[currentStudent]['class'][currentPeriod]['pts']=0
                def advisoryScan():
                    for currentStudent in self.data:
                        try:
                            if self.data[currentStudent]['class']['H']['Teacher Name'] not in self.advisory_teachers:
                                self.advisory_teachers.append(self.data[currentStudent]['class']['H']['Teacher Name'])
                        except KeyError:
                            continue
            advisoryScan()
            leftMenu(self.data,self.advisory_teachers)
            print(self.module.get())
            if str(self.module.get()) == 'v1':
               Module1()
            elif str(self.module.get()) == 'v2':
                Module2()
            elif str(self.module.get()) == 'v3':
                Module3()
            elif str(self.module.get()) == 'v4':
                Module4()
            self.export_button.configure(state='normal')
            


        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack(expand=TRUE,side=LEFT, anchor='w')
        self.treeview=ttk.Treeview(self.frame_content)
        self.treeview.grid(row=1,column=0)
        self.treeview.config(height=30)

        self.frame_main = ttk.Frame(master)
        self.frame_main.pack(expand=TRUE,side=LEFT,anchor='nw')
        
        ttk.Label(self.frame_main, text='Track').grid(row=0,column=0,padx=10)
        ttk.Label(self.frame_main, text='Academics').grid(row=0,column=1, padx=10)
        ttk.Label(self.frame_main, text='Work Habbits').grid(row=0,column=2, padx=10)
        ttk.Label(self.frame_main, text='Cooperation').grid(row=0,column=3,padx=10)
        ttk.Label(self.frame_main, text='Attendance').grid(row=0,column=4, padx=10)

        #Needs border above, and to the right
        ttk.Label(self.frame_main, text='A').grid(row=1,column=0, rowspan=2,pady=20)
        ttk.Label(self.frame_main, text='B').grid(row=3,column=0,rowspan=2,pady=20)
        ttk.Label(self.frame_main, text='C').grid(row=5,column=0,rowspan=2,pady=20)
        ttk.Label(self.frame_main, text='D').grid(row=7,column=0,rowspan=2,pady=20)
        ttk.Label(self.frame_main, text='E').grid(row=9,column=0,rowspan=2,pady=20)
        ttk.Label(self.frame_main, text='F').grid(row=11,column=0,rowspan=2,pady=20)
        ttk.Label(self.frame_main, text='H').grid(row=13,column=0,rowspan=2,pady=20)
        #ttk.Label(self.frame_main, text='Total').grid(row=15,column=0,pady=20)
        ttk.Label(self.frame_main, text='Grand Total: ').grid(row=15,column=2,pady=20)

        ##boxes inside main window
        #A
        self.a1_entry=ttk.Entry(self.frame_main,width=5)
        self.a1_entry.grid(row=2,column=1)
        self.a1_label=ttk.Label(self.frame_main,text='VAR')
        self.a1_label.grid(row=1,column=1)

        self.a2_entry=ttk.Entry(self.frame_main,width=5)
        self.a2_entry.grid(row=2,column=2)
        self.a2_label=ttk.Label(self.frame_main,text='VAR')
        self.a2_label.grid(row=1,column=2)
        
        self.a3_entry=ttk.Entry(self.frame_main,width=5)
        self.a3_entry.grid(row=2,column=3)
        self.a3_label=ttk.Label(self.frame_main,text='VAR')
        self.a3_label.grid(row=1,column=3)

        self.a4_entry=ttk.Entry(self.frame_main,width=5)
        self.a4_entry.grid(row=2,column=4)
        self.a4_label=ttk.Label(self.frame_main,text='VAR')
        self.a4_label.grid(row=1,column=4)

        #B
        self.b1_entry=ttk.Entry(self.frame_main,width=5)
        self.b1_entry.grid(row=4,column=1)
        self.b1_label=ttk.Label(self.frame_main,text='VAR')
        self.b1_label.grid(row=3,column=1)

        self.b2_entry=ttk.Entry(self.frame_main,width=5)
        self.b2_entry.grid(row=4,column=2)
        self.b2_label=ttk.Label(self.frame_main,text='VAR')
        self.b2_label.grid(row=3,column=2)
        
        self.b3_entry=ttk.Entry(self.frame_main,width=5)
        self.b3_entry.grid(row=4,column=3)
        self.b3_label=ttk.Label(self.frame_main,text='VAR')
        self.b3_label.grid(row=3,column=3)

        self.b4_entry=ttk.Entry(self.frame_main,width=5)
        self.b4_entry.grid(row=4,column=4)
        self.b4_label=ttk.Label(self.frame_main,text='VAR')
        self.b4_label.grid(row=3,column=4)

         #C
        self.c1_entry=ttk.Entry(self.frame_main,width=5)
        self.c1_entry.grid(row=6,column=1)
        self.c1_label=ttk.Label(self.frame_main,text='VAR')
        self.c1_label.grid(row=5,column=1)

        self.c2_entry=ttk.Entry(self.frame_main,width=5)
        self.c2_entry.grid(row=6,column=2)
        self.c2_label=ttk.Label(self.frame_main,text='VAR')
        self.c2_label.grid(row=5,column=2)
        
        self.c3_entry=ttk.Entry(self.frame_main,width=5)
        self.c3_entry.grid(row=6,column=3)
        self.c3_label=ttk.Label(self.frame_main,text='VAR')
        self.c3_label.grid(row=5,column=3)

        self.c4_entry=ttk.Entry(self.frame_main,width=5)
        self.c4_entry.grid(row=6,column=4)
        self.c4_label=ttk.Label(self.frame_main,text='VAR')
        self.c4_label.grid(row=5,column=4)

        #D
        self.d1_entry=ttk.Entry(self.frame_main,width=5)
        self.d1_entry.grid(row=8,column=1)
        self.d1_label=ttk.Label(self.frame_main,text='VAR')
        self.d1_label.grid(row=7,column=1)

        self.d2_entry=ttk.Entry(self.frame_main,width=5)
        self.d2_entry.grid(row=8,column=2)
        self.d2_label=ttk.Label(self.frame_main,text='VAR')
        self.d2_label.grid(row=7,column=2)
        
        self.d3_entry=ttk.Entry(self.frame_main,width=5)
        self.d3_entry.grid(row=8,column=3)
        self.d3_label=ttk.Label(self.frame_main,text='VAR')
        self.d3_label.grid(row=7,column=3)

        self.d4_entry=ttk.Entry(self.frame_main,width=5)
        self.d4_entry.grid(row=8,column=4)
        self.d4_label=ttk.Label(self.frame_main,text='VAR')
        self.d4_label.grid(row=7,column=4)

        #E
        self.e1_entry=ttk.Entry(self.frame_main,width=5)
        self.e1_entry.grid(row=10,column=1)
        self.e1_label=ttk.Label(self.frame_main,text='VAR')
        self.e1_label.grid(row=9,column=1)

        self.e2_entry=ttk.Entry(self.frame_main,width=5)
        self.e2_entry.grid(row=10,column=2)
        self.e2_label=ttk.Label(self.frame_main,text='VAR')
        self.e2_label.grid(row=9,column=2)
        
        self.e3_entry=ttk.Entry(self.frame_main,width=5)
        self.e3_entry.grid(row=10,column=3)
        self.e3_label=ttk.Label(self.frame_main,text='VAR')
        self.e3_label.grid(row=9,column=3)

        self.e4_entry=ttk.Entry(self.frame_main,width=5)
        self.e4_entry.grid(row=10,column=4)
        self.e4_label=ttk.Label(self.frame_main,text='VAR')
        self.e4_label.grid(row=9,column=4)

        #F
        self.f1_entry=ttk.Entry(self.frame_main,width=5)
        self.f1_entry.grid(row=12,column=1)
        self.f1_label=ttk.Label(self.frame_main,text='VAR')
        self.f1_label.grid(row=11,column=1)

        self.f2_entry=ttk.Entry(self.frame_main,width=5)
        self.f2_entry.grid(row=12,column=2)
        self.f2_label=ttk.Label(self.frame_main,text='VAR')
        self.f2_label.grid(row=11,column=2)
        
        self.f3_entry=ttk.Entry(self.frame_main,width=5)
        self.f3_entry.grid(row=12,column=3)
        self.f3_label=ttk.Label(self.frame_main,text='VAR')
        self.f3_label.grid(row=11,column=3)

        self.f4_entry=ttk.Entry(self.frame_main,width=5)
        self.f4_entry.grid(row=12,column=4)
        self.f4_label=ttk.Label(self.frame_main,text='VAR')
        self.f4_label.grid(row=11,column=4)

        #H
        self.h1_entry=ttk.Entry(self.frame_main,width=5)
        self.h1_entry.grid(row=14,column=1)
        self.h1_label=ttk.Label(self.frame_main,text='VAR')
        self.h1_label.grid(row=13,column=1)

        self.h2_entry=ttk.Entry(self.frame_main,width=5)
        self.h2_entry.grid(row=14,column=2)
        self.h2_label=ttk.Label(self.frame_main,text='VAR')
        self.h2_label.grid(row=13,column=2)
        
        self.h3_entry=ttk.Entry(self.frame_main,width=5)
        self.h3_entry.grid(row=14,column=3)
        self.h3_label=ttk.Label(self.frame_main,text='VAR')
        self.h3_label.grid(row=13,column=3)

        self.h4_entry=ttk.Entry(self.frame_main,width=5)
        self.h4_entry.grid(row=14,column=4)
        self.h4_label=ttk.Label(self.frame_main,text='VAR')
        self.h4_label.grid(row=13,column=4)

        #GrandTotal
        self.grandTotal_=ttk.Label(self.frame_main,text='XX')
        self.grandTotal_.grid(row=15,column=3)



        #####Content ##Need to account for spanish parents. TRABJ
        
        def drawData(data_):
            print(data_)
            try:
                
                self.a1_label.config(text=data_['class']['1'][' ACAD'])
                self.a3_label.config(text=data_['class']['1']['COOP'])
                if ' TRAB' in data_['class']['1'].keys():
                    self.a2_label.config(text=data_['class']['1'][' TRAB'])
                else:
                    self.a2_label.config(text=data_['class']['1'][' W.H'])
                self.a4_label.config(text='Abs '+data_['class']['1']['ABS']+' Tar '+data_['class']['1']['TAR'])
                self.b1_label.config(text=data_['class']['2'][' ACAD'])
                self.b3_label.config(text=data_['class']['2']['COOP'])
                if ' TRAB' in data_['class']['2'].keys():
                    self.b2_label.config(text=data_['class']['2'][' TRAB'])
                else:
                    self.b2_label.config(text=data_['class']['2'][' W.H'])
                self.b4_label.config(text='Abs '+data_['class']['2']['ABS']+' Tar '+data_['class']['2']['TAR'])
                self.c1_label.config(text=data_['class']['3'][' ACAD'])
                self.c3_label.config(text=data_['class']['3']['COOP'])
                if ' TRAB' in data_['class']['3'].keys():
                    self.c2_label.config(text=data_['class']['3'][' TRAB'])
                else:
                    self.c2_label.config(text=data_['class']['3'][' W.H'])
                self.c4_label.config(text='Abs '+data_['class']['3']['ABS']+' Tar '+data_['class']['3']['TAR'])
                self.d1_label.config(text=data_['class']['4'][' ACAD'])
                self.d3_label.config(text=data_['class']['4']['COOP'])
                if ' TRAB' in data_['class']['4'].keys():
                     self.d2_label.config(text=data_['class']['4'][' TRAB'])
                else:
                    self.d2_label.config(text=data_['class']['4'][' W.H'])
                self.d4_label.config(text='Abs '+data_['class']['4']['ABS']+' Tar '+data_['class']['4']['TAR'])
                self.e1_label.config(text=data_['class']['5'][' ACAD'])
                self.e3_label.config(text=data_['class']['5']['COOP'])
                if ' TRAB' in data_['class']['5'].keys():
                    self.e2_label.config(text=data_['class']['5'][' TRAB'])
                else:
                    self.e2_label.config(text=data_['class']['5'][' W.H'])
                self.e4_label.config(text='Abs '+data_['class']['5']['ABS']+' Tar '+data_['class']['5']['TAR'])
                self.f1_label.config(text=data_['class']['6'][' ACAD'])
                self.f3_label.config(text=data_['class']['6']['COOP'])
                if ' TRAB' in data_['class']['6'].keys():
                    self.f2_label.config(text=data_['class']['6'][' TRAB'])
                else:
                    self.f2_label.config(text=data_['class']['6'][' W.H'])
                self.f4_label.config(text='Abs '+data_['class']['6']['ABS']+' Tar '+data_['class']['6']['TAR'])
                self.h1_label.config(text=data_['class']['H'][' ACAD'])
                self.h3_label.config(text=data_['class']['H']['COOP'])
                if ' TRAB' in data_['class']['H'].keys():
                    self.h2_label.config(text=data_['class']['H'][' TRAB'])
                else:
                    self.h2_label.config(text=data_['class']['H'][' W.H'])
                self.h4_label.config(text='Abs '+data_['class']['H']['ABS']+' Tar '+data_['class']['H']['TAR'])
                self.grandTotal_.config(text=data_['Tpts'])

            except:
                print('error drawing')
            
        def callback(event):
            print(self.treeview.selection()[0])
            try:
                drawData(self.data[self.treeview.selection()[0]])
            except KeyError:
                return
        
        #drawData(data={'Tpoints':'25'})
       

        



        
        #Left Menu
        #for tname in advisoryList
        def leftMenu(data,advisory_teachers):
            for teacher in advisory_teachers:
                self.treeview.insert('','0',teacher,text=teacher)
            for cStudent in data:
                try:
                    self.treeview.insert((data[cStudent]['class']['H']['Teacher Name']),'end',cStudent,text=cStudent)
                except KeyError:
                    continue
            self.treeview.bind('<<TreeviewSelect>>',callback)
            self.treeview.config(selectmode='browse')

        def Module1():
            for currentStudent in self.data:
                print(currentStudent)
                self.data[currentStudent]['points']=0
                for j in range(1,7):
                    try:
                        if self.data[currentStudent]['class'][str(j)][' ACAD'] in self.goodACAD:
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+3
                        elif self.data[currentStudent]['class'][str(j)][' ACAD'] is 'D':
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+1
                        if self.data[currentStudent]['class'][str(j)]['COOP'] in self.goodCOOP:
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+2
                        wh =False;
                        if self.data[currentStudent]['class'][str(j)]['ABS'] is '0' and int(self.data[currentStudent]['class'][str(j)]['TAR']) < 3:
                            wh=True
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+2
                        if wh is True:
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+2
                       #HomeRoom Below.
                    except KeyError:
                        print('Error with '+currentStudent+' could not find course: '+ str(j))
                        continue
                try:    
                    if self.data[currentStudent]['class']['H'][' ACAD'] in self.goodACAD:
                            self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+1.5
                    elif self.data[currentStudent]['class']['H'][' ACAD'] is 'D':
                            self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+0.5
                    if self.data[currentStudent]['class']['H']['COOP'] in self.goodCOOP:
                        self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+1
                    wh =False;
                    if self.data[currentStudent]['class']['H']['ABS'] is '0' and int(self.data[currentStudent]['class']['H']['TAR']) < 3:
                        wh=True
                        self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+1
                    if wh is True:
                        self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+1
                except KeyError:
                    print('Error with '+currentStudent+' could not find course: H or points to add')
                    continue
                    #Now Tally individual student totals.
                try:
                    for j in range(1,7):
                        self.data[currentStudent]['Tpts']=self.data[currentStudent]['Tpts']+self.data[currentStudent]['class'][str(j)]['pts']
                    self.data[currentStudent]['Tpts']=self.data[currentStudent]['Tpts']+self.data[currentStudent]['class']['H']['pts']
                except KeyError:
                    continue
        ######Module 2

        def Module2():
            for currentStudent in self.data:
                print(currentStudent)
                self.data[currentStudent]['points']=0
                for j in range(1,7):
                    try:
                        if self.data[currentStudent]['class'][str(j)][' ACAD'] in self.goodACAD:
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+3
                        elif self.data[currentStudent]['class'][str(j)][' ACAD'] is 'D':
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+1
                        if self.data[currentStudent]['class'][str(j)]['COOP'] in self.goodCOOP:
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+1
                        if int(self.data[currentStudent]['class'][str(j)]['ABS']) < 3 and int(self.data[currentStudent]['class'][str(j)]['TAR']) < 2:
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+3
                        if ' TRAB' in self.data[currentStudent]['class'][str(j)].keys(): #########
                            if self.data[currentStudent]['class'][str(j)][' TRAB'] in self.goodCOOP:
                                self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+1
                        elif self.data[currentStudent]['class'][str(j)][' W.H'] in self.goodCOOP:
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+1
                       #HomeRoom Below.
                    except KeyError:
                        print('Error with '+currentStudent+' could not find course: '+ str(j))
                        continue
                try:    
                    if self.data[currentStudent]['class']['H'][' ACAD'] in self.goodACAD:
                            self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+1.5
                    elif self.data[currentStudent]['class']['H'][' ACAD'] is 'D':
                            self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+0.5
                    if self.data[currentStudent]['class']['H']['COOP'] in self.goodCOOP:
                        self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+0.5
                    if int(self.data[currentStudent]['class']['H']['ABS']) < 3 and int(self.data[currentStudent]['class']['H']['TAR']) < 2:
                        self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+1.5
                    if ' TRAB' in self.data[currentStudent]['class']['H'].keys(): #########
                        if self.data[currentStudent]['class']['H'][' TRAB'] in self.goodCOOP:
                            self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+0.5
                    elif self.data[currentStudent]['class']['H'][' W.H'] in self.goodCOOP:
                            self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+0.5
                except KeyError:
                    print('Error with '+currentStudent+' could not find course: H or points to add')
                    continue
                    #Now Tally individual student totals.
                try:
                    for j in range(1,7):
                        self.data[currentStudent]['Tpts']=self.data[currentStudent]['Tpts']+self.data[currentStudent]['class'][str(j)]['pts']
                except KeyError:
                    continue
                try:
                    self.data[currentStudent]['Tpts']=self.data[currentStudent]['Tpts']+self.data[currentStudent]['class']['H']['pts']
                except KeyError:
                    continue

        ######Module 3 I have not changed anything for this one from 2.

        def Module3():
            for currentStudent in self.data:
                print(currentStudent)
                self.data[currentStudent]['points']=0
                for j in range(1,7):
                    try:
                        if self.data[currentStudent]['class'][str(j)][' ACAD'] in self.goodACAD:
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+3
                        elif self.data[currentStudent]['class'][str(j)][' ACAD'] is 'D':
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+1
                        if self.data[currentStudent]['class'][str(j)]['COOP'] in self.goodCOOP:
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+1
                        if int(self.data[currentStudent]['class'][str(j)]['ABS']) < 4 and int(self.data[currentStudent]['class'][str(j)]['TAR']) < 3:
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+3
                        if ' TRAB' in self.data[currentStudent]['class'][str(j)].keys(): #########
                            if self.data[currentStudent]['class'][str(j)][' TRAB'] in self.goodCOOP:
                                self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+1
                        elif self.data[currentStudent]['class'][str(j)][' W.H'] in self.goodCOOP:
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+1
                       #HomeRoom Below.
                    except KeyError:
                        print('Error with '+currentStudent+' could not find course: '+ str(j))
                        continue
                try:    
                    if self.data[currentStudent]['class']['H'][' ACAD'] in self.goodACAD:
                            self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+1.5
                    elif self.data[currentStudent]['class']['H'][' ACAD'] is 'D':
                            self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+0.5
                    if self.data[currentStudent]['class']['H']['COOP'] in self.goodCOOP:
                        self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+0.5
                    if int(self.data[currentStudent]['class']['H']['ABS']) < 4 and int(self.data[currentStudent]['class']['H']['TAR']) < 3:
                        self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+1.5
                    if ' TRAB' in self.data[currentStudent]['class']['H'].keys(): #########
                        if self.data[currentStudent]['class']['H'][' TRAB'] in self.goodCOOP:
                            self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+0.5
                    elif self.data[currentStudent]['class']['H'][' W.H'] in self.goodCOOP:
                            self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+0.5
                except KeyError:
                    print('Error with '+currentStudent+' could not find course: H or points to add')
                    continue
                    #Now Tally individual student totals.
                try:
                    for j in range(1,7):
                        self.data[currentStudent]['Tpts']=self.data[currentStudent]['Tpts']+self.data[currentStudent]['class'][str(j)]['pts']
                except KeyError:
                    continue
                try:
                    self.data[currentStudent]['Tpts']=self.data[currentStudent]['Tpts']+self.data[currentStudent]['class']['H']['pts']
                except KeyError:
                    continue

        ######Module 3 I have not changed anything for this one from 2.

        def Module4():
            for currentStudent in self.data:
                print(currentStudent)
                self.data[currentStudent]['points']=0
                for j in range(1,7):
                    try:
                        if self.data[currentStudent]['class'][str(j)][' ACAD'] in self.goodACAD:
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+3
                        elif self.data[currentStudent]['class'][str(j)][' ACAD'] is 'D':
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+1
                        if self.data[currentStudent]['class'][str(j)]['COOP'] in self.goodCOOP:
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+1
                        if int(self.data[currentStudent]['class'][str(j)]['ABS']) < 5 and int(self.data[currentStudent]['class'][str(j)]['TAR']) < 4:
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+3
                        if ' TRAB' in self.data[currentStudent]['class'][str(j)].keys(): #########
                            if self.data[currentStudent]['class'][str(j)][' TRAB'] in self.goodCOOP:
                                self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+1
                        elif self.data[currentStudent]['class'][str(j)][' W.H'] in self.goodCOOP:
                            self.data[currentStudent]['class'][str(j)]['pts']=self.data[currentStudent]['class'][str(j)]['pts']+1
                       #HomeRoom Below.
                    except KeyError:
                        print('Error with '+currentStudent+' could not find course: '+ str(j))
                        continue
                try:    
                    if self.data[currentStudent]['class']['H'][' ACAD'] in self.goodACAD:
                            self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+1.5
                    elif self.data[currentStudent]['class']['H'][' ACAD'] is 'D':
                            self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+0.5
                    if self.data[currentStudent]['class']['H']['COOP'] in self.goodCOOP:
                        self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+0.5
                    if int(self.data[currentStudent]['class']['H']['ABS']) < 5 and int(self.data[currentStudent]['class']['H']['TAR']) < 4:
                        self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+1.5
                    if ' TRAB' in self.data[currentStudent]['class']['H'].keys(): #########
                        if self.data[currentStudent]['class']['H'][' TRAB'] in self.goodCOOP:
                            self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+0.5
                    elif self.data[currentStudent]['class']['H'][' W.H'] in self.goodCOOP:
                            self.data[currentStudent]['class']['H']['pts']=self.data[currentStudent]['class']['H']['pts']+0.5
                except KeyError:
                    print('Error with '+currentStudent+' could not find course: H or points to add')
                    continue
                    #Now Tally individual student totals.
                try:
                    for j in range(1,7):
                        self.data[currentStudent]['Tpts']=self.data[currentStudent]['Tpts']+self.data[currentStudent]['class'][str(j)]['pts']
                except KeyError:
                    continue
                try:
                    self.data[currentStudent]['Tpts']=self.data[currentStudent]['Tpts']+self.data[currentStudent]['class']['H']['pts']
                except KeyError:
                    continue


        def WriteOut():
            outputFile=open('Output.csv','w',newline='')
            outputWriter=csv.writer(outputFile)
            outputWriter.writerow(['Student Name','Id','Advisory','Total Points'])
            for currentStudent in self.data:
                #print('about to write: ',currentStudent)
                try:
                    outputWriter.writerow([currentStudent,self.data[currentStudent]['id'],self.data[currentStudent]['class']['H']['Teacher Name'],self.data[currentStudent]['Tpts'] ])
                except KeyError:
                    continue
            outputFile.close()
            messagebox.showinfo("Export Complete","File Saved as Output.csv in this program's directory")
                


def main():
    root = Tk()
    program = Program(root)
    root.mainloop()
    
if __name__ == "__main__": main()
