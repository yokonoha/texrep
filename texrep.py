################################
###テキリプ Python Recreation ###
###      by Y.Yokoha         ###
###       Beta Edition       ###
################################


import tkinter as tk
from tkinter import messagebox

def reptxt():
    orginal=textbox3.get("1.0",tk.END)
    grep=textbox1.get()
    rep=textbox2.get()
    new=orginal.replace(grep,rep)
    textbox4.insert(1.0,new)
    root.clipboard_append(new)
    messagebox.showinfo("処理完了","置換が完了し、結果をクリップボードへコピーしました!")

root=tk.Tk()
root.title("テキリプ")
root.geometry("740x480")
label1=tk.Label(root,text="テキリプ! -Text Replace by Y.Yokoha",font=("Helvetica",10))
label1.pack(pady=10)
label2=tk.Label(root,text="原文を貼り付け後、上の入力欄に置き換える対象となる文字、",font=("Helvetica",12))
label2.pack(pady=5)
label25=tk.Label(root,text="下の入力欄に置き換え後の文字を入力して下さい。",font=("Helvetica",12))
label25.pack()
label3=tk.Label(root,text="原文を入力またはCtl+Vで貼り付け↓",font=("Helvetica",14))
label3.pack(pady=10)
textbox3=tk.Text(root,width=50,height=6)
textbox3.pack(pady=5)  
textbox1=tk.Entry(root,width=40)
textbox1.pack(pady=5)
textbox1.insert(0,"置換前")
textbox2=tk.Entry(root,width=40)
textbox2.pack(pady=5)
textbox2.insert(0,"置換後")
button1=tk.Button(root,text="置き換えを開始",command=reptxt)
button1.pack(pady=15)
label4=tk.Label(root,text="結果表示↓",font=("Helvetica",16))
label4.pack(pady=10)
textbox4=tk.Text(root,width=50,height=6)
textbox4.pack(pady=5)
root.mainloop()




