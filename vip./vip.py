import tkinter as tk
import requests
import re 
import webbrowser

#创建一个窗口
root = tk.Tk()
#设置窗口大小
root.geometry('562x331+200+200')

#设置标题
root.title('在线看电影软件')

def show():
    #判断选择哪个窗口，获取选择的是哪个窗口
    num = num_int_var.get()
    #获取输入的内容
    word = input_va.get()
    if num ==1:
        # print('选择的是第一个窗口')
        # print('输入的内容是',word)
        link = 'https://jiexi.pengdouw.com/jiexi1/?url' + word
        html_data =requests.get(url=link).text
        vido_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)',html_data)[0]
        webbrowser.open(vido_url)
    elif num == 2:
        link = 'https://jiexi.pengdouw.com/jiexi2/?url' + word
        html_data =requests.get(url=link).text
        vido_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)',html_data)[0]
        webbrowser.open(vido_url)  
    elif num == 3:
        link = 'https://jiexi.pengdouw.com/jiexi3/?url' + word
        html_data =requests.get(url=link).text
        vido_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)',html_data)[0]
        webbrowser.open(vido_url)  


#设置读取一张照片
img = tk.PhotoImage(file='/Users/frank_young/Desktop/code/截屏2022-11-30 23.02.01.png')
#布局图片
tk.Label(root,image=img).pack()
#设置标签框
choose_frame = tk.LabelFrame(root)
choose_frame.pack(pady=10,fill='both')

tk.Label(choose_frame,text='选择接口：',font=('黑体',18)).pack(side=tk.LEFT)
#设置可变变量
num_int_var = tk.IntVar() 
#设置默认选项
num_int_var.set(1)
#设置选择
tk.Radiobutton(choose_frame,text='1号通用VIP引擎系统',variable=num_int_var,value=1).pack(side=tk.LEFT,padx=5)
tk.Radiobutton(choose_frame,text='2号通用VIP引擎系统',variable=num_int_var,value=2).pack(side=tk.LEFT,padx=5)
tk.Radiobutton(choose_frame,text='3号通用VIP引擎系统',variable=num_int_var,value=3).pack(side=tk.LEFT,padx=5)
#输入标签框
input_frame = tk.LabelFrame(root)
input_frame.pack(pady=10,fill='both')
#设置一个可变变量
input_va = tk.StringVar()


tk.Label(input_frame,text='播放地址：',font=('黑体',18)).pack(side=tk.LEFT)
tk.Entry(input_frame,width=100,relief='flat',textvariable=input_va).pack(side=tk.LEFT,fill='both')
#设置点击解析按钮
tk.Button(root,text='Go点击在线解析播放',font=('黑体',15),relief='flat',background='Green',command=show).pack(fill='both')
#让窗口持续展现
root.mainloop()