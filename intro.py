from tkinter import *
import tkinter.messagebox as MessageBox
from tkinter.ttk import Combobox
from forms import open_user_form, open_admin_form

root = Tk()
root.geometry("1000x550")
root.title("АИС Фирмы по прокату фильмов")

def print_intro():
    #отчистка экрана
    def destroy():
        obj = [group, pw, label, e_group, e_pw, ok]
        for object_name in obj:
            object_name.destroy()

    # выбор пользователя
    def insert():
        gr= e_group.get()
        pwd = e_pw.get()
        if (gr == 'Администратор'):
            if (pwd != '1'):
                MessageBox.showinfo(title='Ошибка!', message="Пароль не верный!")
            else:
                destroy()
                open_admin_form(root)
        elif (gr == 'User'):
            if (pwd != '1'):
                MessageBox.showinfo(title='Ошибка!', message="Пароль не верный!")
            else:
                destroy()
                open_user_form(root)
        elif (pwd != ''):
            MessageBox.showinfo(title='Ошибка!',  message="Имя пользователя не корректно!")




    group = Label(root, text='Группа пользователей', font=('bold', 11))
    group.place(x=20, y=60)

    pw = Label(root, text='Пароль', font=('bold', 11))
    pw.place(x=20, y=120)



    groups = ['Администратор', 'User']

    group_var = StringVar(value = groups[0])

    label = Label(textvariable=group_var, font=('bold', 12))

    e_group = Combobox(textvariable=group_var, values=groups)
    e_group.pack(anchor=NW, padx=6, pady=60)
    e_group.place(x = 200, y = 60)


    e_pw = Entry(show='*')
    e_pw.place(x = 200, y = 120)

    ok = Button (root, text = 'OK', font=('italic', 11), bg='white', command = insert)
    ok.place(x = 20, y = 150)

    root.mainloop()

