import re
import tkinter as tk
from urllib import parse
import tkinter.messagebox as msgbox
import webbrowser


class App(object):
    def __init__(self, width=500, height=300):
        self.w = width
        self.h = height

        # 软件名称属性设置
        self.title = '一起看定影'
        self.root = tk.Tk(className=self.title)
        self.root.iconbitmap('icon.ico')
        # 用户输入的视频链接
        self.url = tk.StringVar()  # 输入的链接定义成字符串

        # 定义播放源 默认选中第二个
        self.result_value = tk.IntVar()
        self.result_value_use_if = tk.IntVar()
        self.result_value.set(1)

        # 软件空间划分
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        # 控件内容设置
        group_text_0 = tk.Label(frame_1, text='一播通道：', padx=10, pady=10)
        tk_button_0 = tk.Radiobutton(frame_1, text='挂了留纪念', variable=self.result_value, value=0, width=10, height=1)

        group_text_1 = tk.Label(frame_1, text='二播通道：', padx=10, pady=10)
        tk_button_1 = tk.Radiobutton(frame_1, text='最推荐', variable=self.result_value, value=1, width=10, height=1)

        group_text_2 = tk.Label(frame_1, text='三播通道：', padx=10, pady=10)
        tk_button_2 = tk.Radiobutton(frame_1, text='比较慢', variable=self.result_value, value=2, width=10, height=1)

        group_text_3 = tk.Label(frame_1, text='四播通道：', padx=10, pady=10)
        tk_button_3 = tk.Radiobutton(frame_1, text='盘古解析', variable=self.result_value, value=3, width=10, height=1)

        group_text_4 = tk.Label(frame_1, text='五播通道：', padx=10, pady=10)
        tk_button_4 = tk.Radiobutton(frame_1, text='H8解析', variable=self.result_value, value=4, width=10, height=1)

        label = tk.Label(frame_2, text='请输入视频地址：')
        entry = tk.Entry(frame_2, textvariable=self.url)
        play = tk.Button(frame_2, text='播放', font=('楷体', 12), fg='Purple', width=2, height=1, command=self.video_play)

        # 控件布局
        frame_1.pack()  # 激活控件
        frame_2.pack()

        # 控件位置
        group_text_0.grid(row=0, column=0)
        tk_button_0.grid(row=0, column=1)
        group_text_1.grid(row=1, column=0)
        tk_button_1.grid(row=1, column=1)
        group_text_2.grid(row=2, column=0)
        tk_button_2.grid(row=2, column=1)
        group_text_3.grid(row=3, column=0)
        tk_button_3.grid(row=3, column=1)
        group_text_4.grid(row=4, column=0)
        tk_button_4.grid(row=4, column=1)

        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        play.grid(row=0, column=2, ipadx=10, ipady=10)

    # 定义播放功能
    def video_play(self):
        port_0 = 'http://www.wmxz.wang/video.php?url='
        port_1 = 'https://www.yemu.xyz/?url='
        port_2 = 'https://www.playm3u8.cn/jiexi.php?url='
        port_3 = 'https://www.pangujiexi.cc/jiexi.php?url='
        port_4 = 'https://www.h8jx.com/jiexi.php?url='

        self.result_value_use_if.set(self.result_value.get())
        # 使用正则表达式判断用户输入的地址是否正确
        if re.match(r'https?:/{2}\w.+$', self.url.get()):
            ip = self.url.get()
            ip = parse.quote_plus(ip)
            self.result_value_use_if.set(self.result_value.get())
            if self.result_value_use_if.get() == 0:
                webbrowser.open(port_0 + ip)
            elif self.result_value_use_if.get() == 1:
                webbrowser.open(port_1 + ip)
            elif self.result_value_use_if.get() == 2:
                webbrowser.open(port_2 + ip)
            elif self.result_value_use_if.get() == 3:
                webbrowser.open(port_3 + ip)
            elif self.result_value_use_if.get() == 4:
                webbrowser.open(port_4 + ip)
        else:
            msgbox.showerror(title='报错了！', message='视频地址输入不对劲！')

    def loop(self):
        self.root.resizable(True, True)
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.loop()


"""
备注：
variable=self.result_value, value=1/0
value = 0 / 1 
当选中第一个控件的时候，value = 0，同时把 0 赋值给 self.result_value，用于后续的判断。
当选择第二个控件的时候，value = 1 赋值给 self.result_value，用于后续的分支判断。
"""