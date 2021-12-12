from tkinter import *
import tkinter.font as tkFont
def about_ui_begin():
    about = Tk()
    w = 400
    h = 400
    x = (about.winfo_screenwidth() - w) / 2
    y = (about.winfo_screenheight() - h) / 2
    about.geometry('%dx%d+%d+%d' % (w, h, x, y))
    about.title('关于')
    about.resizable(width=False, height=False)
    about_frame = Frame(about, bg='#68B8BE', width=600, height=400)
    about_frame.pack()
    about_font_1 = tkFont.Font(family='宋体', size=16, weight=tkFont.BOLD)
    Label(about_frame, text='超市信息管理系统', font=about_font_1, bg='#68B8BE').place(x=110, y=20)
    Label(about_frame, text='组别：第五组', font=about_font_1, bg='#68B8BE').place(x=50, y=90)
    Label(about_frame, text='组长：韩梦洋', font=about_font_1, bg='#68B8BE').place(x=50, y=150)
    Label(about_frame, text='组员：彭衍召、常思明、徐昆银', font=about_font_1, bg='#68B8BE').place(x=50, y=210)
    Label(about_frame, text='李洲、王子豪、张帅兵、赵雪斌', font=about_font_1, bg='#68B8BE').place(x=50, y=270)
    Label(about_frame, text='班级：计本1904班', font=about_font_1, bg='#68B8BE').place(x=50, y=330)
    about.mainloop()