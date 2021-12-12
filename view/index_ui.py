from tkinter import *
import tkinter.font as tkFont
from view.about_ui import about_ui_begin
from view.modify_ui import modify_ui_begin
from view.inquire_ui import inquire_ui_begin
from view.add_ui import add_ui_begin
from view.info_ui import info_ui_begin
from view.delete_ui import delete_ui_begin

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        global photo_bg
        photo_bg = PhotoImage(file='./images/login.gif')
        # 使用时../改为./
        label_bg = Label(self, image=photo_bg)
        label_bg.pack()
        self.frame_left = Frame(self, bg='#68B8BE',width=200, height=540).place(x=0, y=0)
        global photo_Avatar
        photo_Avatar = PhotoImage(file='./images/Avatar.gif')
        label_Avatar = Label(self.frame_left, bg='#68B8BE', image=photo_Avatar)
        label_Avatar.place(x=23, y=25)
        menu_font = tkFont.Font(family='宋体', size=10)
        Button(self.frame_left, text='商品信息', font=menu_font, fg='#000000', bg="#ffffff", command=self.index_info).place(x=30, y=193, width=140, height=30)
        Button(self.frame_left, text='查询商品', font=menu_font, fg='#000000', bg="#ffffff", command=self.index_inquire).place(x=30, y=243, width=140, height=30)
        Button(self.frame_left, text='添加商品', font=menu_font, fg='#000000', bg="#ffffff", command=self.index_add).place(x=30, y=293, width=140, height=30)
        Button(self.frame_left, text='修改商品', font=menu_font, fg='#000000', bg="#ffffff", command=self.index_modify).place(x=30, y=343, width=140, height=30)
        Button(self.frame_left, text='删除商品', font=menu_font, fg='#000000', bg="#ffffff", command=self.index_delete).place(x=30, y=393, width=140, height=30)
        Button(self.frame_left, text='关于', font=menu_font, fg='#000000', bg="#ffffff", command=self.index_about).place(x=30, y=443, width=140, height=30)
        Button(self.frame_left, text='退出', font=menu_font, fg='#000000', bg="#ffffff", command=self.index_quit).place(x=30, y=493, width=140, height=30)

        self.frame_right = Frame(self, width=600, height=540).place(x=200, y=0)
        global photo_index
        photo_index = PhotoImage(file='./images/info.gif')
        Label(self.frame_right, image=photo_index).place(x=200, y=0)

    # 商品信息
    def index_info(self):
        info_ui_begin()
    # 查询商品
    def index_inquire(self):
        inquire_ui_begin()
    # 添加商品
    def index_add(self):
        add_ui_begin()
    # 修改商品
    def index_modify(self):
        modify_ui_begin()
    # 删除商品
    def index_delete(self):
        delete_ui_begin()
    # 关于
    def index_about(self):
        about_ui_begin()

    # 退出-销毁界面
    def index_quit(self):
        self.master.destroy()
