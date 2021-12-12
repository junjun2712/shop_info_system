from tkinter import *
from view.login_ui import Application as login


if __name__ == '__main__':
    win = Tk()
    w = 800
    h = 540
    sw = win.winfo_screenwidth()
    # 得到屏幕宽度
    sh = win.winfo_screenheight()
    # 得到屏幕高度
    # 窗口宽高为100
    x = (sw - w) / 2
    y = (sh - h) / 2
    win.geometry('%dx%d+%d+%d' % (w, h, x, y))
    win.title('超市信息管理系统')
    win.resizable(width=False, height=False)
    # 加载login界面
    login(master=win)
    win.mainloop()