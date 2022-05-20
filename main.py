"""
    Topic： 车辆违章信息查询系统
    Create: 2020-10-03
    Update: 2022-05-20
    Author: Zhiyuan Tao
"""

import tkinter
import numpy as np
import pandas as pd
from tkinter import *
from tkinter import ttk

## 定义主页界面 
class Home(object):

    # 读取管理员csv文件
    def get_manager_csv():
        user_csv = pd.read_csv(r'./dataset/manager.csv', encoding='GBK')
        return user_csv
    
    # 读取用户信息csv文件
    def get_user_csv():
        user_csv = pd.read_csv(r'./dataset/user.csv', encoding='GBK')
        return user_csv
   
    ## 跳转到指定功能
    def go_First(self):     # 进入功能一：
        self.root.destroy() # 界面销毁
        First()    # 跳转到指定功能函数，这里是违法查询系统函数（这应该叫做 类 吧？迷，迷，迷 ）
    def go_Second(self):    # 进入功能二：
        self.root.destroy()        
        Second()
    def go_Third(self):     # 进入功能三：
        self.root.destroy()
        Third()
    def go_Fourth(self):    # 进入功能四：
        self.root.destroy()
        Fourth()
    
    def __init__(self):
        global width,height, screenwidth, screenheight
        self.root = Tk()
        self.root.title('车辆违章查询系统') #设置窗口标题
        width  = 500
        height = 250
        screenwidth  = (self.root.winfo_screenwidth() -width) /2    # 获取屏幕的宽度，除 2 是表示在1/2 宽度处显示
        screenheight = (self.root.winfo_screenheight()-height)/2    # # 获取屏幕的高度，除 2 是表示在1/2 高度处显示
        self.root.geometry('%dx%d+%d+%d'%(width, height, screenwidth, screenheight))
        # self.root.geometry('400x250')
        Label(self.root, text='信息查询').place(x=20,y=10)
        ## 四个功能按钮分别关联 四个函数(函数?/类?迷？😅)，并跳转到指定功能界面
        Button(self.root, text='机动车违法查询', command=self.go_First, width=20, height=2).place(x=175,y=30)
        Button(self.root, text='驾驶证计分查询', command=self.go_Second, width=20, height=2).place(x=175,y=90)
        Button(self.root, text='报废车辆查询', command=self.go_Third, width=20, height=2).place(x=175,y=150)
        
        Button(self.root, text='管理员登录', command=self.go_Fourth).place(x=410, y=200)
        self.root.mainloop()
        
## 功能一：违法查询功能
class First(object):
    def go_Home(self):
        self.root.destroy()
        Home()
        
    def go_Check(self):
        self.root_1 = Tk()
        self.root_1.geometry('%dx%d+%d+%d'%(width, height, screenwidth, screenheight))
        new_1 = s_1.get()    # 号牌
        new_2 = s_2.get()    # 发动机号后六位
        new_3 = com_1.get()    # 车型
        new_4 = com_2.get()    # 省份
        print(new_1,new_2, new_3, new_4)
        
        user_info = get_user_csv()    # 调用函数
        for user in user_info['号牌']:
            if new_1 == str(user):
                # print('查询成功')
                user_info = user_info[['姓名','违法行为']]
            else:
                # print(' 查询失败\n','根据您提交的信息，无法查询到违法记录。')
                user_info = '请核实您提交的信息是否准确'
                
        Label(self.root_1, text=user_info).pack()
        Button(self.root_1, text='👉返回👈', command=self.root_1.destroy).pack()
        self.root_1.mainloop()
             
    def __init__(self):
        global s_1,s_2,com_1,com_2
        
        self.root = Tk()
        self.root.geometry('%dx%d+%d+%d'%(width, height, screenwidth, screenheight))
        self.root.title('机动车违法查询')
        Label(self.root,text='机动车违法查询').pack()
        com_1 = ttk.Combobox(self.root);  com_1.place(x=170,y=35)
        com_2 = ttk.Combobox(self.root, width=3);  com_2.place(x=170,y=70)
        com_1['values'] = ('大型汽车','小型汽车','大型新能源汽车','小型新能源汽车','使馆汽车','领馆汽车','境外汽车','外籍汽车','普通摩托车','轻便摩托车','使馆摩托车','领馆摩托车','境外摩托车','外籍摩托车','低速车','拖拉机','挂车','教练汽车','教练摩托车','试验汽车')
        com_2['values'] = ('京','津','沪','渝','蒙','新','藏','宁','桂','港','澳','黑','吉','辽','晋','冀','青','鲁','豫','苏','皖','浙','闽','赣','湘','鄂','粤','琼','甘','陕','贵','云','川')
        com_1.current(0)    # 设置默认选项
        com_2.current(0)    # 设置默认选项

        s_1 = StringVar()
        s_2 = StringVar()
        entry_1 = Entry(self.root, textvariable=s_1, width=15);  entry_1.place(x=225,y=70);
        s_1.set('请输入号牌号码')
        entry_2 = Entry(self.root, textvariable=s_2, width=23);  entry_2.place(x=170,y=105);
        s_2.set('请输入发动机号后六位')
       
        # Label(self.root, text='This is show!!!').pack()
        Button(self.root, text='👉查询👈', command=self.go_Check, bg='blue',fg='white', width=10, height=1).place(x=170, y=140)
        Button(self.root, text='👉返回👈', command=self.go_Home, width=10, height=1).place(x=255, y=140)
        self.root.mainloop()
        
## 功能二：驾驶证计分查询功能   
class Second(object):
    def go_Home(self):
        self.root.destroy()
        Home()
    
    def go_Check(self):
        self.root_2 = Tk()
        self.root_2.title('返回')
        self.root_2.geometry('%dx%d+%d+%d'%(width, height, screenwidth, screenheight))
        new_1 = s_3.get()    # 驾驶证号码
        print(new_1)
        new_2 = s_4.get()    # 发动机号后六位  
        
        user_info = get_user_csv()    # 调用函数
        for user in user_info['驾驶证号']:
            if new_1 == str(user):
                user_info = user_info[['姓名', '号牌', '驾驶证号', '当前分数']]
            else:
                user_info = '请核实您提交的信息是否准确'
                
        Label(self.root_2, text=user_info).pack()
        Button(self.root_2, text='👉返回👈', command=self.root_2.destroy).pack()
        self.root_2.mainloop()
        
    def __init__(self):
        global s_3,s_4
        self.root = Tk()
        self.root.geometry('%dx%d+%d+%d'%(width, height, screenwidth, screenheight))
        self.root.title('驾驶证计分查询')
        Label(self.root, text='驾驶证计分查询').pack()
        
        s_3 = StringVar()
        s_4 = StringVar()
        s_3.set('请输入驾驶证号码')
        s_4.set('请输入驾驶证档案编号')
        Entry(self.root, textvariable=s_3, width=23).place(x=175,y=35)
        Entry(self.root, textvariable=s_4, width=23).place(x=175,y=75)

        Button(self.root, text='👉查询👈',command=self.go_Check, bg='blue',fg='white', width=20).place(x=180,y=135)
        Button(self.root, text='👉返回👈', command=self.go_Home, width=20).place(x=180,y=175)
        self.root.mainloop()
        
## 功能三：报废车辆查询功能       
class Third(object):
    def go_Home(self):
        self.root.destroy()
        Home()

    def go_Check(self):
        self.root_3 = Tk()
        self.root_3.title('报废车辆查询')
        self.root_3.geometry('%dx%d+%d+%d'%(width, height, screenwidth, screenheight))
        new_1 = s_5.get()    # 号牌
        new_2 = s_6.get()    # 发动机号后六位
        new_3 = com_3.get()    # 车型
        new_4 = com_4.get()    # 省份       
        
        user_info = get_user_csv()    # 调用函数
        for user in user_info['发动机号后六位']:
            if new_1 == str(user):
                user_info = user_info[['姓名', '报废年限']]
            else:
                user_info = '请核实您提交的信息是否准确'
                
        Label(self.root_3, text=user_info).pack()
        Button(self.root_3, text='👉返回👈', command=self.root_3.destroy).pack()
        self.root_3.mainloop()
        
    def __init__(self):
        global s_5,s_6,com_3,com_4
        
        self.root = Tk()
        self.root.title('报废车辆查询功能')
        self.root.geometry('%dx%d+%d+%d'%(width, height, screenwidth, screenheight))
        
        Label(self.root,text='报废车辆查询功能').pack()
        com_3 = ttk.Combobox(self.root);  com_3.place(x=170,y=35)
        com_4 = ttk.Combobox(self.root, width=3);  com_4.place(x=170,y=70)
        com_3['values'] = ('大型汽车','小型汽车','大型新能源汽车','小型新能源汽车','使馆汽车','领馆汽车','境外汽车','外籍汽车','普通摩托车','轻便摩托车','使馆摩托车','领馆摩托车','境外摩托车','外籍摩托车','低速车','拖拉机','挂车','教练汽车','教练摩托车','试验汽车')
        com_4['values'] = ('京','津','沪','渝','蒙','新','藏','宁','桂','港','澳','黑','吉','辽','晋','冀','青','鲁','豫','苏','皖','浙','闽','赣','湘','鄂','粤','琼','甘','陕','贵','云','川')
        com_3.current(0)
        com_4.current(0)

        s_5 = StringVar()
        s_6 = StringVar()
        Entry(self.root, textvariable=s_5, width=15).place(x=225,y=70);    s_5.set('请输入号牌号码')
        Entry(self.root, textvariable=s_6, width=23).place(x=170,y=105);    s_6.set('请输入发动机号后六位')        

        Button(self.root, text='👉查询👈',command=self.go_Check, bg='blue',fg='white', width=20).place(x=178,y=135)
        Button(self.root, text='👉返回👈', command=self.go_Home, width=20).place(x=178,y=175)
        self.root.mainloop()
    
## 功能四：管理员登录
class Fourth(object):
    def go_Home(self):
        self.root.destroy()
        Home()
        
    def go_Check(self):
        self.root_4 = Tk()
        self.root_4.title('登录信息')
        self.root_4.geometry('%dx%d+%d+%d'%(width, height, screenwidth, screenheight))
        
        accounts = account.get()    # 账户号
        passwords = password.get()    # 密码
        
        user_info = get_manager_csv()    # 调用函数
        for i in range(len(user_info)):
            if accounts == user_info.iloc[i]['账户名']:
                if passwords == user_info.iloc[i]['密码']:
                    msg = '登录成功'
                    break
                else:
                    msg = '密码错误! 请重新输入'
            else:
                msg = '账号不存在! 请联系管理员'

        Label(self.root_4, text=msg).pack()
        Button(self.root_4, text='👉返回👈', command=self.root_4.destroy).pack()
        self.root_4.mainloop()
      
    def __init__(self):
        global account,password
        self.root = Tk()
        self.root.title('管理员登录')
        self.root.geometry('%dx%d+%d+%d'%(width, height, screenwidth, screenheight))
        Label(self.root, text='管理员登录').pack
        
        account = StringVar()
        password = StringVar()
        Label(self.root, text='账号').place(x=150, y=50)
        Label(self.root, text='密码').place(x=150, y=100)
        Entry(self.root, textvariable=account, width=20).place(x=200,y=50)
        Entry(self.root, textvariable=password, width=20, show='*').place(x=200,y=100)
        
        Button(self.root, text='👉返回👈', command=self.go_Home, width=10).place(x=115,y=160)
        Button(self.root, text='👉登录👈', width=10, command=self.go_Check, bg='blue',fg='white').place(x=300,y=160)
        self.root.mainloop()

if __name__ == '__main__':
    Home()