"""商品信息"""
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
from Dao.commodityMapper import info_com


def info_ui_begin():
    info = tk.Toplevel()
    w = 600
    h = 400
    x = (info.winfo_screenwidth() - w) / 2
    y = (info.winfo_screenheight() - h) / 2
    info.geometry('%dx%d+%d+%d' % (w, h, x, y))
    info.title('商品信息')
    info.resizable(width=False, height=False)
    info_frame = Frame(info, bg='#68B8BE',width=600,height=55)
    info_frame.place(x=0,y=0)
    inquire_font_1 = tkFont.Font(family='宋体', size=25, weight=tkFont.BOLD)
    Label(info_frame, text='商品信息', font=inquire_font_1, bg='#68B8BE').place(x=230, y=10)

    entries = []
    com_list = info_com()
    for i in com_list:
        args = (i.get_commodity()['com_code'], i.get_commodity()['com_name'], i.get_commodity()['com_price'],
                i.get_commodity()['com_stock'])
        entries.append(args)
    tabel_frame = Frame(info)
    tabel_frame.place(x=0, y=55, width=600, height=345)
    yscroll = Scrollbar(tabel_frame, orient=VERTICAL)
    style = ttk.Style()
    style.configure('Treeview.Heading', font=(None, 14))
    style.configure('Treeview', rowheight=30, font=(None,12))
    tree = ttk.Treeview(
        master=tabel_frame,
        columns=('商品编号', '商品名称', '商品价格', '商品库存'),
        yscrollcommand=yscroll.set,
    )
    yscroll.config(command=tree.yview)
    yscroll.pack(side=RIGHT, fill=Y)
    tree['show'] = 'headings'
    tree.heading('#1', text='商品编号')
    tree.heading('#2', text='商品名称')
    tree.heading('#3', text='商品价格')
    tree.heading('#4', text='商品库存')
    tree.column('#1', stretch=YES, width=150, minwidth=150, anchor='center')
    tree.column('#2', stretch=YES, width=150, minwidth=150, anchor='center')
    tree.column('#3', stretch=YES, width=150, minwidth=150, anchor='center')
    tree.column('#4', stretch=YES, width=150, minwidth=150, anchor='center')
    tree.pack(fill=BOTH, expand=1)

    for entry in entries:
        tree.insert('', 'end', values=(entry[0], entry[1], entry[2], entry[3]))
    info.mainloop()