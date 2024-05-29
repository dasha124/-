#import mysql.connector as
import pymssql
from tkinter import *
import tkinter.messagebox as MessageBox
from reciept import print_rec


from intro import print_intro


connection = 0
try:
    connection = pymssql.connect(
        host = '127.0.0.1',
        user = 'pass',
        password = '1',
        database = 'AIS_2'
    )
    print('successfully connected...')
    print_intro()

except Exception as ex:
    print("Connection refused...")
    print(ex)


