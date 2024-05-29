import datetime
from tkinter import *
import pymssql
from tkinter.ttk import Treeview
from tkinter.ttk import Combobox
import tkinter.messagebox as MessageBox


def print_rec(root, i):
    # i = id_client


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


        select_cl_pay = 'SELECT c.ID_client, FIO_client, ID_Payment, ' \
                                 'date_start, date_finish, date_return FROM "Client" c ' \
                                 'inner join "Payment" p on p.ID_client=c.ID_client'
        cursor.execute(select_cl_pay)
        clients_pay = cursor.fetchall()
        for cl in clients_pay:
            print(cl)
        # ------------------------------------------------------------------
        select_book_film = 'SELECT b.ID_Payment, f.ID_film, f.ID_genre, f.film_name '\
                        'FROM "Film" f inner join "Booking" b '\
                        'on f.ID_film=b.ID_film'

        cursor.execute(select_book_film)
        book_film = cursor.fetchall()
        # ------------------------------------------------------------------
        select_f_fg = 'SELECT f.ID_film, fg.ID_genre, fg.genre, fg.price ' \
                'FROM "Film" f inner join "FilmGenre" fg '\
                'on f.ID_genre=fg.ID_genre'
        cursor.execute(select_f_fg)
        f_fg = cursor.fetchall()


        obj =[]
        # основная форма
        for c in range(9): root.columnconfigure(index=c, weight=1)

        label_cl = Label(foreground='blue', text='Расчет заказов', anchor='w', font=('bold', 13), width=20)
        label_cl.grid(row=0, column=0, sticky='w', pady=7, padx=2), obj.append(label_cl)
        bck = Button(text="Назад", background="lightcyan", width=6, height=1, command=back)
        bck.grid(row=0, column=7, sticky='n', pady=7), obj.append(bck)
        #шапка
        cl_n = Label(foreground='gray', text='Имя клиента', anchor='nw', font=('bold', 11), padx=5)
        cl_n.grid(row=1, column=0, sticky='nw'), obj.append(cl_n)
        ds = Label(foreground='gray', text='Начало аренды', anchor='w', width=17,  font=('bold', 10), padx=3)
        ds.grid(row=1, column=1, sticky='nw'), obj.append(ds)
        df = Label(foreground='gray', text='Окончание аренды', anchor='w',  width=20, font=('bold', 10), padx=3)
        df.grid(row=1, column=2, sticky='nw'), obj.append(df)
        dr = Label(foreground='gray', text='Дата возврата', anchor='nw', font=('bold', 10), padx=3, width=17)
        dr.grid(row=1, column=3, sticky='nw'), obj.append(dr)
        fn= Label(foreground='gray', text='Фильм', anchor='nw', font=('bold', 10), padx=5)
        fn.grid(row=1, column=4, sticky='nw', columnspan=1), obj.append(fn)
        fg = Label(foreground='gray', text='Жанр', anchor='nw', font=('bold', 10), padx=5)
        fg.grid(row=1, column=5, sticky='nw', columnspan=1), obj.append(fg)
        gp = Label(foreground='gray', text='Цена', anchor='nw', font=('bold', 10), padx=1)
        gp.grid(row=1, column=6, sticky='nw'), obj.append(gp)
        sp = Label(foreground='gray', text='Стоимость аренды фильма', anchor='e', font=('bold', 10), width=27)
        sp.grid(row=1, column=7, sticky='nw'), obj.append(sp)

        def print_paym(ip):
            pass

        #данные
        mus_pays=[]
        mus_cl = []

        r = 2
        for client in clients_pay:
            #r = 2
            #print("cl[0] =", client[0])
            print(client[1], mus_pays, client[0], i, "----------------------------------------------------------------")
            if client[0]==(i) and client[0] not in mus_cl:
                mus_cl.append(client[0])
                cl = Text(font=('bold', 10), width=17, height=3, wrap='word')
                cl.grid(row=r, column=0, sticky='nw', padx=5, pady=1), obj.append(cl)
                cl.insert(0.0, client[1])
                mus_cl.append(client[0])
                mus_pays.append(client[2])
                films0 = []
                for film in book_film:
                    if film[0] == client[2]:  # если id payment-а клиента в форме совпал с id payment-а клиента booking-е и в форме
                        films0.append([film[3], film[2]])
                print(films0)
                # даты 1 аренды
                r+=1
                date_st = Text(font=('bold', 10), width=14, height=1)
                date_st.grid(row=r, column=1, sticky='nw', padx=2, pady=2), obj.append(date_st)
                date_st.insert(0.0, client[3])
                date_f = Text(font=('bold', 10), width=14, height=1)
                date_f.grid(row=r, column=2, sticky='nw', padx=2, pady=2), obj.append(date_f)
                date_f.insert(0.0, client[4])
                date_r = Text(font=('bold', 10), width=14, height=1)
                date_r.grid(row=r, column=3, sticky='nw', padx=2, pady=2), obj.append(date_r)
                date_r.insert(0.0, client[5])
                r+=2
                # фильмы 1 аренды
                mus_films = []
                s = 0
                for i0 in range(len(films0)):
                    f = Text(font=('bold', 10), width=30, height=2, wrap='word')
                    f.grid(row=r, column=4, sticky='nw', padx=5, pady=2), obj.append(f)
                    f.insert(0.0, films0[i0][0])

                    pr = 0
                    for genr in f_fg:
                        if genr[1]==films0[i0][1]:
                            films0[i0][1]=genr[2]
                            pr = genr[3]
                    g = Text(font=('bold', 10), width=11, height=1)
                    g.grid(row=r, column=5, sticky='nw', padx=5, pady=1), obj.append(g)
                    g.insert(0.0, films0[i0][1])

                    p = Text(font=('bold', 10), width=3, height=1)
                    p.grid(row=r, column=6, sticky='nw', padx=3, pady=2), obj.append(p)
                    p.insert(0.0, pr)

                    dd = (int(str(client[5] - client[3]).split()[0]) + 1)*pr
                    ps0 = Text(font=('bold', 10), width=4, height=1)
                    ps0.grid(row=r, column=7, sticky='n', padx=3, pady=2), obj.append(ps0)
                    ps0.insert(0.0, dd)
                    s+=dd

                    mus_films.append(f)
                    r += 1
                p0 = Label(foreground='gray', text='Конечная стоимость заказа', anchor='nw', font=('bold', 10), padx=5, width=35)
                p0.grid(row=r, column=5, sticky='nw', columnspan=2), obj.append(p0)

                p = Text(font=('bold', 10), width=8, height=1)
                p.grid(row=r, column=7, sticky='n', padx=3, pady=1), obj.append(p)
                p.insert(0.0, s)
                r += 1
                #print("r0 =", r)
            elif client[0]==(i) and client[2] not in mus_pays:
                print("r1 =", r)
                mus_pays.append(client[2])
                films0 = []
                for film in book_film:
                    if film[0] == client[2]:  # если id payment-а клиента в форме совпал с id payment-а клиента booking-е и в форме
                        films0.append([film[3], film[2]])
                # даты 1 аренды
                date_st = Text(font=('bold', 10), width=14, height=1)
                date_st.grid(row=r, column=1, sticky='nw', padx=2, pady=2), obj.append(date_st)
                date_st.insert(0.0, client[3])
                date_f = Text(font=('bold', 10), width=14, height=1)
                date_f.grid(row=r, column=2, sticky='nw', padx=2, pady=2), obj.append(date_f)
                date_f.insert(0.0, client[4])
                date_r = Text(font=('bold', 10), width=14, height=1)
                date_r.grid(row=r, column=3, sticky='nw', padx=2, pady=2), obj.append(date_r)
                date_r.insert(0.0, client[5])
                r+=1
                # фильмы 1 аренды
                mus_films = []
                s=0
                for i0 in range(len(films0)):
                    f = Text(font=('bold', 10), width=30, height=2, wrap='word')
                    f.grid(row=r, column=4, sticky='nw', padx=5, pady=2), obj.append(f)
                    f.insert(0.0, films0[i0][0])

                    for genr in f_fg:
                        if genr[1] == films0[i0][1]:
                            films0[i0][1] = genr[2]
                    g = Text(font=('bold', 10), width=11, height=1)
                    g.grid(row=r, column=5, sticky='nw', padx=5, pady=1), obj.append(g)
                    g.insert(0.0, films0[i0][1])

                    p = Text(font=('bold', 10), width=3, height=1)
                    p.grid(row=r, column=6, sticky='nw', padx=3, pady=2), obj.append(p)
                    p.insert(0.0, pr)

                    dd = (int(str(client[5] - client[3]).split()[0]) + 1)*pr
                    ps0 = Text(font=('bold', 10), width=4, height=1)
                    ps0.grid(row=r, column=7, sticky='n', padx=3, pady=2), obj.append(ps0)
                    ps0.insert(0.0, dd)
                    s+=dd

                    mus_films.append(f)
                    r += 1
                p0 = Label(foreground='gray', text='Конечная стоимость заказа', anchor='nw', font=('bold', 10), padx=5)
                p0.grid(row=r, column=5, sticky='nw', columnspan=2), obj.append(p0)

                p = Text(font=('bold', 10), width=8, height=1)
                p.grid(row=r, column=7, sticky='n', padx=3, pady=1), obj.append(p)
                p.insert(0.0, s)
                r += 1
            print("----------------------------------------------------------------")

        ip=0
        print_paym(ip)

        root.mainloop()