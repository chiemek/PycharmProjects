from tkinter import *

def iCalc(source,side):
    storeObj= Frame(source, borderwidth=4, bd=4, bg="powerblue")
    storeObj.pack(side=side,expand=YES, fill=BOTH)
    return storeObj

def button(source, side, text, command= None):
    storeObj = button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*font','arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')

        display = StringVar()
        Entry(self, relief= RIDGE,
              textvariable=display, justify='right', bg='power blue', bd=30.).pack(side=TOP, expand=YES, fill=BOTH)

        for clearBut in ('[CE]','[C]'):
            erase = iCalc(self,TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar,
                       lambda storeObj=display, q= ichar: storeObj=set(''))

        for NumBut in ('789/','456*', '123-', '0.+'):
            functionNum = iCalc(self, TOP)
            for char in NumBut:
                button(functionNum,LEFT,char,
                       lambda storeObj= display, q=char: storeObj.set(storeObj.get() + q))
