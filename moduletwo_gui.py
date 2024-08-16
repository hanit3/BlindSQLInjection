import tkinter
from tkinter import *
import tkinter.messagebox
import tkinter.ttk
import moduletwo_shopping as f

tk = Tk()
tk.title('Blind SQL Injection 자동화 프로그램')
tk.geometry("620x360")

tableList = []
columnDict = {}
dataDict = {}
tempDict = {}

def exploit():
    cookie = entryCookie.get()
    if cookie == "":
        tkinter.messagebox.showwarning("경고", "세션 ID를 입력해주세요.")
        return False
    
    f.cookies["JSESSIONID"] = cookie
    print("exploit")
    
    tables = f.main()
    for t in tables:
        tablelistBox.insert(tkinter.END, t)
    tableList.append(tables)
    print(tableList)
            
    return 


def updateColumns(event):
    if not tablelistBox.curselection():
        return
    
    selected_indices = tablelistBox.curselection()
    if selected_indices[0] == 0:
        tablelistBox.selection_clear(0)
    
    try: 
        tableIndex = tablelistBox.curselection()[0]
        selectedTable = tablelistBox.get(tableIndex)
        columnlistBox.delete(1, tkinter.END)
        if selectedTable in columnDict.keys():
            columns = columnDict[selectedTable]
        else:    
            columns = f.mainColumn(selectedTable)      
            columnDict[selectedTable] = columns  
        for c in columns:
            columnlistBox.insert(tkinter.END, c)
        
        print(columns)
        datalistBox.delete(1, tkinter.END)
    except IndexError as e:
        print("인덱스를 선택함") 


def updateData(event):
    if not columnlistBox.curselection():
        return
    
    selected_indices = columnlistBox.curselection()
    if selected_indices[0] == 0:
        columnlistBox.selection_clear(0)
    
    try: 
        tableIndex = tablelistBox.curselection()[0]
        selectedTable = tablelistBox.get(tableIndex)
        columnIndex = columnlistBox.curselection()[0]
        selectedColumn = columnlistBox.get(columnIndex)
        
        datalistBox.delete(1, tkinter.END)
        
        if (selectedTable in dataDict.keys()) and (selectedColumn in dataDict[selectedTable].keys()):
            data = dataDict[selectedTable][selectedColumn]
        else:
            data = f.mainData(selectedTable, selectedColumn)      
            tempDict[selectedColumn] = data
            dataDict[selectedTable] = tempDict
        for d in data:
            datalistBox.insert(tkinter.END, d)
        print(data)
    except IndexError as e:
        print("인덱스를 선택함") 
    
def reset():
    print("전체 초기화")
    tablelistBox.delete(1, tkinter.END)
    columnlistBox.delete(1, tkinter.END)
    datalistBox.delete(1, tkinter.END)


def listboxView(x, w, name):
    listFrame = Frame(tk)
    listFrame.pack(fill="both", padx=5, pady=5)
    listFrame.place(x=x, y=80)  

    scrollbar = Scrollbar(listFrame)
    scrollbar.pack(side="right", fill="y")
    scrollbarx = Scrollbar(listFrame, orient='horizontal')
    scrollbarx.pack(side="bottom", fill="x")

    listFile = Listbox(listFrame, selectmode="extend", height=15, width=w, yscrollcommand=scrollbar.set, xscrollcommand=scrollbarx.set, exportselection=0)
    listFile.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=listFile.yview)
    scrollbarx.config(command=listFile.xview)
    
    fixed_item = name
    listFile.insert(END, fixed_item)
    listFile.itemconfig(0, {'bg': 'lightgray'})
    
    return listFile


labelCookie = Label(tk,text='세션 ID: ')
labelCookie.place(x=140, y=30)

entryCookie = Entry(tk, width="30")
entryCookie.place(x=190, y=30)

tablelistBox = listboxView(10, 20, "테이블")
tablelistBox.bind('<<ListboxSelect>>', updateColumns)

columnlistBox = listboxView(160, 20, "컬럼")
columnlistBox.bind('<<ListboxSelect>>', updateData)

datalistBox = listboxView(310, 40, "데이터")

exploitBtn = Button(tk,text='실행',bg='white',fg='black',command=exploit)
exploitBtn.place(x=420, y=27)
resetBtn = Button(tk,text='초기화',bg='white',fg='black',command=reset)
resetBtn.place(x=460, y=27)

tk.mainloop()