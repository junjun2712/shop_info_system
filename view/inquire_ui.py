"""查询商品"""
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from Dao.commodityMapper import inquire

def inquire_ui_begin():
    inquire = tk.Toplevel()
    w = 600
    h = 400
    x = (inquire.winfo_screenwidth() - w) / 2
    y = (inquire.winfo_screenheight() - h) / 2
    global com_name
    global com_price
    global com_stock
    global com_name_label
    global com_price_label
    global com_stock_label
    com_name = '查询中'
    com_price = '查询中'
    com_stock = '查询中'
    inquire.geometry('%dx%d+%d+%d' % (w, h, x, y))
    inquire.title('查询商品')
    inquire.resizable(width=False, height=False)
    inquire_frame = Frame(inquire, bg='#68B8BE',width=600,height=400)
    inquire_frame.pack()
    inquire_font_1 = tkFont.Font(family='宋体', size=25, weight=tkFont.BOLD)
    Label(inquire_frame, text='查询商品信息', font=inquire_font_1, bg='#68B8BE').place(x=200, y=20)
    inquire_font_2 = tkFont.Font(family='宋体', size=15)
    Label(inquire_frame, text='商品编号：', font=inquire_font_2, bg='#68B8BE').place(x=200, y=90)
    Label(inquire_frame, text='商品名称：', font=inquire_font_2, bg='#68B8BE').place(x=200, y=150)
    Label(inquire_frame, text='商品价格：', font=inquire_font_2, bg='#68B8BE').place(x=200, y=210)
    Label(inquire_frame, text='商品库存：', font=inquire_font_2, bg='#68B8BE').place(x=200, y=270)
    com_code = tk.StringVar()
    Entry(inquire_frame, highlightthickness=1, font=('宋体', 15), bg='#F3F3F4',textvariable=com_code).place(x=300, y=90, width=200, height=30)
    com_name_label = Label(inquire_frame, text=com_name, font=inquire_font_2, bg='#68B8BE')
    com_name_label.place(x=300, y=150)
    com_price_label = Label(inquire_frame, text=com_price, font=inquire_font_2, bg='#68B8BE')
    com_price_label.place(x=300, y=210)
    com_stock_label = Label(inquire_frame, text=com_stock, font=inquire_font_2, bg='#68B8BE')
    com_stock_label.place(x=300, y=270)
    Button(inquire_frame, text='立即查询', font=('宋体', 15, 'bold'), fg='#000000', bg="#ffffff", command=lambda:inquire_com(com_code)).place(x=180, y=325, width=240, height=40)
    inquire.mainloop()

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