# 爬取必应壁纸
import requests
import random
import json
from datetime import date
import os
import time
import tkinter as tk
from tkinter import scrolledtext
import tkinter.messagebox
from tkinter.filedialog import askdirectory
import webbrowser
from tkinter import *
from tkinter import ttk
import win32con
import win32gui
import win32api

"""爬虫头"""

agents = [
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
    "Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
    "Mozilla/3.01Gold (Win95; I)",
    "Mozilla/4.8 [en] (Windows NT 5.1; U)",
    "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.2; U; de-DE) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/234.40.1 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
    "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
 ]

agent = random.choice(agents)  # 随机从爬虫头库中随机选取一个头，防止网站拦截
headers = {"User-Agent": agent}


def sp():
    # 爬取必应壁纸
    def get_one_page(url):  # 解析给定url的网页源代码
        response = requests.get(url, headers=headers)
        if (response.status_code == 200):  # 状态码200说明返回状态正确，状态码是404,403等其他代号则说明网页请求失败
            return response.text
        return None

    def download(url, FileName2):  # 下载图片到本地文件夹
        DstDir = str(path.get()) + os.path.sep
        FileNameEnd = '.jpg'
        FileName = FileName2 + FileNameEnd
        File = open(DstDir + FileName, 'wb')
        response = requests.get(url, headers=headers)
        File.write(response.content)
        File.close()
        show_text.insert(END, str(FileName2))
        show_text.insert(END, '日壁纸—已下载到' + str(path.get()) + '\n')
        return 0


    def parse(html):  # 解析网页源代码
        pattern = re.compile('data-progressive="(.*?)".*?<h3>(.*?)</h3>')  # 正则表达式筛选html
        items = re.findall(pattern, html)
        for item in items:
            try:
                url = item[0].replace('640', '1920').replace('480', '1080')  # 替换图片尺寸
                imagename = item[1].strip()
                rule = re.compile(r'[a-zA-z1-9()-/]')  # []用来表示一组字符【abc】匹配a,b,或c
                imagename = rule.sub('', imagename)
                download(url, imagename.strip())
            except Exception:
                continue

    def main():
        value.set('当天')  # 默认选中当天==combobox.current(1)
        for i in range(1):
            if (str(path.get())) != '':
                url = 'https://bing.ioliu.cn/?p=' + str(i)
                html = get_one_page(url)
                parse(html)
            else:
                cle()
                show_text.insert(END, '请先选择保存路径！\n')
                break
        if (str(path.get())) != '':
            time.sleep(0.5)
            show_text.insert(END, '已下载完成\n')

    if __name__ == '__main__':
        main()



def spider():
    def main():
        num_ch = format(combobox.get())
        if num_ch == '当天':
            num = 1
        if num_ch == '三天':
            num = 3
        if num_ch == '五天':
            num = 5
        if num_ch == '一周':
            num = 7
        for i in range(num):
            if (str(path.get())) != '':
                address0 = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx='
                address1 = str(i)
                address2 = '&n=1&mkt=en-US'
                address = address0 + address1 + address2
                response = get_one_page(address)
                url = getUrl(response)
                url = "http://www.bing.com" + url
                downloadPic(url, i)
                progress()
            else:
                cle()
                show_text.insert(END, '请先选择保存路径！\n')
                break
        if (str(path.get())) != '':
            time.sleep(0.5)
            show_text.insert(END, '已下载完成\n')

    def get_one_page(url):  # 解析给定url的网页源代码
        response = requests.get(url, headers=headers)
        if (response.status_code == 200):  # 状态码200说明返回状态正确，状态码是404,403等其他代号则说明网页请求失败
            return response.text
        return None

    def getUrl(response):
        dict = json.loads(response)
        list = dict['images']
        # 获取url
        url = list[0]['url']
        url = url[:-20] + 'UHD' + url[-11:]
        url = url[:-39] + 'UHD' + url[-30:]
        return url

    def downloadPic(url, i):
        DstDir = str(path.get()) + os.path.sep
        today = date.today()
        fileDate = date.fromordinal(today.toordinal() - i)
        FileName2 = fileDate.isoformat()
        FileNameEnd = '.jpg'
        FileName = FileName2 + FileNameEnd
        File = open(DstDir + FileName, 'wb')

        response = requests.get(url, headers=headers)
        File.write(response.content)
        File.close()
        show_text.insert(END, str(FileName2))
        show_text.insert(END, '日壁纸—已下载到' + str(path.get()) + '\n')
        return 0

    if __name__ == '__main__':
        cle()
        main()



def text():
    cle()
    show_text.insert(END, '获取bing图片或设置为壁纸，运行时间取决当前网速，请先选择保存路径！\n')
    show_text.insert(END, '注：设置壁纸请勿使用桌面整理工具！高清壁纸请勿用作商业用途！\n')
    return None


def aboutme():
    webbrowser.open("https://user.qzone.qq.com/2268289662")
    return None


def select_Path():
    """选取本地路径"""
    path_ = askdirectory()
    path.set(path_)
    return None


def set_img_as_wallpaper():
    value.set('当天')  # 默认选中当天==combobox.current(1)
    spider()
    today = date.today()
    fileDate = date.fromordinal(today.toordinal())
    FileName2 = fileDate.isoformat()
    FileNameEnd = '.jpg'
    FileName = FileName2 + FileNameEnd
    filepath = str(path.get())  # 图片文件的的路径
    filemane = str(FileName)
    file = filepath + '/' + filemane
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 2：拉伸  0：居中  6：适应  10：填充
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # SPIF_SENDWININICHANGE 这个参数意思为立即生效
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, file, win32con.SPIF_SENDWININICHANGE)
    if (str(path.get())) != '':
        show_text.insert(END, '图片已设置为壁纸~\n')

def quited():
    quit = tkinter.messagebox.askokcancel('确认', '确定退出吗？')
    if quit == True:
        win.destroy()
    return None


def cle():
    """定义一个函数，用于清空输出框的内容"""
    show_text.delete(1.0, "end")  # 从第一行清除到最后一行
    return None


def progress():
    # 填充进度条
    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
    x = 50  # 未知变量，可更改
    n = 465 / x  # 465是矩形填充满的次数
    for i in range(x):
        n = n + 465 / x
        canvas.coords(fill_line, (0, 0, n, 60))
        win.update()
        time.sleep(0.005)  # 控制进度条流动的速度
    # 清空进度条
    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="white")
    x = 50  # 未知变量，可更改
    n = 465 / x  # 465是矩形填充满的次数

    for t in range(x):
        n = n + 465 / x
        # 以矩形的长度作为变量值更新
        canvas.coords(fill_line, (0, 0, n, 60))
        win.update()
        time.sleep(0)  # 时间为0，即飞速清空进度条


win = tk.Tk()
win.title('槐序壁纸')
win.resizable(0, 0)  # 禁止调整窗口大小
win.geometry('500x380')
win.iconbitmap('c.ico')

path = tk.StringVar()
tk.Label(win, text='BY:', font=('宋体', 20)).place(x=38, y=10)
tk.Label(win, text='HUAI XU', font=('宋体', 20)).place(x=70, y=40)
tk.Label(win, text='bug请联系作者', font=('隶书', 12)).place(x=50, y=350)
tk.Label(win, text='仅供娱乐', font=('隶书', 12)).place(x=360, y=350)
tk.Label(win, text='下载进度', font=('SimHei', 10)).place(x=40, y=182)
tk.Label(win, text='选择下载日期', font=('宋体', 12)).place(x=38, y=138)

tk.Entry(win, textvariable=path, width=50).place(x=40, y=85)  # 创建一个输入框,显示图片存放路径

aa = tk.Button(win, bg='skyblue', text='原图下载', font=('SimHei', 10), width=10, height=2, command=spider)
aa.place(x=386, y=208)

bb = tk.Button(win, bg='skyblue', text='关闭程序', font=('SimHei', 10), width=8, height=2, command=quited)
bb.place(x=400, y=130)

cc = tk.Button(win, bg='skyblue', text='程序介绍', font=('SimHei', 10), width=8, height=2, command=text)
cc.place(x=220, y=130)

dd = tk.Button(win, bg='skyblue', text='选择路径', relief=tk.RAISED, width=8, height=1, command=select_Path)
dd.place(x=400, y=80)

ee = tk.Button(win, bg='skyblue', text='清空输出', font=('SimHei', 10), width=8, height=2, command=cle)
ee.place(x=310, y=130)

ff = tk.Button(win, text='联系我', font=('SimHei', 10), width=8, height=1, command=aboutme)
ff.place(x=220, y=350)

gg = tk.Button(win, bg='skyblue', text='设置为壁纸', font=('SimHei', 10), width=10, height=2, command=set_img_as_wallpaper)
gg.place(x=386, y=306)

hh = tk.Button(win, bg='skyblue', text='非原图下载', font=('SimHei', 10), width=10, height=2, command=sp)
hh.place(x=386, y=256)

canvas = tk.Canvas(win, width=364, height=20, bg="white")
canvas.place(x=100, y=180)

show_text = scrolledtext.ScrolledText(win, width=45, height=10, font=('SimHei', 10))  # 滑轮框
show_text.place(x=40, y=210)

value = StringVar()
value.set('当天')  # 默认选中当天==combobox.current(1)
values = ['当天', '三天', '五天', '一周']
combobox = ttk.Combobox(
    master=win,  # 父容器
    height=20,  # 高度,下拉显示的条目数量
    width=5,  # 宽度
    state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
    cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
    font=('', 12),  # 字体
    textvariable=value,  # 通过StringVar设置可改变的值
    values=values,  # 设置下拉框的选项
)
combobox.place(x=142, y=138)

win.mainloop()
