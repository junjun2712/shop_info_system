"""删除商品"""
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox

from Dao.commodityMapper import inquire
from Dao.commodityMapper import delete

def delete_ui_begin():
    delete = tk.Toplevel()
    w = 600
    h = 400
    x = (delete.winfo_screenwidth() - w) / 2
    y = (delete.winfo_screenheight() - h) / 2
    global com_name
    global com_price
    global com_stock
    global com_name_label
    global com_price_label
    global com_stock_label
    com_name = '查询中'
    com_price = '查询中'
    com_stock = '查询中'
    delete.geometry('%dx%d+%d+%d' % (w, h, x, y))
    delete.title('删除商品')
    delete.resizable(width=False, height=False)
    delete_frame = Frame(delete, bg='#68B8BE',width=600,height=400)
    delete_frame.pack()
    delete_font_1 = tkFont.Font(family='宋体', size=25, weight=tkFont.BOLD)
    Label(delete_frame, text='删除商品信息', font=delete_font_1, bg='#68B8BE').place(x=200, y=20)
    delete_font_2 = tkFont.Font(family='宋体', size=15)
    Label(delete_frame, text='商品编号：', font=delete_font_2, bg='#68B8BE').place(x=200, y=90)
    Label(delete_frame, text='商品名称：', font=delete_font_2, bg='#68B8BE').place(x=200, y=150)
    Label(delete_frame, text='商品价格：', font=delete_font_2, bg='#68B8BE').place(x=200, y=210)
    Label(delete_frame, text='商品库存：', font=delete_font_2, bg='#68B8BE').place(x=200, y=270)
    com_code = tk.StringVar()
    Entry(delete_frame, highlightthickness=1, font=('宋体', 15), bg='#F3F3F4',textvariable=com_code).place(x=300, y=90, width=200, height=30)
    com_name_label = Label(delete_frame, text=com_name, font=delete_font_2, bg='#68B8BE')
    com_name_label.place(x=300, y=150)
    com_price_label = Label(delete_frame, text=com_price, font=delete_font_2, bg='#68B8BE')
    com_price_label.place(x=300, y=210)
    com_stock_label = Label(delete_frame, text=com_stock, font=delete_font_2, bg='#68B8BE')
    com_stock_label.place(x=300, y=270)
    Button(delete_frame, text='立即查询', font=('宋体', 15, 'bold'), fg='#000000', bg="#ffffff", command=lambda:inquire_com(com_code)).place(x=140, y=325, width=120, height=40)
    Button(delete_frame, text='立即删除', font=('宋体', 15, 'bold'), fg='#000000', bg="#ffffff", command=lambda:delete_com(com_code)).place(x=340, y=325, width=120, height=40)
    delete.mainloop()

def inquire_com(com_code):
    com =  inquire(com_code.get())
    if com == False:
        com_code.set('查询失败')
        com_name_label.config(text='查询失败')
        com_price_label.config(text='查询失败')
        com_stock_label.config(text='查询失败')
    else:
        com_name_label.config(text=com.get_commodity()['com_name'])
        com_price_label.config(text=com.get_commodity()['com_price'])
        com_stock_label.config(text=com.get_commodity()['com_stock'])
def delete_com(com_code):
    result = delete(com_code.get())
    if result == True:
        messagebox.showinfo('提示', '删除成功')
    else:
        messagebox.showinfo('提示', '删除失败')