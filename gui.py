#!/usr/bin/python3

from tkinter import *
from tkinter import ttk


class Program:


    def __init__(self,master):
        master.option_add('*tearoff',False)
        master.title('Point System')
        self.menubar=Menu(master)
        master.config(menu = self.menubar)
        self.file=Menu(self.menubar)
        self.load=Menu(self.file)
        self.menubar.add_cascade(menu=self.file, label='File')
        self.file.add_command(label='Load',command=lambda:print('Load File Here'))
        self.file.add_command(label='Quit',command=lambda:exit())

        self.frame_header= ttk.Frame(master)
        self.frame_header.pack(expand=TRUE)
        ttk.Label(self.frame_header, text = 'Coming Soon', style = 'Header.TLabel').grid(row = 0, column = 1)
        self.dir_entry=ttk.Entry(self.frame_header,width=50)
        self.dir_entry.grid(row=0 ,column=3)
        self.load_button=ttk.Button(self.frame_header,text="Load File")
        self.load_button.grid(row=0,column=5)
        self.load_button=ttk.Button(self.frame_header,text="RUN")
        self.load_button.grid(row=0,column=6)
        
        ttk.Label(self.frame_header, text = 'Quarter Select', style = 'Header.TLabel').grid(row = 0, column = 2)


        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack(expand=TRUE,side=LEFT, anchor='w')
        self.treeview=ttk.Treeview(self.frame_content)
        self.treeview.grid(row=1,column=0)
        self.treeview.config(height=30)

        self.frame_main = ttk.Frame(master)
        self.frame_main.pack(expand=TRUE,side=LEFT,anchor='nw')
        
        ttk.Label(self.frame_main, text='Track').grid(row=0,column=0,padx=10)
        ttk.Label(self.frame_main, text='Academics').grid(row=0,column=1, padx=10)
        ttk.Label(self.frame_main, text='Cooperation').grid(row=0,column=2, padx=10)
        ttk.Label(self.frame_main, text='Work Habbits').grid(row=0,column=3,padx=10)
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



        #####Content
        
        def drawData(data_):
            try:
                self.grandTotal_.config(text='00')
                
                self.a1_label.config(text=data_['class']['1'][' ACAD'])
                self.a2_label.config(text=data_['class']['1']['COOP'])
                self.a3_label.config(text=data_['class']['1'][' W.H'])
                self.a4_label.config(text='Abs '+data_['class']['1']['ABS']+' Tar '+data_['class']['1']['TAR'])
                self.b1_label.config(text=data_['class']['2'][' ACAD'])
                self.b2_label.config(text=data_['class']['2']['COOP'])
                self.b3_label.config(text=data_['class']['2'][' W.H'])
                self.b4_label.config(text='Abs '+data_['class']['2']['ABS']+' Tar '+data_['class']['2']['TAR'])
                self.c1_label.config(text=data_['class']['3'][' ACAD'])
                self.c2_label.config(text=data_['class']['3']['COOP'])
                self.c3_label.config(text=data_['class']['3'][' W.H'])
                self.c4_label.config(text='Abs '+data_['class']['3']['ABS']+' Tar '+data_['class']['3']['TAR'])
                self.d1_label.config(text=data_['class']['4'][' ACAD'])
                self.d2_label.config(text=data_['class']['4']['COOP'])
                self.d3_label.config(text=data_['class']['4'][' W.H'])
                self.d4_label.config(text='Abs '+data_['class']['4']['ABS']+' Tar '+data_['class']['4']['TAR'])
                self.e1_label.config(text=data_['class']['5'][' ACAD'])
                self.e2_label.config(text=data_['class']['5']['COOP'])
                self.e3_label.config(text=data_['class']['5'][' W.H'])
                self.e4_label.config(text='Abs '+data_['class']['5']['ABS']+' Tar '+data_['class']['5']['TAR'])
                self.f1_label.config(text=data_['class']['6'][' ACAD'])
                self.f2_label.config(text=data_['class']['6']['COOP'])
                self.f3_label.config(text=data_['class']['6'][' W.H'])
                self.f4_label.config(text='Abs '+data_['class']['6']['ABS']+' Tar '+data_['class']['6']['TAR'])
                self.h1_label.config(text=data_['class']['H'][' ACAD'])
                self.h2_label.config(text=data_['class']['H']['COOP'])
                self.h3_label.config(text=data_['class']['H'][' W.H'])
                self.h4_label.config(text='Abs '+data_['class']['H']['ABS']+' Tar '+data_['class']['H']['TAR'])


                self.grandTotal_.config(text=data_['Tpts'])

            except:
                print('ok')
            
            
                #drawData(data={'Tpoints':'25'})



        



        
        #Left Menu
        self.treeview.insert('','0','item1',text='Advisory teacher')
        self.treeview.insert('item1','0','item2',text='Student')

        


def main():
    root = Tk()
    program = Program(root)
    root.mainloop()
    
if __name__ == "__main__": main()
