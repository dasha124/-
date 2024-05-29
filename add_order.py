from tkinter import *
import pymssql
from tkinter.ttk import Treeview
from tkinter.ttk import Combobox
import tkinter.messagebox as MessageBox
from reciept import print_rec
from tkcalendar import Calendar
from datetime import datetime

#from main import Tk

def add_order(root, c):
    # c - id клиента, на кого навешиваем новый заказ
    connection = pymssql.connect(
        host='127.0.0.1',
        user='pass',
        password='1',
        database='AIS_2'
    )

    with connection.cursor() as cursor:

        select_cl = 'SELECT *FROM "Client"'
        cursor.execute(select_cl)
        clients0 = cursor.fetchall()

        select_films = 'SELECT Film.ID_film, Film.film_name FROM "Film" WHERE Film.available=1'
        cursor.execute(select_films)
        films0 = cursor.fetchall()


        films =[]
        for film in films0:
            films.append(film[1])
        clients=[]
        for client in clients0:
            clients.append(client[1])
            # [id_cl, ds, df. (*dr), films]
        client=[] #данные по добавлению в бд по одному клиенту


        obj = []
        # шапка
        def destroy():
            while len(obj) > 0:
                obj.pop().destroy()

        def back():
            destroy()
            from admin_orders import open_orders
            open_orders(root)
        mus_films=[]

        client.append(c)
        def add_film(a, rw, client_m):

            def selected(event, cb):
                selection = combobox.get()
                cb.destroy()
                #print("sel =", selection)
                f1 = Text(font=('bold', 10), width=50, height=1)
                f1.grid(row=rw-1, column=0, sticky='w', padx=3, pady=2), obj.append(f1)
                f1.insert(0.0, selection)

                mus_films.append(selection)
               # print("mus_films[] =", mus_films)
                films.remove(selection)

            def save_ordr(clnt_m):
                print("UPDATE")
                for i in range(len(mus_films)):
                    #print("000")
                    for f in films0:
                        if f[1]==mus_films[i]:
                            client.append(f[0])
                            break

                connection = pymssql.connect(
                    host='127.0.0.1',
                    user='pass',
                    password='1',
                    database='AIS_2'
                )
                print(clnt_m)
                

                date_st = clnt_m[1][0:2] + '/' + clnt_m[1][3:5] + '/' + clnt_m[1][6:10]
                dt_st = datetime.strptime(date_st, '%d/%m/%Y').date()

                date_fin = clnt_m[2][0:2] + '/' + clnt_m[2][3:5] + '/' + clnt_m[2][6:10]
                dt_fin = datetime.strptime(date_fin, '%d/%m/%Y').date()

                if clnt_m[3]!='-':
                    date_ret = clnt_m[3][0:2] + '/' + clnt_m[3][3:5] + '/' + clnt_m[3][6:10]
                    dt_ret = datetime.strptime(date_ret, '%d/%m/%Y').date()
                else:
                    date_ret = '01/01/1900'
                    dt_ret = datetime.strptime(date_ret, '%d/%m/%Y').date()
                #print(date_st, type(date_st))
                #print(date_fin, type(date_fin))
                #print(date_ret, type(date_st))


                cur = connection.cursor()
                cur.execute("INSERT INTO Payment (ID_client, date_start, date_finish, date_return) VALUES (%s,%s,%s,%s)", \
                            (int(clnt_m[0]), dt_st, dt_fin, dt_ret))
                connection.commit()

                cur = connection.cursor()
                id_pa = 'SELECT TOP 1 ID_Payment FROM "Payment" order by ID_Payment DESC'
                cur.execute(id_pa)
                id_p= cur.fetchall()
                print("ID_Payment =", id_p[0], id_p[0][0])

                for i in range(4, len(clnt_m)):
                    for f in films0:
                        if clnt_m[i]==f[0]:
                            cur = connection.cursor()
                            cur.execute(
                                "INSERT INTO Booking (ID_Payment, ID_film) VALUES (%s,%s)", \
                                (id_p[0][0], f[0]))
                            connection.commit()

                            cur = connection.cursor()
                            cur.execute(
                                "INSERT INTO Booking (ID_Payment, ID_film) VALUES (%s,%s)", \
                                (id_p[0][0], f[0]))
                            connection.commit()

                            cur = connection.cursor()
                            cur.execute("UPDATE Film SET available=%s where ID_film=%s",
                                        (False, f[0]))
                            connection.commit()
                            break



                # ++  добавление фильмов по табл


                

            film_var = StringVar(value='')
            combobox = Combobox(textvariable=film_var, values=films, width=50)
            combobox.grid(row=rw, column=0, sticky='w', padx=3, pady=2), obj.append(combobox)
            combobox.bind("<<ComboboxSelected>>", lambda event, cb=combobox: selected(event, cb))

            #rw += 1

            btt_b = Button(text="Добавить фильм", bg='lightcyan', command=lambda: add_film(a, rw, client_m))
            btt_b.grid(row=rw, column=1, pady=2), obj.append(btt_b)

            #rw += 1
            btt3 = Button(text="Сохранить заказ", font=('italic', 10), height=1, width=15, bg='lightcyan', command=lambda: save_ordr(client_m))
            btt3.grid(row=rw, column=4, columnspan=2, pady=2), obj.append(btt3)

            rw+=1

        #---------------------------------------------------------------------------------------

        label_cl = Label(foreground='blue', text='Добавить заказ', anchor='nw', font=('bold', 14))
        label_cl.grid(row=0, column=0, sticky='ne', columnspan=1), obj.append(label_cl)
        btt_b = Button(text="Назад", bg='lightcyan', command=back)
        btt_b.grid(row=0, column=5), obj.append(btt_b)

        cl = Label(text='Клиент', anchor='w', font=('bold', 12), width=15)
        cl.grid(row=1, column=0, sticky='w', padx=10, pady=5, ipady=2, ipadx=2), obj.append(cl)
        fio = Text(font=('bold', 11), width=45, height=1)
        fio.grid(row=1, column=1, sticky='w', padx=10, pady=10), obj.append(fio)
        fio.insert(0.0, clients0[c-1][1])

        def ok1_ins():
            ds = e_ds.get()
            client.append(ds)
            MessageBox.showinfo(title='', message="Дата начала аренды успешно добавлена")

        def ok2_ins():
            df = e_df.get()
            client.append(df)
            MessageBox.showinfo(title='', message="Дата окончания аренды успешно добавлена")

        def ok3_ins():
            dr = e_dr.get()
            client.append(dr)
            MessageBox.showinfo(title='', message="Дата возрата заказа успешно добавлена")

        ds = Label(text='Дата начала аренды', anchor='w', font=('bold', 12), width=20)
        ds.grid(row=2, column=0, sticky='w', padx=10, pady=5, ipady=2, ipadx=2), obj.append(ds)
        e_ds = Entry()
        e_ds.grid(row=2, column=1), obj.append(e_ds)
        ok1 = Button(text='OK', font=('italic', 11), bg='white', command=ok1_ins)
        ok1.grid(row=2, column=2), obj.append(ok1)


        df = Label(text='Дата окончания аренды', anchor='w', font=('bold', 12), width=20)
        df.grid(row=3, column=0, sticky='w', padx=10, pady=5, ipady=2, ipadx=2), obj.append(df)
        e_df = Entry()
        e_df.grid(row=3, column=1), obj.append(e_df)
        ok2 = Button(text='OK', font=('italic', 11), bg='white', command=ok2_ins)
        ok2.grid(row=3, column=2), obj.append(ok2)

        dr = Label(text='Дата возврата', anchor='w', font=('bold', 12), width=20)
        dr.grid(row=4, column=0, sticky='w', padx=10, pady=5, ipady=2, ipadx=2), obj.append(dr)
        e_dr = Entry()
        e_dr.grid(row=4, column=1), obj.append(e_dr)
        ok3 = Button(text='OK', font=('italic', 11), bg='white', command=ok3_ins)
        ok3.grid(row=4, column=2), obj.append(ok3)

        fl = Label(text='Фильмы', anchor='nw', font=('bold', 14), foreground='blue')
        fl.grid(row=5, column=0, sticky='w', padx=10, pady=15, ipady=2, ipadx=2), obj.append(fl)

        r= 6
        btt_b = Button(text="Добавить фильм", bg='lightcyan', command=lambda :add_film(c, r, client))
        btt_b.grid(row=6, column=1), obj.append(btt_b)

        #connection.close()




        # c - id клиента, на кого навешиваем новый заказ



