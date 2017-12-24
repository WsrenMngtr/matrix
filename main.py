import tkinter as tk
from matrix import Matrix


def main():
    root = tk.Tk('matrix')
    root.grid()

    inputRow = tk.StringVar()
    inputBox = tk.Entry(root, textvariable=inputRow)
    inputBox.grid(row=0, column=0, columnspan=2)

    inputMatrix = tk.StringVar()
    rowList = tk.Listbox(root, selectmode=tk.MULTIPLE, listvariable=inputMatrix)
    rowList.grid(row=1, column=0, columnspan=2)

    outputList = tk.Listbox(root, selectmode=tk.MULTIPLE)
    outputList.grid(row=1, column=3, columnspan=2)

    def pushIntoList():
        rowList.insert(tk.END, inputRow.get())
        inputBox.delete(0, tk.END)
    inputButton = tk.Button(root, text='add', command=pushIntoList)
    inputButton.grid(row=0, column=2)

    def removeOutOfList():
        for index in rowList.curselection()[::-1]:
            rowList.delete(index)
    removeButton = tk.Button(root, text='remove', command=removeOutOfList)
    removeButton.grid(row=2, column=0)

    def clearList():
        rowList.delete(0, tk.END)
    clearButton = tk.Button(root, text='clear', command=clearList)
    clearButton.grid(row=2, column=1)

    nowMatrix = Matrix()
    
    def solveMatrix():
        nowMatrix.clear()
        matrix = (inputMatrix.get()[2:-2]).split("', '")
        for eachRow in matrix:
            row = eachRow.split()
            for index in range(len(row)):
                row[index] = int(row[index])
            nowMatrix.addRow(row)
        outputList.delete(0, tk.END)
        print(nowMatrix)
        nowMatrix.toRowSimplestMatrix()
        print(nowMatrix)
        for eachRow in nowMatrix:
            outputList.insert(tk.END, str(eachRow))
    solveButton = tk.Button(root, text='solve', command=solveMatrix)
    solveButton.grid(row=1, column=2)

    tk.mainloop()


main()
