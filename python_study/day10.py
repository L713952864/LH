"""
开发GUI: wxPython\PyQt\PyGTK
使用tkinter:
1 导入tkinter模块中我们需要的东西。
2 创建一个顶层窗口对象并用它来承载整个GUI应用。
3 在顶层窗口对象上添加GUI组件。
4 通过代码将这些GUI组件的功能组织起来。
5 进入主事件循环(main loop)。

开发游戏：pygame/Panda3D
"""

import tkinter
import tkinter.messagebox

def main():
    # 1
    flag = True
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('blue', 'HELLO, GUI') if flag else ('red', 'GOODBYE GUI')
        label.config(text=msg, fg=color)

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('退出？'):
            top.quit()

    # 2
    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('480x320')
    # 设置窗口标题
    top.title('Main Window')

    # 3 4
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器:panel
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 5 开启主事件循环
    tkinter.mainloop()
if __name__ == '__main__':
    main()