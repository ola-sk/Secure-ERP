import tkinter as tk
root = tk.Tk()
root.geometry("240x240")

def getTextInput():
    result=textExample.get(1.0, tk.END+"-1c")
    print(result)

textExample=tk.Text(root, height=10)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="SEND", 
                    command=getTextInput)

btnRead.pack()

root.mainloop()