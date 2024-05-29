from tkinter import *
import pymssql
from tkinter.ttk import Treeview
import tkinter.messagebox as MessageBox
import datetime

def debtors(root):

    connection = pymssql.connect(
        host='127.0.0.1',
        user='pass',
        password='1',
        database='AIS_2'
    )

    def destroy():
        while len(obj) > 0:
            obj.pop().destroy()

    def back():
        destroy()
        from admin_clients import open_clients
        open_clients(root)


    cur = connection.cursor()

    cur.execute('SELECT p.ID_payment, p.ID_client, date_start, date_finish, date_return, FIO_client FROM Payment p inner ' \
                'join Client c on p.ID_client=c.ID_client')
    payment_list = cur.fetchall()
    deb = []
    d_m = []
    for d in payment_list:
        print(d)
        dif = (d[4] - d[3]).days
        if dif > 3 and d[1] not in deb:
            deb.append(d[1])
            d_m.append(dif)
            print(deb)
    r=0
    obj = []
    for c in range(9): root.columnconfigure(index=c, weight=1)

    btt_b = Button(text="Назад", font=('italic', 10), height=1, width=13, bg='lightcyan', command=back)
    btt_b.grid(row=r, column=7, padx=2, pady=2), obj.append(btt_b)
    r+=1

    cl = Label(text='Клиент', anchor='w', font=('bold', 12), foreground="gray", width=15)
    cl.grid(row=r, column=0, sticky='w', padx=2, pady=5), obj.append(cl)

    ds = Label(text='Дата начала аренды', anchor='w', font=('bold', 11), foreground="gray", width=20)
    ds.grid(row=r, column=1, sticky='w', padx=2, pady=5), obj.append(ds)


    df = Label(text='Дата окончания аренды', anchor='w', font=('bold', 11),foreground="gray", width=20)
    df.grid(row=r, column=2, sticky='w', padx=2, pady=5), obj.append(df)

    dr = Label(text='Дата возврата', anchor='w', font=('bold', 11),foreground="gray", width=20)
    dr.grid(row=r, column=3, sticky='w', padx=2, pady=5), obj.append(dr)


    fl = Label(text='Просрочено дней', anchor='nw', font=('bold', 12), foreground="gray")
    fl.grid(row=r, column=4, sticky='w', padx=2, pady=5), obj.append(fl)


    r+=1
    #printed=[]
    for i in range(len(deb)):
        for d in payment_list:
            if deb[i] == d[1]:
                #printed.append(d[1])
                f1 = Text(font=('bold', 11), width=40, height=1)
                f1.grid(row=r, column=0, sticky='w', padx=3, pady=2), obj.append(f1)
                f1.insert(0.0, d[-1])

                f2 = Text(font=('bold', 11), width=20, height=1)
                f2.grid(row=r, column=1, sticky='w', padx=3, pady=2), obj.append(f2)
                t = d[2].strftime('%d/%m/%Y')
                f2.insert(0.0, t)

                f3 = Text(font=('bold', 11), width=25, height=1)
                f3.grid(row=r, column=2, sticky='w', padx=3, pady=2), obj.append(f3)
                t = d[3].strftime('%d/%m/%Y')
                f3.insert(0.0, t)

                f4 = Text(font=('bold', 11), height=1, width=20)
                f4.grid(row=r, column=3, sticky='w', padx=3, pady=2), obj.append(f4)
                t = d[4].strftime('%d/%m/%Y')
                f4.insert(0.0, t)

                f5 = Text(font=('bold', 11), width=22, height=1)
                f5.grid(row=r, column=4, sticky='w', padx=3, pady=2), obj.append(f5)
                f5.insert(0.0, d_m[i])
                r+=1



