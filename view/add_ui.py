"""添加商品"""
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename, askdirectory
from Dao.commodityMapper import add
from tkinter import messagebox
from controller.commodity_excel import com_excel
from controller.add_com_excel import add_com_excel
def add_ui_begin():
    add = tk.Toplevel()
    w = 600
    h = 400
    x = (add.winfo_screenwidth() - w) / 2
    y = (add.winfo_screenheight() - h) / 2
    global com_code
    global com_name
    global com_price
    global com_stock
    com_code = tk.StringVar()
    com_name = tk.StringVar()
    com_price = tk.StringVar()
    com_stock = tk.StringVar()
    add.geometry('%dx%d+%d+%d' % (w, h, x, y))
    add.title('修改商品')
    add.resizable(width=False, height=False)
    add_frame = Frame(add, bg='#68B8BE',width=600,height=400)
    add_frame.pack()
    add_font_1 = tkFont.Font(family='宋体', size=25, weight=tkFont.BOLD)
    Label(add_frame, text='添加商品信息', font=add_font_1, bg='#68B8BE').place(x=200, y=20)
    add_font_2 = tkFont.Font(family='宋体', size=15)
    Label(add_frame, text='商品编号：', font=add_font_2, bg='#68B8BE').place(x=100, y=90)
    modify_font_3 = tkFont.Font(family='宋体', size=9)
    Label(add_frame, text='注意：商品编号不可重复', font=modify_font_3, bg='#68B8BE').place(x=235, y=125)
    Label(add_frame, text='商品名称：', font=add_font_2, bg='#68B8BE').place(x=100, y=150)
    Label(add_frame, text='商品价格：', font=add_font_2, bg='#68B8BE').place(x=100, y=210)
    Label(add_frame, text='商品库存：', font=add_font_2, bg='#68B8BE').place(x=100, y=270)
    Entry(add_frame, highlightthickness=1, font=('宋体', 15), bg='#F3F3F4',textvariable=com_code).place(x=300, y=90, width=200, height=30)
    Entry(add_frame, highlightthickness=1, font=('宋体', 15), bg='#F3F3F4', textvariable=com_name).place(x=300, y=150, width=200, height=30)
    Entry(add_frame, highlightthickness=1, font=('宋体', 15), bg='#F3F3F4', textvariable=com_price).place(x=300, y=210, width=200, height=30)
    Entry(add_frame, highlightthickness=1, font=('宋体', 15), bg='#F3F3F4', textvariable=com_stock).place(x=300, y=270, width=200, height=30)
    Button(add_frame, text='批量添加', font=('宋体', 15, 'bold'), fg='#000000', bg="#ffffff", command=adds_com).place(x=70, y=325, width=120, height=40)
    Button(add_frame, text='立即添加', font=('宋体', 15, 'bold'), fg='#000000', bg="#ffffff", command=add_com).place(x=230, y=325, width=120, height=40)
    Button(add_frame, text='下载模板', font=('宋体', 15, 'bold'), fg='#000000', bg="#ffffff", command=dow_com).place(x=390, y=325, width=120, height=40)
    add.mainloop()

def adds_com():
    f = askopenfilename(title="上传文件", initialdir="D:",filetypes=[("Excel表格",".xlsx")])
    excel1 = add_com_excel(f)
    if excel1.result == True:
        messagebox.showinfo('提示', '导入成功')
    else:
        messagebox.showinfo('提示', '导入失败')


def add_com():
        result = add(com_code.get(), com_name.get(), com_price.get(), com_stock.get())
        if result == True:
            messagebox.showinfo('提示', '添加成功')
        else:
            messagebox.showinfo('提示', '添加失败')

def dow_com():
    f = askdirectory(title="选择保存的文件夹")
    excel1 = com_excel(f)
    if excel1.result == True:
        messagebox.showinfo('提示', '保存成功')
    else:
        messagebox.showinfo('提示', '保存失败')