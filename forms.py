from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as MessageBox
from tkinter.ttk import Combobox
from admin_clients import open_clients
from admin_orders import open_orders
from admin_films import open_films
from admin_genres_price import open_genres
from admin_prod import open_produc
from user_films import open_films_u


global lab
def open_admin_form(root):
    #отчистка экрана
    def destroy():
        obj = [label, orders, clients, films, genres, prods]
        for object_name in obj:
            object_name.destroy()

    def back():
        destroy()
        from intro import print_intro
        print_intro()

    def open_ordrs():
        destroy()
        open_orders(root)
    def open_clnts():
        destroy()
        open_clients(root)

    def open_flms():
        destroy()
        open_films(root)
    def open_gnrs():
        destroy()
        open_genres(root)

    def open_pr():
        destroy()
        open_produc(root)


    label = Label(text="Меню", font=("Arial", 14))
    label.pack()



    orders = Button (text = 'Заказы', font=('italic', 14), width=20,  bg='lightcyan', command=open_ordrs)
    orders.place(x = 385, y = 40)

    clients = Button (text = 'Клиенты', font=('italic', 14), width=20, bg='lightcyan', command = open_clnts)
    clients.place(x = 385, y = 90)

    films = Button (text = 'Фильмы', font=('italic', 14), width=20, bg='lightcyan', command = open_flms)
    films.place(x = 385, y = 140)

    genres = Button (text = 'Жанры и цены за них', font=('italic', 14), width=20, bg='lightcyan', command = open_gnrs)
    genres.place(x = 385, y = 190)

    prods = Button (text = 'Режиссеры', font=('italic', 14), width=20, bg='lightcyan', command = open_pr)
    prods.place(x = 385, y = 240)

def open_user_form(root):
    def destroy():
        while len(obj) > 0:
            obj.pop().destroy()
            #lab.delete()

    def back():
        destroy()
        from intro import print_intro
        print_intro()

    def open_flms_u():
        destroy()
        open_films_u(root)

    def open_pr():
        destroy()
        open_produc(root)

    """
    path ='C:/Users/dasha/OneDrive/Рабочий стол/Учеба/2ой курс/3 sem/МД+БД(Access)/макет/pic.png'
    python_logo = PhotoImage(open(path))

    label = Label(image=python_logo, text="Меню", compound="top", bg='black', fg='white', height=100, width=150)
    label.pack(side = "bottom", fill = "both")
    """


    #path = 'C:/Users/dasha/OneDrive/Рабочий стол/Учеба/2ой курс/3 sem/МД+БД(Access)/макет'
    image=Image.open("C:/Users/dasha/pic.png")
    #img = PhotoImage(file="C:/Users/dasha/pic.png")
    photo = ImageTk.PhotoImage(image)



    obj=[]
    #lab = Label(root, image=photo).place(x=50, y=10)



    films = Button(text='Фильмы', font=('italic', 10), width=20, bg='lightcyan', command=open_flms_u)
    films.place(x=218, y=105), obj.append(films)

    prods = Button(text='Режиссеры', font=('italic', 10), width=20, bg='lightcyan', command=open_pr)
    prods.place(x=218, y=145), obj.append(prods)
    root.mainloop()

