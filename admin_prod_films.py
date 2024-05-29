from tkinter import *
import pymssql
from tkinter.ttk import Treeview
import tkinter.messagebox as MessageBox


def open_prod_flms(root, id):
    print("id =", id)
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
            from admin_prod import open_produc
            open_produc(root)

        def open_debtors():
            pass

        def change_av(flm):
            pass

        def change_genre(flm):
            pass

        def del_film(flm):
            pass

        select_films_f = 'SELECT *FROM "Film"'
        cursor.execute(select_films_f)
        films = cursor.fetchall()
        select_genres = 'SELECT *FROM "FilmGenre"'
        cursor.execute(select_genres)
        genres = cursor.fetchall()


        obj = []
        for c in range(8): root.columnconfigure(index=c, weight=1)

        r1 = 0
        mus_films = []
        # шапка
        bck = Button(text="Назад", background="lightcyan", width=6, height=1, command=back)
        bck.grid(row=0, column=7, sticky='n', pady=1), obj.append(bck)
        label_f = Label(foreground='blue', text='Фильмы', anchor='w', font=('bold', 14), pady=5, padx=10)
        label_f.grid(row=0, column=0, sticky='w', columnspan=1, padx=5), obj.append(label_f)
        fn = Label(foreground='gray', text='Название фильма', anchor='nw', font=('bold', 11), padx=50)
        fn.grid(row=1, column=0, sticky='nw', columnspan=1), obj.append(fn)
        av = Label(foreground='gray', text='Доступность', anchor='nw', font=('bold', 11), padx=5)
        av.grid(row=1, column=1, sticky='ne', columnspan=1), obj.append(av)
        y = Label(foreground='gray', text='Год', anchor='nw', font=('bold', 11), padx=20)
        y.grid(row=1, column=2, sticky='ne', columnspan=1), obj.append(y)
        с = Label(foreground='gray', text='Страна', anchor='nw', font=('bold', 11), padx=20)
        с.grid(row=1, column=3, sticky='nw', columnspan=1), obj.append(с)
        t = Label(foreground='gray', text='(мин)', anchor='nw', font=('bold', 11), padx=20)
        t.grid(row=1, column=4, sticky='ne', columnspan=1), obj.append(t)
        ag = Label(foreground='gray', text='Возраст+', anchor='nw', font=('bold', 11), padx=20)
        ag.grid(row=1, column=5, sticky='nw', columnspan=1), obj.append(ag)
        g = Label(foreground='gray', text='Жанр', anchor='nw', font=('bold', 11), padx=20)
        g.grid(row=1, column=6, sticky='ne', columnspan=1), obj.append(g)
        sl = Label(foreground='gray', text='Слоган', anchor='nw', font=('bold', 11), padx=20)
        sl.grid(row=3, column=0, sticky='nw', columnspan=1), obj.append(sl)

        def print_film(id_f, i, l, mus):
            r = 2
            c=0
            ii=i
            for i in range(len(films)):
                if films[i][0]==id_f:
                    c=i
                    break

            print("args ", mus)
            f = Text(font=('bold', 10), width=45, height=1, wrap='word')
            f.grid(row=r, column=0, sticky='w', padx=1, pady=2), obj.append(f)
            f.insert(0.0, films[c][1]), mus_films.append(f)

            if films[c][3] == True:
                b = 'green'
            else:
                b = 'red'

            av_btt = Button(text="", background=b, width=1, height=1, command=lambda: change_av(films[c]))
            av_btt.grid(row=r, column=1, sticky='n', padx=5, pady=1), obj.append(av_btt)
            yt = Text(font=('bold', 10), width=5, height=1)
            yt.grid(row=r, column=2, sticky='n', padx=5, pady=1), obj.append(yt)
            yt.insert(0.0, films[c][4])
            ct = Text(font=('bold', 10), width=15, height=1)
            ct.grid(row=r, column=3, sticky='n', padx=5, pady=1), obj.append(ct)
            ct.insert(0.0, films[c][6])
            tt = Text(font=('bold', 10), width=5, height=1)
            tt.grid(row=r, column=4, sticky='n', padx=5, pady=1), obj.append(tt)
            tt.insert(0.0, films[c][7])
            ag = Text(font=('bold', 10), width=5, height=1)
            ag.grid(row=r, column=5, sticky='n', padx=5, pady=1), obj.append(ag)
            ag.insert(0.0, films[c][8])

            slog = Text(font=('bold', 10), width=45, height=2, wrap='word')
            slog.grid(row=4, column=0, sticky='nw', padx=5, pady=1), obj.append(slog)
            slog.insert(0.0, films[c][9])

            for genre in genres:
                if isinstance(genre[1], str):
                    if genre[0] == films[c][2]:
                        b = 'green'
                    else:
                        b = 'lightgreen'
                    f1 = Button(width=13, height=1, text=genre[1], background=b, command=lambda: change_genre(films[c]))
                    f1.grid(row=r, column=6, sticky='n', padx=5, pady=1), obj.append(f1)
                    r += 1
            def bott_prev(a):
                print("1 a =", a)
                if (a - 1) < 0:
                    MessageBox.showinfo(title='Ошибка!', message="Вы в начале списка фильмов данного режиссера!")
                else:
                    a -= 1
                    #print("1 a =", a)
                    print("Вверх", mus[a], a, l, mus)
                    print_film(mus[a], a, l, mus)
            def bott_next(a):
                print("2 a =", a, "l =", l)
                if (a + 1) >=l:
                    MessageBox.showinfo(title='Ошибка!', message="Вы в конце списка фильмов данного режиссера!")
                else:
                    a += 1
                    #print("a =", a)
                    print_film(mus[a], a, l, mus)

            btt_prev = Button(text="Вверх", bg='blue', command=lambda: bott_prev(ii))
            btt_prev.grid(row=2, column=7), obj.append(btt_prev)
            btt_next = Button(text="Вниз", bg='blue', command=lambda: bott_next(ii))
            btt_next.grid(row=15, column=7), obj.append(btt_next)



        m_id_films=[]
        for film in films:
            if id==film[5]:
                print(film[0])
                m_id_films.append(film[0])

        print("mus-F =", m_id_films)
        if len(m_id_films)>0:
            i0=0
            print_film(m_id_films[i0], i0, len(m_id_films), m_id_films)
        else:
            back()

    root.mainloop()




