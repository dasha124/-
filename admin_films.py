from tkinter import *
import pymssql
from tkinter.ttk import Treeview
import tkinter.messagebox as MessageBox


def open_films(root):
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


        def change_av(id_, av):
            cur = connection.cursor()
            print("avail =", av, id_)
            if av==True:
                av=False
            else:
                av=True
            cur.execute("UPDATE Film SET available=%s where ID_film=%s",
                        (av, id_))
            connection.commit()
            cur = connection.cursor()
            s0 = 'SELECT *FROM "Film"'
            cur.execute(s0)
            films1 = cur.fetchall()
            cur = connection.cursor()
            s3 = 'SELECT *FROM "FilmGenre"'
            cur.execute(s3)
            genres1 = cur.fetchall()
            for i in range(10):
                obj.pop().destroy()
            for i in range(len(films1)):
                if films1[i][0]==id_:
                    id_=i
                    break
            print_film(id_, films1, genres1)

        def change_genre(p1, p2):

            print("p1 =", p1, "p2 =", p2)
            cur = connection.cursor()
            cur.execute("UPDATE Film SET ID_genre=%s where ID_film=%s",
                        (p2, p1))
            connection.commit()

            cur = connection.cursor()
            s0 = 'SELECT *FROM "Film"'
            cur.execute(s0)
            films2 = cur.fetchall()
            cur = connection.cursor()
            s3 = 'SELECT *FROM "FilmGenre"'
            cur.execute(s3)
            genres2 = cur.fetchall()
            for i in range(10):
                obj.pop().destroy()
            for i in range(len(films2)):
                if films2[i][0]==p1:
                    p1=i
                    break
            print_film(p1, films2, genres2)


        def del_film(id_, name):
            print("id =", id_, "name =", name)

            cur = connection.cursor()
            cur.execute("DELETE FROM Booking WHERE ID_film=%s", (id_))
            connection.commit()

            cur = connection.cursor()
            cur.execute("DELETE FROM Film WHERE ID_film=%s", (id_))
            connection.commit()

            MessageBox.showinfo(title='Внимание!', message="Данный фильм удален!")

            cur = connection.cursor()
            s0 = 'SELECT *FROM "Film"'
            cur.execute(s0)
            films3 = cur.fetchall()
            cur = connection.cursor()
            s3 = 'SELECT *FROM "FilmGenre"'
            cur.execute(s3)
            genres3 = cur.fetchall()
            for i in range(10):
                obj.pop().destroy()
            if id_==1:
                print_film(id_+1, films3, genres3)
            else:
                print_film(id_ - 1, films3, genres3)



        select_films_f = 'SELECT *FROM "Film"'
        cursor.execute(select_films_f)
        films0 = cursor.fetchall()
        select_genres = 'SELECT *FROM "FilmGenre"'
        cursor.execute(select_genres)
        genres0 = cursor.fetchall()

        obj = []
        for c in range(8): root.columnconfigure(index=c, weight=1)

        r1 = 0
        #mus_films = []
        #шапка
        bck = Button(text="Назад", background="lightcyan", width=6, height=1, command=back)
        bck.grid(row=0, column=7, sticky='n', pady=1), obj.append(bck)
        label_f = Label(foreground='blue', text='Фильмы', anchor='w', font=('bold', 14), pady=5, padx=10)
        label_f.grid(row=0, column=0, sticky='w', columnspan=1, padx=5), obj.append(label_f)

        r = 0
        """
        label_enter = Label(foreground='gray', font=('bold', 11), text='Введите название фильма', anchor='w', width=30)
        label_enter.grid(row=r, column=1), obj.append(label_enter)

        v = StringVar(value='*')
        cl_en = Entry(textvariable=v)
        cl_en.grid(row=r, column=2, sticky='e'), obj.append(cl_en)

        ok = Button(text='OK', font=('italic', 10), height=1, width=3, bg='lightgray',
                    command="")
        ok.grid(row=r, column=4, pady=2, sticky='w'), obj.append(ok)
        """
        fn = Label(foreground='gray', text='Название фильма', anchor='nw', font=('bold', 11), padx=50)
        fn.grid(row=1, column=0, sticky='nw', columnspan=1), obj.append(fn)
        av = Label(foreground='gray', text='Доступность', anchor='nw', font=('bold', 11), padx=2, width=20)
        av.grid(row=1, column=1, sticky='nw', columnspan=1), obj.append(av)
        y = Label(foreground='gray', text='Год', anchor='nw', font=('bold', 11), padx=2)
        y.grid(row=1, column=1, sticky='ne', columnspan=1), obj.append(y)
        с = Label(foreground='gray', text='Страна', anchor='nw', font=('bold', 11), padx=2)
        с.grid(row=1, column=2, sticky='nw'), obj.append(с)
        t = Label(foreground='gray', text='(мин)', anchor='w', font=('bold', 11), padx=2)
        t.grid(row=1, column=4, sticky='w'), obj.append(t)
        ag = Label(foreground='gray', text='Возраст+', anchor='nw', font=('bold', 11), padx=2)
        ag.grid(row=1, column=5, sticky='nw', columnspan=1), obj.append(ag)
        g = Label(foreground='gray', text='Жанр', anchor='nw', font=('bold', 11), padx=2)
        g.grid(row=1, column=6, sticky='ne', columnspan=1), obj.append(g)
        sl = Label(foreground='gray', text='Слоган', anchor='nw', font=('bold', 11), padx=2)
        sl.grid(row=3, column=0, sticky='nw', columnspan=1), obj.append(sl)


        def print_film(c, films, genres):
            def bott_next(a):
                if (a + 1) >= len(films):
                    MessageBox.showinfo(title='Ошибка!', message="Вы в конце списка!")
                else:
                    a += 1
                    print_film(a, films, genres)

            def bott_prev(a):
                if (a - 1) < 0:
                    MessageBox.showinfo(title='Ошибка!', message="Вы в начале списка!")
                else:
                    a -= 1
                    print_film(a, films, genres)
            print("film[c][..] =", films[c])
            r = 2

            f = Text(font=('bold', 10), width=45, height=1)
            f.grid(row=r, column=0, sticky='w', padx=1, pady=2), obj.append(f)
            f.insert(0.0, films[c][1])

            print("av =", films[c][3], films[c][0])
            if films[c][3] == True:
                b = 'green'
            else:
                b = 'red'

            av_btt = Button(text="", background=b, width=1, height=1, command=lambda: change_av(films[c][0], films[c][3]))
            av_btt.grid(row=r, column=1, sticky='nw', padx=5, pady=4), obj.append(av_btt)
            yt = Text(font=('bold', 10), width=5, height=1)
            yt.grid(row=r, column=1, sticky='ne', padx=5, pady=1), obj.append(yt)
            yt.insert(0.0, films[c][4])
            ct = Text(font=('bold', 10), width=20, height=1)
            ct.grid(row=r, column=2, sticky='nw', padx=5, pady=1), obj.append(ct)
            ct.insert(0.0, films[c][6])
            tt = Text(font=('bold', 10), width=7, height=1)
            tt.grid(row=r, column=4, sticky='nw', padx=5, pady=1), obj.append(tt)
            tt.insert(0.0, films[c][7])
            ag = Text(font=('bold', 10), width=10, height=1)
            ag.grid(row=r, column=5, sticky='nw', padx=5, pady=1), obj.append(ag)
            ag.insert(0.0, films[c][8])

            slog = Text(font=('bold', 10), width=45, height=2, wrap='word')
            slog.grid(row=4, column=0, sticky='nw', padx=5, pady=1), obj.append(slog)
            slog.insert(0.0, films[c][9])

            genr_but_m=[]
            i=0
            for genre in genres:
                if isinstance(genre[1], str):
                    if genre[0] == films[c][2]:
                        b = 'green'
                    else:
                        b = 'lightgreen'
                    f1 = Button(width=15, height=1, text=genre[1], background=b, command=lambda m1=films[c][0], m2 =genre[0]:change_genre(m1, m2))
                    genr_but_m.append(f1)
                    genr_but_m[i].grid(row=r, column=6, sticky='n', padx=5, pady=1), obj.append(f1)
                    r += 1
                    i+=1
            btt_prev = Button(text="Вверх", bg='blue', command=lambda: bott_prev(c))
            btt_prev.grid(row=2, column=7), obj.append(btt_prev)
            btt_next = Button(text="Вниз", bg='blue', command=lambda: bott_next(c))
            btt_next.grid(row=15, column=7), obj.append(btt_next)
            #btt_del = Button(text="Удалить запись", width=17, bg='lightcyan', command=lambda: del_film(films[c][0], films[c][1]))
            #btt_del.grid(row=16, column=7, pady=7, padx=2), obj.append(btt_del)

        c = 0
        print_film(c, films0, genres0)

    root.mainloop()


