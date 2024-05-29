from tkinter import *
import pymssql
from tkinter.ttk import Treeview
import tkinter.messagebox as MessageBox
import datetime

global r
def open_clients(root):
    connection = pymssql.connect(
        host='127.0.0.1',
        user='pass',
        password='1',
        database='AIS_2'
    )

    # получение данных из бд
    with connection.cursor() as cursor:

        def destroy():
            while len(obj) > 0:
                obj.pop().destroy()
        def back():
            destroy()
            from forms import open_admin_form
            open_admin_form(root)

        def open_debtors():
            destroy()
            from debtors import debtors
            debtors(root)

        def open_report():
            destroy()
            from report import report
            report(root)
        def mess():
            MessageBox.showinfo(title='Внимание!', message="Подготовьте устройство для печати отчета!")







        select_all_rows = 'SELECT *FROM "Client"'
        cursor.execute(select_all_rows)
        people = cursor.fetchall()



        obj = []
        for c in range(10): root.columnconfigure(index=c, weight=1)

        dop_mus=[]
        def cl_search(a):
            for i in range(11, len(obj)):
                obj.pop().destroy()
            print("entered client =", a)
            r=3
            for clnt in people:
                if a in clnt[1]:

                    v_fio = StringVar(value=clnt[1])
                    fio = Entry(textvariable=v_fio, width=45)
                    fio.grid(row=r, column=0, sticky='w', padx=5), obj.append(fio)
                    dop_mus.append(fio)

                    v_num = StringVar(value=clnt[2])
                    num = Entry(textvariable=v_num, width=20)
                    num.grid(row=r, column=1, sticky='w', padx=2), obj.append(num)
                    dop_mus.append(num)

                    v_gm = StringVar(value=clnt[3])
                    gmail = Entry(textvariable=v_gm, width=45)
                    gmail.grid(row=r, column=2, sticky='w', padx=5), obj.append(gmail)
                    dop_mus.append(gmail)

                    change = Button(text='Изменить', font=('italic', 9), height=1, width=10, bg='lightgray', padx=2, \
                                    command=""
                                    )
                    #butt.append(change)
                    paym = Button(text='Перейти к заказу', font=('italic', 9), height=1, width=25, bg='lightgray',
                                  padx=2, command=''
                                  )
                    # butt.append(change)

                    change.grid(row=r, column=4, padx=2, pady=1, sticky='w'), obj.append(change)
                    paym.grid(row=r, column=5, padx=2, pady=1, sticky='w'), obj.append(paym)
                    r+=1

        def pr_all():
            while len(dop_mus)>0:
                dop_mus.pop().destroy()
            print_all(2)

        r = 0
        label_enter = Label(foreground='gray', font=('bold', 11), text='Введите имя клиента', anchor='nw')
        label_enter.grid(row=r, column=0), obj.append(label_enter)

        v = StringVar(value='*')
        cl_en = Entry(textvariable=v)
        cl_en.grid(row=r, column=1, sticky='w'), obj.append(cl_en)



        ok = Button(text='OK', font=('italic', 10), height=1, width=3, bg='lightgray', command=lambda: cl_search(cl_en.get()))
        ok.grid(row=r, column=2, pady=2, sticky='w'), obj.append(ok)

        ok1 = Button(text='Все клиенты', font=('italic', 10), height=1, width=10, bg='lightgray',
                    command=pr_all)
        ok1.grid(row=r, column=2, pady=2, sticky='e'), obj.append(ok1)

        orders = Button(text='Список должников', font=('italic', 10), height=2, width=22, bg='lightcyan', command=open_debtors)
        orders.grid(row=r, column=4, pady=2, padx=10, sticky='e'), obj.append(orders)

        report = Button(text='Отчет', font=('italic', 10), height=2, width=5, bg='lightcyan', command=open_report)
        report.grid(row=r, column=5, padx=2, pady=2, sticky='w'), obj.append(report)

        printt = Button(text='Печать', font=('italic', 10), height=2, width=14, bg='lightcyan', \
        command=mess)
        printt.grid(row=r, column=5, padx=2, pady=2, sticky='e'), obj.append(printt)

        save = Button(text='Сохранить', font=('italic', 10), height=2, width=16, bg='lightcyan', command='')
        save.grid(row=r, column=7, padx=2, pady=2), obj.append(save)

        btt_b = Button(text="Назад", font=('italic', 10), height=2, width=13, bg='lightcyan', command=back)
        btt_b.grid(row=r, column=8, padx=2, pady=2), obj.append(btt_b)
        r+=1

        cl = Label(text='ФИО клиента', anchor='w', foreground='gray', font=('bold', 10), width=20)
        cl.grid(row=r, column=0, sticky='w', padx=5, pady=5), obj.append(cl)

        n = Label(text='Номер телефона', anchor='w', foreground='gray', font=('bold', 10), width=20)
        n.grid(row=r, column=1, sticky='w', padx=2, pady=5), obj.append(n)

        gm = Label(text='Адрес эл.почты', anchor='w', foreground='gray', font=('bold', 10), width=20)
        gm.grid(row=r, column=2, sticky='w', padx=2, pady=5), obj.append(gm)
        print("len obj =", len(obj))


        def print_all(r):
            cur = connection.cursor()
            select = 'SELECT *FROM "Client"'
            cur.execute(select)
            peple = cur.fetchall()
            r+=1
            butt = []
            cl=[]
            ent=[]
            num_ent=[]
            gm_ent=[]
           # i1=0
            i=0
            for client in peple:

                def change_cl(i):
                    # i=id_cl
                    ent[i - 1].focus_set(); new_fio = ent[i-1].get()
                    num_ent[i-1].focus_set(); new_num = num_ent[i-1].get()
                    gm_ent[i-1].focus_set(); new_gm = gm_ent[i-1].get()
                    print("UPDATE", i, new_fio, new_num, new_gm)

                    cur = connection.cursor()
                    cur.execute("UPDATE Client SET FIO_client=%s, Phone_number=%s, Gmail=%s where ID_client=%s",
                                (new_fio, new_num, new_gm, i))
                    connection.commit()
                    MessageBox.showinfo(title='', message="Изменения успешно выполнены")

                    s = 'SELECT *FROM "Client"'
                    cur.execute(s)
                    p = cur.fetchall()
                    for pp in p:
                        print(pp)

                cl0=[]
                v_fio = StringVar(value=client[1])
                fio = Entry(textvariable=v_fio, width=45)
                ent.append(fio)
                #cl0.append(fio.get())
                cl0.append(client[1])
                ent[i].grid(row=r, column=0, sticky='w', padx=5), obj.append(ent[i])


                v_num = StringVar(value=client[2])
                num = Entry(textvariable=v_num, width=20)
                num_ent.append(num)
                #cl0.append(num.get())
                cl0.append(client[2])
                num_ent[i].grid(row=r, column=1, sticky='w', padx=2), obj.append(num_ent[i])

                v_gm = StringVar(value=client[3])
                gmail = Entry(textvariable=v_gm, width=45)
                gm_ent.append(gmail)
                #cl0.append(gmail.get())
                cl0.append(client[3])
                gm_ent[i].grid(row=r, column=2, sticky='w', padx=2), obj.append(gm_ent[i])

                cl.append(cl0)
                change = Button(text='Изменить', font=('italic', 9), height=1, width=10, bg='lightgray', padx=2, \
                                command=lambda m=client[0]: change_cl(m)
                                )
                butt.append(change)
                paym = Button(text='Перейти к заказу', font=('italic', 9), height=1, width=25, bg='lightgray', padx=2, \
                                command=''
                                )
                #butt.append(change)

                butt[i].grid(row=r, column=4, padx=2, pady=1, sticky='w'), obj.append(butt[i])
                paym.grid(row=r, column=5, padx=2, pady=1, sticky='w'), obj.append(paym)

                r+=1
                i+=1

            def add_cl(p1, p2, p3):
                p1.focus_set()
                new_fio1 = p1.get()
                p2.focus_set()
                new_num1 = p2.get()
                p3.focus_set()
                new_gm1 = p3.get()
                print("UPDATE", new_fio1, new_num1, new_gm1)

                cur = connection.cursor()
                cur.execute("INSERT INTO Client (FIO_client, Phone_number, Gmail) VALUES (%s,%s,%s)",
                            (new_fio1, new_num1, new_gm1))
                connection.commit()
                MessageBox.showinfo(title='', message="Изменения успешно выполнены")

                s = 'SELECT *FROM "Client"'
                cur.execute(s)
                p = cur.fetchall()
                for pp in p:
                    print(pp)
                print_all()


            def add_client(r):
                cl2=[]
                ent1 =[]
                i = 0
                add_fio = Entry(width=45)
                ent1.append(add_fio)
                ent1[i].grid(row=r, column=0, sticky='w', padx=5), obj.append(ent1[i])
                print("i m1", i)
                i+=1


                add_num = Entry(width=20)
                num_ent.append(num)
                ent1.append(add_num)
                ent1[i].grid(row=r, column=1, sticky='w', padx=2), obj.append(ent1[i])
                print("i m2", i)

                i+=1
                add_gmail = Entry(width=45)
                ent1.append(add_gmail)
                ent1[i].grid(row=r, column=2, sticky='w', padx=2), obj.append(ent1[i])
                


                cl.append(cl0)
                change = Button(text='Добавление', font=('italic', 9), height=1, width=10, bg='lightgray', padx=2, \
                                command=lambda m1=ent1[0], m2=ent1[1], m3=ent1[2]: add_cl(m1, m2, m3)
                                )
                change.grid(row=r, column=4, sticky='w', padx=2), obj.append(change)
                #butt.append(change)

            add = Button(text='Добавить клиента', font=('italic', 10), height=1, width=23, bg='lightcyan',
                         command=lambda :add_client(r))
            add.grid(row=r-1, column=7, padx=2, pady=1), obj.append(add)

        print_all(r)

