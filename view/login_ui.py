#coding=utf-8
import tkinter
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from controller import login_verify
from view.index_ui import Application as index_ui


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()
        self.createWidget()

    def createWidget(self):
        # 背景图片
        global photo_login
        photo_login = PhotoImage(file='./images/login.gif')
        self.label_bg = Label(self, image=photo_login)
        self.label_bg.pack()

        # 欢迎语区域
        global photo_login_center
        photo_login_center = PhotoImage(file='./images/login_center.gif')
        label_login_center = Label(self, image=photo_login_center,  width='600', height='340')
        label_login_center.place(x='100', y='100')
        welcome_font_1 =  tkFont.Font(family='宋体', size=30, weight=tkFont.BOLD)
        label_welcome_1 = Label(self, text='Welcome', font=welcome_font_1, bg='#56cdff')
        label_welcome_1.place(x=175, y=170)
        welcome_font_2 = tkFont.Font(family='宋体', size=20, weight=tkFont.BOLD)
        label_welcome_2 = Label(self, text='欢迎登录超市信息', font=welcome_font_2, bg='#56cdff')
        label_welcome_2.place(x=140, y=260)
        label_welcome_3 = Label(self, text='管理系统', font=welcome_font_2, bg='#56cdff')
        label_welcome_3.place(x=195, y=320)

        # 数据输入区域
        login_font = tkFont.Font(family='宋体', size=9)
        login_user = Label(self, text='请输入账号:', font=login_font, bg='#ffffff')
        login_user.place(x=430, y=160)
        Entry(self, highlightthickness=1, font=('宋体', 15), bg='#F3F3F4',textvariable=self.username).place(x=430, y=190,width=240,height=40)
        login_pass = Label(self, text='请输入密码:', font=login_font, bg='#ffffff')
        login_pass.place(x=430, y=240)
        Entry(self, highlightthickness=1,font=('宋体', 15), bg='#F3F3F4', show='*', textvariable=self.password).place(x=430, y=270, width=240, height=40)
        Button(self, text='立即登录', font=('宋体', 15, 'bold'), fg='#000000', bg="#56cdff", command=self.login).place(x=430, y=340, width=240, height=40)

    def login(self):
        errMessage = ""
        username = self.username.get()
        password = self.password.get()
        new_errMessage = login_verify.login_verify(username, password)
        errMessage = errMessage + new_errMessage
        if errMessage != "":
            messagebox.showinfo('提示', errMessage)
            self.password.set('')
        if new_errMessage == '登录成功':
            self.login_destroy()
            # 加载index界面
            index_ui(self.master)

    # 销毁界面
    def login_destroy(self):
        self.destroy()


