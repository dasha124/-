import datetime
from tkinter import *
import pymssql
from tkinter.ttk import Treeview
from tkinter.ttk import Combobox
import tkinter.messagebox as MessageBox


def report(root):

    connection = pymssql.connect(
        host='127.0.0.1',
        user='pass',
        password='1',
        database='AIS_2'
    )
    with connection.cursor() as cursor:
        def destroy():
            while len(obj) > 0:
                obj.pop().destroy()
        def back():
            destroy()
            from admin_orders import open_orders
            open_orders(root)

        select_all_rows = 'SELECT *FROM "Client"'
        cursor.execute(select_all_rows)
        people = cursor.fetchall()


        obj =[]
        # основная форма
        for c in range(9): root.columnconfigure(index=c, weight=1)
        r=0
        bck = Button(text="Назад", background="lightcyan", width=6, height=1, command=back)
        bck.grid(row=r, column=7, sticky='n', pady=1), obj.append(bck)
        label_f = Label(foreground='blue', text='Клиенты', anchor='w', font=('bold', 14), pady=5, padx=10)
        label_f.grid(row=r, column=0, sticky='w', columnspan=1, padx=5, pady=3), obj.append(label_f)

        def print_cl_rep(c):

            def bott_next(a):
                if (a+1) >= len(people):
                    MessageBox.showinfo(title='Ошибка!', message="Вы в конце списка клиентов!")
                else:
                    a+=1
                    while len(cl_mus)>0:
                        cl_mus.pop().destroy()
                    print_cl_rep(a)

            def bott_prev(a):
                if (a-1) < 0:
                    MessageBox.showinfo(title='Ошибка!', message="Вы в начале списка клиентов!")
                else:
                    a-=1
                    while len(cl_mus)>0:
                        cl_mus.pop().destroy()
                    print_cl_rep(a)

            cl_mus=[]
            r=2
            cl = Label(text='ФИО клиента', anchor='w', font=('bold', 12), foreground="gray", width=15)
            cl.grid(row=r, column=0, sticky='w', padx=2, pady=5), obj.append(cl)
            fio = Text(font=('bold', 11), width=45, height=1)
            fio.grid(row=r, column=1, sticky='w', padx=3, pady=1), obj.append(fio)
            fio.insert(0.0, people[c][1])
            r+=1
            ds = Label(text='Номер телефона', anchor='w', font=('bold', 11), foreground="gray", width=20)
            ds.grid(row=r, column=0, sticky='w', padx=2, pady=5), obj.append(ds)
            num = Text(font=('bold', 11), width=45, height=1)
            num.grid(row=r, column=1, sticky='w', padx=3, pady=1), obj.append(num)
            num.insert(0.0, people[c][2])
            r += 1
            df = Label(text='Адрес эл.почты', anchor='w', font=('bold', 11), foreground="gray", width=20)
            df.grid(row=r, column=0, sticky='w', padx=2, pady=5), obj.append(df)
            gm = Text(font=('bold', 11), width=45, height=1)
            gm.grid(row=r, column=1, sticky='w', padx=3, pady=1), obj.append(gm)
            gm.insert(0.0, people[c][3])
            r += 1
            btt_next = Button(text="След. запись", bg='lightcyan', command=lambda: bott_next(c))
            btt_next.grid(row=r, column=5), obj.append(btt_next)
            btt_prev = Button(text="Предыд. запись", bg='lightcyan', command=lambda: bott_prev(c))
            btt_prev.grid(row=1, column=5), obj.append(btt_prev)

        c=0
        print_cl_rep(c)
