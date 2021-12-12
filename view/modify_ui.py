"""修改商品"""
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from Dao.commodityMapper import modify
from Dao.commodityMapper import inquire
from tkinter import messagebox


def modify_ui_begin():
    modify = tk.Toplevel()
    w = 600
    h = 400
    x = (modify.winfo_screenwidth() - w) / 2
    y = (modify.winfo_screenheight() - h) / 2
    global com_code
    global com_name
    global com_price
    global com_stock
    global com_name_label
    global com_price_label
    global com_stock_label
    com_code = tk.StringVar()
    com_name = tk.StringVar()
    com_price = tk.StringVar()
    com_stock = tk.StringVar()
    modify.geometry('%dx%d+%d+%d' % (w, h, x, y))
    modify.title('修改商品')
    modify.resizable(width=False, height=False)
    modify_frame = Frame(modify, bg='#68B8BE',width=600,height=400)
    modify_frame.pack()
    modify_font_1 = tkFont.Font(family='宋体', size=25, weight=tkFont.BOLD)
    Label(modify_frame, text='修改商品信息', font=modify_font_1, bg='#68B8BE').place(x=200, y=20)
    modify_font_2 = tkFont.Font(family='宋体', size=15)
    modify_font_3 = tkFont.Font(family='宋体', size=9)
    Label(modify_frame, text='商品编号：', font=modify_font_2, bg='#68B8BE').place(x=100, y=90)
    Label(modify_frame, text='注意：商品编号不可修改', font=modify_font_3, bg='#68B8BE').place(x=235, y=125)
    Label(modify_frame, text='商品名称：', font=modify_font_2, bg='#68B8BE').place(x=100, y=150)
    Label(modify_frame, text='商品价格：', font=modify_font_2, bg='#68B8BE').place(x=100, y=210)
    Label(modify_frame, text='商品库存：', font=modify_font_2, bg='#68B8BE').place(x=100, y=270)

    Entry(modify_frame, highlightthickness=1, font=('宋体', 15), bg='#F3F3F4',textvariable=com_code).place(x=300, y=90, width=200, height=30)
    Entry(modify_frame, highlightthickness=1, font=('宋体', 15), bg='#F3F3F4', textvariable=com_name).place(x=300, y=150, width=200, height=30)
    Entry(modify_frame, highlightthickness=1, font=('宋体', 15), bg='#F3F3F4', textvariable=com_price).place(x=300, y=210, width=200, height=30)
    Entry(modify_frame, highlightthickness=1, font=('宋体', 15), bg='#F3F3F4', textvariable=com_stock).place(x=300, y=270, width=200, height=30)
    Button(modify_frame, text='立即查询', font=('宋体', 15, 'bold'), fg='#000000', bg="#ffffff", command=inquire_com).place(x=140, y=325, width=120, height=40)
    Button(modify_frame, text='立即修改', font=('宋体', 15, 'bold'), fg='#000000', bg="#ffffff", command=modify_com).place(x=340, y=325, width=120, height=40)
    modify.mainloop()

def inquire_com():
    com =  inquire(com_code.get())
    if com == False:
        com_code.set('查询失败')
        com_name.set('查询失败')
        com_price.set('查询失败')
        com_stock.set('查询失败')
    else:
        com_name.set(com.get_commodity()['com_name'])
        com_price.set(com.get_commodity()['com_price'])
        com_stock.set(com.get_commodity()['com_stock'])

def modify_com():
    result = modify(com_code.get(), com_name.get(), com_price.get(), com_stock.get())
    com_name.set('')
    com_price.set('')
    com_stock.set('')
    if result == True:
        messagebox.showinfo('提示', '修改成功')
    else:
        messagebox.showinfo('提示', '修改失败')
