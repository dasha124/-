from tkinter import *
import pymssql
from tkinter.ttk import Treeview


def open_genres(root):
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
            pass

        def ch_pr(gnr):
            pass

        def add_genre():
            pass

        select_genres = 'SELECT *FROM "FilmGenre"'
        cursor.execute(select_genres)
        g_p = cursor.fetchall()

        obj = []
        mus_genres = []
        for c in range(7): root.columnconfigure(index=c, weight=1)

        r = 0
        label_fg = Label(foreground='blue', text='Жанры', anchor='w', font=('bold', 14), pady=5, padx=10)
        label_fg.grid(row=0, column=0, sticky='w', columnspan=1), obj.append(label_fg)
        bck = Button(text="Назад", background="lightcyan", width=6, height=1, command=back)
        bck.grid(row=0, column=5, sticky='n', padx=5, pady=1), obj.append(bck)
        r+=1

        for genre in g_p:
            if isinstance(genre[1], str):
                g = Text(font=('bold', 11), width=25, height=1)
                g.grid(row=r, column=0, sticky='n', padx=1, pady=1), obj.append(g)
                g.insert(0.0, genre[1])
                mus_genres.append(g)
                p = Text(font=('bold', 11), width=5, height=1)
                p.grid(row=r, column=1, sticky='n', padx=1, pady=1), obj.append(p)
                p.insert(0.0, genre[2])
                mus_genres.append(g)
                ch_pr = Button(text="Изменить цену", background="lightgreen", width=15, height=1, command=lambda: ch_pr(genre))
                ch_pr.grid(row=r, column=2, sticky='nw', padx=1, pady=1), obj.append(ch_pr)
                r += 1
        add = Button(text="Добавить жанр", background="lightcyan", width=17, height=1, command=add_genre)
        add.grid(row=r-1, column=5, sticky='n', padx=5, pady=1), obj.append(add)

    root.mainloop()
