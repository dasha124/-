from tkinter import *
import pymssql
from tkinter.ttk import Treeview
import tkinter.messagebox as MessageBox


def open_films_u(root):
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
            from forms import open_user_form
            open_user_form(root)







        select_films_f = 'SELECT *FROM "Film"'
        cursor.execute(select_films_f)
        films = cursor.fetchall()
        select_genres = 'SELECT *FROM "FilmGenre"'
        cursor.execute(select_genres)
        genres = cursor.fetchall()

        def film_search(flm_name):

            def print_film_(id_f, i, l, mus):
                r = 2
                c = 0
                ii = i
                for i in range(len(films)):
                    if films[i][0] == id_f:
                        c = i
                        break

                print("args ", mus)
                f = Text(font=('bold', 10), width=45, height=1, wrap='word')
                f.grid(row=r, column=0, sticky='w', padx=1, pady=2), obj.append(f)
                f.insert(0.0, films[c][1]), mus_films.append(f)

                if films[c][3] == True:
                    b = 'green'
                else:
                    b = 'red'

                av_btt = Button(text="", background=b, width=1, height=1, command='')
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
                        f1 = Button(width=13, height=1, text=genre[1], background=b,
                                    command='')
                        f1.grid(row=r, column=6, sticky='n', padx=5, pady=1), obj.append(f1)
                        r += 1

                def bott_prev(a):
                    print("1 a =", a)
                    if (a - 1) < 0:
                        MessageBox.showinfo(title='Ошибка!', message="Вы в начале списка фильмов данного режиссера!")
                    else:
                        a -= 1
                        # print("1 a =", a)
                        print("Вверх", mus[a], a, l, mus)
                        print_film_(mus[a], a, l, mus)

                def bott_next(a):
                    print("2 a =", a, "l =", l)
                    if (a + 1) >= l:
                        MessageBox.showinfo(title='Ошибка!', message="Вы в конце списка фильмов данного режиссера!")
                    else:
                        a += 1
                        # print("a =", a)
                        print_film_(mus[a], a, l, mus)

                btt_prev = Button(text="Вверх", bg='blue', command=lambda: bott_prev(ii))
                btt_prev.grid(row=2, column=7), obj.append(btt_prev)
                btt_next = Button(text="Вниз", bg='blue', command=lambda: bott_next(ii))
                btt_next.grid(row=15, column=7), obj.append(btt_next)
# ------------------------------------------------------------------------------------------------------------
            for i in range(5, len(obj)):
                obj.pop().destroy()
            print("entered film =", flm_name)
            r =2
            m_id_films = []
            for film_ in films:
                if flm_name in film_[1]:
                    m_id_films.append(film_[0])
                    print(m_id_films)
            id_f = 0
            if len(m_id_films) > 0:
                print_film_(m_id_films[id_f], id_f, len(m_id_films), m_id_films)


        obj = []
        for c in range(9): root.columnconfigure(index=c, weight=1)

        r1 = 0
        mus_films = []
        #шапка
        bck = Button(text="Назад", background="lightcyan", width=6, height=1, command=back)
        bck.grid(row=0, column=6, sticky='n', pady=1), obj.append(bck)

        label_f = Label(foreground='blue', text='Фильмы', anchor='w', font=('bold', 14), pady=5, padx=10)
        label_f.grid(row=0, column=0, sticky='w', columnspan=1), obj.append(label_f)
        label_enter_cl = Label(foreground='gray', text='Поиск фильма', anchor='w', font=('bold', 10))
        label_enter_cl.grid(row=0, column=2, sticky='nw'), obj.append(label_enter_cl)
        v = StringVar(value='*')
        e_pw1 = Entry(textvariable=v)
        e_pw1.grid(row=0, column=2, sticky='n'), obj.append(e_pw1)
        bck1 = Button(text="Найти", background="lightcyan", width=6, height=1, command=lambda :film_search(e_pw1.get()))
        bck1.grid(row=0, column=2, sticky='ne'), obj.append(bck1)

#        len obj =4
        def print_genre(id_genre, mus_i_genre):

            def print_film(id, i, l, mus):
                def change_av(fil):
                    pass

                print("args ", id, i, l, mus)
                r = 4
                #c = id - 1
                #print("c =", c)
                f = Text(font=('bold', 10), width=45, height=1)
                f.grid(row=r, column=1, sticky='w', pady=7), obj.append(f)
                #print("check =", c, id, i, l, mus)
                #перебрать фильмы, чтобы id взять правильное у фильма
                c = 0
                for ii in range(len(films)):
                    if films[ii][0] == id:
                        c = ii
                        break
                f.insert(0.0, films[c][1]), mus_films.append(f)

                if films[c][3] == True:
                    b = 'green'
                else:
                    b = 'red'

                av_btt = Button(text="", background=b, width=1, height=1, command=lambda: change_av(films[c]))
                av_btt.grid(row=r, column=2, sticky='nw', padx=5, pady=1), obj.append(av_btt), mus_films.append(av_btt)
                r+=1
                yt = Text(font=('bold', 10), width=5, height=1)
                yt.grid(row=r, column=2, sticky='nw', padx=5, pady=1), obj.append(yt), mus_films.append(yt)
                yt.insert(0.0, films[c][4])
                r += 1
                ct = Text(font=('bold', 10), width=15, height=1)
                ct.grid(row=r, column=2, sticky='nw', padx=5, pady=1), obj.append(ct), mus_films.append(ct)
                ct.insert(0.0, films[c][6])
                r += 1
                tt = Text(font=('bold', 10), width=5, height=1)
                tt.grid(row=r, column=2, sticky='nw', padx=5, pady=1), obj.append(tt), mus_films.append(tt)
                tt.insert(0.0, films[c][7])
                r += 1
                ag = Text(font=('bold', 10), width=5, height=1)
                ag.grid(row=r, column=2, sticky='nw', padx=5, pady=1), obj.append(ag), mus_films.append(ag)
                ag.insert(0.0, films[c][8])
                r += 1
                slog = Text(font=('bold', 10), width=49, height=3)
                slog.grid(row=r, column=2, sticky='nw', padx=5, pady=1), obj.append(slog), mus_films.append(slog)
                slog.insert(0.0, films[c][9])


                def bott_prev(a):
                    print("1 a =", a)
                    if (a - 1) < 0:
                        MessageBox.showinfo(title='Ошибка!', message="Вы в начале списка фильмов данного жанра!")
                    else:
                        a -= 1
                        print("1 a =", a)
                        print(mus)
                        print_film(mus[a], a, l, mus)

                def bott_next(a):
                    # print("2 a =", a)
                    if (a + 1) >= l:
                        MessageBox.showinfo(title='Ошибка!', message="Вы в конце списка фильмов данного жанра!")
                    else:
                        a += 1
                        print("a =", a)
                        print_film(mus[a], a, l, mus)

                btt_prev = Button(text="Вверх", bg='blue', command=lambda: bott_prev(i))
                btt_prev.grid(row=4, column=7), obj.append(btt_prev), mus_films.append(btt_prev)
                btt_next = Button(text="Вниз", bg='blue', command=lambda: bott_next(i))
                btt_next.grid(row=9, column=7, sticky='s'), obj.append(btt_next), mus_films.append(btt_next)

            r = 2
            genre_n = Label(foreground='gray', text='Жанр фильма', anchor='w', font=('bold', 11), padx=50)
            genre_n.grid(row=2, column=0, sticky='w', columnspan=1), obj.append(genre_n)
            f = Text(font=('bold', 10), width=45, height=1)
            f.grid(row=2, column=1, sticky='w', padx=1, pady=2), obj.append(f)
            f.insert(0.0, genres[mus_i_genre][1])

            price = Label(foreground='gray', text='Цена', anchor='w', font=('bold', 11), padx=50)
            price.grid(row=3, column=0, sticky='w', columnspan=1), obj.append(price)
            f1 = Text(font=('bold', 10), width=45, height=1)
            f1.grid(row=3, column=1, sticky='w', padx=1, pady=2), obj.append(f1)
            f1.insert(0.0, genres[mus_i_genre][2])
            r+=1
            m_id_films = []
            for film in films:
                #print("1 film =", film, "id_g =", genres[mus_i_genre][0])
                if film[2]==genres[mus_i_genre][0]:

                    #r+=1
                    m_id_films.append(film[0])
                    print(m_id_films)
            id_f = 0
            if len(m_id_films)>0:
                print_film(m_id_films[id_f], id_f, len(m_id_films), m_id_films)

            def destroy_film():
                while len(mus_films) > 0:
                    mus_films.pop().destroy()

            def bott_prev_genre(a):
                print("a_genre_1 =", a, "len(mus_films) =", len(mus_films))
                if (a - 1) < 0:
                    MessageBox.showinfo(title='Ошибка!', message="Вы в начале списка жанров!")
                else:
                    if len(mus_films)>0:
                        destroy_film()
                    a -= 1
                    print_genre(genres[a][0], a)
            def bott_next_genre(a):
                print("a_genre_2 =", a)
                if (a + 1) >= len(genres):
                    MessageBox.showinfo(title='Ошибка!', message="Вы в конце списка жанров!")
                else:
                    if len(mus_films) > 0:
                        destroy_film()
                    a += 1
                    if isinstance(genres[a][1], str):
                        print_genre(genres[a][0], a)

            btt_prev_g = Button(text="<", bg='blue', command=lambda: bott_prev_genre(mus_i_genre))
            btt_prev_g.grid(row=1, column=7), obj.append(btt_prev_g)
            btt_next = Button(text=">", bg='blue', command=lambda: bott_next_genre(mus_i_genre))
            btt_next.grid(row=1, column=8, sticky='s'), obj.append(btt_next)

        id_g = genres[0][0]
        print("start id_g", id_g)
        print_genre(id_g, 0)

    root.mainloop()