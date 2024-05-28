from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget('text')
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()

    if text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+ text)
        screen.update()

root=Tk()
root.geometry('900x400')
root.title('Digi Calculator')
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font='lucida 40 bold',border=20,bg='powder blue',justify='right')
screen.pack(fill=X,ipadx=20,padx=20,pady=20)

f= Frame(root,bg='grey',background='yellow',border=5)
b=Button(f,text='9',font='lucida 15 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)


b=Button(f,text='8',font='lucida 15 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)


b=Button(f,text='7',font='lucida 15 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root,bg='grey',background='yellow',border=5)

b=Button(f,text='6',font='lucida 15 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)


b=Button(f,text='5',font='lucida 15 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)


b=Button(f,text='4',font='lucida 15 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root,bg='grey',background='yellow',border=5)
b=Button(f,text='3',font='lucida 15 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text='2',font='lucida 15 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)


b=Button(f,text='1',font='lucida 15 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root,bg='grey',background='yellow',border=5,)

b=Button(f,text='0',font='lucida 16 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)


b=Button(f,text='-',font='lucida 16 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)


b=Button(f,text='*',font='lucida 15 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root,bg='grey',background='yellow',border=5)

b=Button(f,text='/',font='lucida 15 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)


b=Button(f,text='%',font='lucida 12 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)
f.pack()


b=Button(f,text='=',font='lucida 15 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)
f.pack()

f= Frame(root,bg='grey',background='yellow',border=5)

b=Button(f,text='c',font='lucida 15 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text='+',font='lucida 15 bold',padx=18,pady=14,background='red',foreground='black',border=5)
b.pack(side='left',padx=18,pady=8)
b.bind("<Button-1>",click)
f.pack()
root.mainloop()