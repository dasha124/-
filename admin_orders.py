from tkinter import *
import pymssql
from tkinter.ttk import Treeview
from tkinter.ttk import Combobox
import tkinter.messagebox as MessageBox


import datetime

#from main import Tk

def open_orders(root):
    connection = pymssql.connect(
        host='127.0.0.1',
        user='pass',
        password='1',
        database='AIS_2'
    )

    with connection.cursor() as cursor:
        def get_fio():
            pass

        def open_debtors():
            pass


        select_clients_payment = 'SELECT c.ID_client, FIO_client, ID_Payment, ' \
                                 'date_start, date_finish, date_return FROM "Client" c ' \
                                 'inner join "Payment" p on p.ID_client=c.ID_client'
        cursor.execute(select_clients_payment)
        clients = cursor.fetchall()
        # ------------------------------------------------------------------
        select_paym = 'SELECT *FROM "Payment"'
        cursor.execute(select_paym)
        paym = cursor.fetchall()
        # ------------------------------------------------------------------
        select_book = 'SELECT *FROM "Booking"'
        cursor.execute(select_book)
        book = cursor.fetchall()
        # ------------------------------------------------------------------
        select_films_bp = 'SELECT p.ID_Payment, ID_film FROM "Payment" p inner join "Booking" b on p.ID_Payment=b.ID_Payment'
        cursor.execute(select_films_bp)
        films1 = cursor.fetchall()
        # ------------------------------------------------------------------
        select_films_f = 'SELECT ID_film, film_name FROM "Film"'
        cursor.execute(select_films_f)
        films0 = cursor.fetchall()
        c=1
        for row1 in clients:
            print(c, row1)
            c+=1
        print('# ------------------------------------------------------------------')
        #connection.close()

        #шапка
        def destroy():
            while len(obj) > 0:
                obj.pop().destroy()
        def back():
            destroy()
            from forms import open_admin_form
            open_admin_form(root)

        obj =[]
        v = StringVar(value='*')
        label_cl = Label( foreground='blue', text='Заказы', anchor='nw', font=('bold', 14))
        label_cl.grid(row=0, column=0, sticky='ne',  columnspan=1), obj.append(label_cl)
        btt_b = Button(text="Назад", bg='lightcyan', command=back)
        btt_b.grid(row=0, column=5), obj.append(btt_b)
        label_enter_cl = Label(foreground='gray', text='Поиск клиента (в разработке)', anchor='w', font=('bold', 10))
        label_enter_cl.grid(row=1, column=0, sticky='ne'), obj.append(label_enter_cl)
        e_pw1 = Entry(textvariable=v)
        e_pw1.grid(row=1, column=1, sticky='nw'), obj.append(e_pw1)

        label_enter_date = Label(foreground='gray', text='Поиск заказа по дате (в разработке)', anchor='w', font=('bold', 10))
        label_enter_date.grid(row=2, column=0, sticky='ne'), obj.append(label_enter_date)
        e_pw2 = Entry(textvariable=v)
        e_pw2.grid(row=2, column=1, sticky='nw'), obj.append(e_pw2)

        #основная форма
        for c in range(7): root.columnconfigure(index=c, weight=1)

        #перебор ID всех клиентов, для каждого вывести форму, по кнопке "далее" переходить к другому
        def print_cl(c):
            print("c =", c)
            def print_receipt(a):
                destroy()
                print("a =", a)
                from reciept import print_rec
                print_rec(root, a+1)


            def add_ordr(a):
                destroy()
                from add_order import add_order
                add_order(root, a+1)

            def del_ordr(clnt, i_p):

                #print("DELETE")
                for film in clnt:
                    cur = connection.cursor()
                    cur.execute(
                        "DELETE FROM Booking WHERE ID_payment=%s and ID_film=%s", (i_p, film)
                    )
                    connection.commit()

                cur = connection.cursor()
                cur.execute(
                    "DELETE FROM Payment WHERE ID_client=%s and date_start=%s and date_finish=%s and date_return=%s", \
                    (clients[c][0], clients[c][3], clients[c][4], clients[c][5]))
                connection.commit()
                #print("DELETE DONE")
                MessageBox.showinfo(title='Внимание!', message="Данный заказ удален!")



            def bott_next(a):
                if (a+1) >= len(clients):
                    MessageBox.showinfo(title='Ошибка!', message="Вы в начале списка заказов!")
                else:
                    a+=1
                    while len(mus_films)>0:
                        mus_films.pop().destroy()
                    print_cl(a)

            def bott_prev(a):
                if (a-1) < 0:
                    MessageBox.showinfo(title='Ошибка!', message="Вы в конце списка заказов!")
                else:
                    a-=1
                    while len(mus_films)>0:
                        mus_films.pop().destroy()
                    print_cl(a)

            client_mus = []
            cl = Label(text='Клиент', anchor='w', font=('bold', 12), width=15)
            cl.grid(row=4, column=0, sticky='w', padx=10, pady=5, ipady=2, ipadx=2), obj.append(cl)
            fio = Text(font=('bold', 11), width=45, height=1)
            fio.grid(row=4, column=1, sticky='w', padx=10, pady=10), obj.append(fio)
            fio.insert(0.0, clients[c][1])

            ds = Label(text='Дата начала аренды', anchor='w', font=('bold', 12), width=20)
            ds.grid(row=5, column=0, sticky='w', padx=10, pady=5, ipady=2, ipadx=2), obj.append(ds)
            date_st = Text(font=('bold', 11), width=45, height=1)
            date_st.grid(row=5, column=1, sticky='w', padx=10, pady=10), obj.append(date_st)
            t = clients[c][3].strftime('%d/%m/%Y')
            date_st.insert(0.0, t)

            df = Label(text='Дата окончания аренды', anchor='w', font=('bold', 12), width=20)
            df.grid(row=6, column=0, sticky='w', padx=10, pady=5, ipady=2, ipadx=2), obj.append(df)
            date_fin = Text(font=('bold', 11), width=45, height=1)
            date_fin.grid(row=6, column=1, sticky='w', padx=10, pady=10), obj.append(date_fin)
            t = clients[c][4].strftime('%d/%m/%Y')
            date_fin.insert(0.0, t)

            dr = Label(text='Дата возврата', anchor='w', font=('bold', 12), width=20)
            dr.grid(row=7, column=0, sticky='w', padx=10, pady=5, ipady=2, ipadx=2), obj.append(dr)
            date_ret = Text(font=('bold', 11), width=45, height=1)
            date_ret.grid(row=7, column=1, sticky='w', padx=10, pady=10), obj.append(date_ret)
            t = clients[c][5].strftime('%d/%m/%Y')
            date_ret.insert(0.0, t)

            fl = Label(text='Фильмы', anchor='nw', font=('bold', 14), foreground='blue')
            fl.grid(row=8, column=0, sticky='w', padx=10, pady=15, ipady=2, ipadx=2), obj.append(fl)

            id_payment=0
            films = []
            for client in clients:
                if client[0]==(c+1):  # если id клиента в форме совпал с id клиента в табл
                    for film in films1:
                        if film[0]==clients[c][2]:  # если id payment-а клиента в форме совпал с id payment-а клиента
                            # в  booking-е и в форме
                            id_payment=film[0]
                            for i in films0:  # 'SELECT ID_film, film_name FROM "Film"'
                                if film[1] == i[0] and i[1] not in films:
                                    films.append(i[1])
                                    client_mus.append(i[0])

            for i in range(len(films)):
                print(films[i])
            print("\n------------------------------------------------------------------\n")

            btt_next = Button(text="След. запись", bg='lightcyan', command=lambda: bott_next(c))
            btt_next.grid(row=7, column=5), obj.append(btt_next)
            btt_prev = Button(text="Предыд. запись", bg='lightcyan', command=lambda: bott_prev(c))
            btt_prev.grid(row=7, column=4), obj.append(btt_prev)

            btt4 = Button(text="Удалить заказ", font=('italic', 10), height=2, width=25, bg='lightcyan', command=lambda: del_ordr(client_mus, id_payment))
            btt4.grid(row=8, column=4, columnspan=2, pady=2), obj.append(btt4)

            btt2 = Button(text="Чек", font=('italic', 10), height=2, width=25, bg='lightcyan', command=lambda: print_receipt(c))
            btt2.grid(row=9, column=4, columnspan=2), obj.append(btt2)
            btt3 = Button(text="Добавить заказ", font=('italic', 10), height=2, width=25, bg='lightcyan', command=lambda: add_ordr(c))
            btt3.grid(row=10, column=4, columnspan=2, pady=2), obj.append(btt3)



            r = 9
            mus_films=[]
            for i in range(len(films)):
                f = Text(font=('bold', 11), width=45, height=1)
                f.grid(row=r, column=0, sticky='w', padx=10, pady=1), obj.append(f)
                f.insert(0.0, films[i])
                mus_films.append(f)
                r+=1


        c = 0
        print_cl(c)

    root.mainloop()





    

















