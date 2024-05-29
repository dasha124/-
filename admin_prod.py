from tkinter import *
import pymssql
from tkinter.ttk import Treeview
import tkinter.messagebox as MessageBox



def open_produc(root):
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

        def open_prod_films(id_pr):
            destroy()
            from admin_prod_films import open_prod_flms
            open_prod_flms(root, id_pr)




        select_prod = 'SELECT *FROM "Producer"'
        cursor.execute(select_prod)
        producer = cursor.fetchall()

        obj = []
        mus_genres = []
        for c in range(7): root.columnconfigure(index=c, weight=1)

        r = 0
        label_fg = Label(foreground='blue', text="Режиссер", anchor='w', font=('bold', 14), pady=5, padx=10)
        label_fg.grid(row=0, column=0, sticky='w', columnspan=1), obj.append(label_fg)


        bck = Button(text="Назад", background="lightcyan", width=6, height=1, command=back)
        bck.grid(row=0, column=4, sticky='n', pady=1), obj.append(bck)

        def print_prod(c):
            def bott_next(a):
                if (a+1) >= len(producer):
                    MessageBox.showinfo(title='Ошибка!', message="Вы в начале списка режиссеров!")
                else:
                    a+=1
                    print_prod(a)

            def bott_prev(a):
                if (a-1) < 0:
                    MessageBox.showinfo(title='Ошибка!', message="Вы в конце списка режиссеров!")
                else:
                    a-=1
                    print_prod(a)

            prod_films = Button(text="Фильмы данного режиссера", background="lightgreen", width=25, height=1,
                                command=lambda: open_prod_films(producer[c][0]))
            prod_films.grid(row=1, column=2, sticky='w'), obj.append(prod_films)

            pr = Label(text='Имя режиссера', anchor='w', font=('bold', 12), width=17)
            pr.grid(row=1, column=0, sticky='w', padx=10, pady=5), obj.append(pr)
            fio = Text(font=('bold', 11), width=45, height=1)
            fio.grid(row=1, column=1, sticky='w', padx=10, pady=10), obj.append(fio)
            fio.insert(0.0, producer[c][1])

            osc = Label(text='Кол-во Оскаров', anchor='w', font=('bold', 12), width=20)
            osc.grid(row=2, column=0, sticky='w', padx=10, pady=5, ipady=2, ipadx=2), obj.append(osc)
            oscars = Text(font=('bold', 11), width=45, height=1)
            oscars.grid(row=2, column=1, sticky='w', padx=10, pady=10), obj.append(oscars)
            oscars.insert(0.0, producer[c][2])

            d_b = Label(text='Дата рождения', anchor='w', font=('bold', 12), width=20)
            d_b.grid(row=3, column=0, sticky='w', padx=10, pady=5, ipady=2, ipadx=2), obj.append(d_b)
            date_b = Text(font=('bold', 11), width=45, height=1)
            date_b.grid(row=3, column=1, sticky='w', padx=10, pady=10), obj.append(date_b)

            t = producer[c][3].strftime('%d/%m/%Y')
            date_b.insert(0.0, t)

            d_d = Label(text='Дата смерти', anchor='w', font=('bold', 12), width=20)
            d_d.grid(row=4, column=0, sticky='w', padx=10, pady=5, ipady=2, ipadx=2), obj.append(d_d)
            date_d = Text(font=('bold', 11), width=45, height=1)
            date_d.grid(row=4, column=1, sticky='w', padx=10, pady=10), obj.append(date_d)
            if str(producer[c][4])!='1900-01-01':
                date_d.insert(0.0, producer[c][4])
            else:
                date_d.insert(0.0, '')

            btt_prev = Button(text="Предыд. запись", bg='lightcyan', command=lambda: bott_prev(c))
            btt_prev.grid(row=5, column=2), obj.append(btt_prev)
            btt_next = Button(text="След. запись", width=15, bg='lightcyan', command=lambda: bott_next(c))
            btt_next.grid(row=5, column=3, padx=10), obj.append(btt_next)
            btt_del = Button(text="Удалить запись", width=17,  bg='lightcyan', command=lambda: bott_next(c))
            btt_del.grid(row=5, column=4, padx=10), obj.append(btt_del)


        c=0
        print_prod(c)





    root.mainloop()
