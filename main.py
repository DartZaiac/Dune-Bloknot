import tkinter as tk
from tkinter import *
import json
import os
from PIL import ImageTk, Image

class Example:
    def __init__(self):
        # Инициализация кнопки с помощью которой будем работать. Имено здесь будет храниться инфа, кому добавлять карты и какую удалять
        self.curButt = ""

        # Списки карт каждого игрока
        self.listEmperor = []
        self.listMuad = []
        self.listRed=[]
        self.listBlue = []
        self.listYellow = []
        self.listGreen = []

        self.wid = 72
        self.hey = 100

        # Список отключённых карт из империума
        self.listOfDisabled = []

        # Загружаем список колод
        file = open('AddList.json')
        listOfAddons = json.load(file)
        file.close()

        # Создаём окно
        self.root = tk.Tk()
        self.root.title("Dune Imperium Блокнот")



        # menu left
        self.menu_left = tk.Frame(self.root, bg="#f0f0f0")
        # Поле для режима игроков (4 или 6)
        self.menu_left_upper = tk.Frame(self.menu_left,   )
        # Поле для 4 полей колод игроков
        self.menu_left_color = tk.Frame(self.menu_left,  )

        # Поле для кнопки удаления
        self.menu_left_Delete = tk.Frame(self.menu_left,  bg="blue")

        # поле размеров
        self.menu_size = tk.Frame(self.root)
        
        # Размещаем левые поля
        self.menu_left_upper.grid(column=0,row=0)
        self.menu_left_color.grid(column=0,row=1)
        self.menu_left_Delete.grid(column=0,row=2)
        

        # Добавляем кружки выбора количества игроков
        self.AlwaysOnTop = IntVar(value=1)
        self.mode  = StringVar(value="play4") 
        self.play4 = tk.Radiobutton(self.menu_left_upper, text="4 игрока",  value="play4", variable=self.mode, command=self.ModeRadio)
        self.play6 = tk.Radiobutton(self.menu_left_upper, text="6 игроков", value="play6", variable=self.mode, command=self.ModeRadio)
        self.AlwaysOnTopCheck = tk.Checkbutton(self.menu_left_upper, text = "Alwats on Top",variable=self.AlwaysOnTop,command=self.AlwaysOnTopFunc)
        self.play4.grid(row = 1, column = 0)
        self.play6.grid(row = 1, column = 1)
        self.AlwaysOnTopCheck.grid(column=0,row=0,columnspan=2)

        # Menu Colors. Поля цветов игроков       
        self.RED = tk.Frame(self.menu_left_color, bg="red", borderwidth=2)
        self.RED.grid(column=0,row=1)

        self.EMPEROR = tk.Frame(self.menu_left_color, bg="white", borderwidth=2)
        self.EMPEROR.grid(column=1,row=1)

        self.GREEN = tk.Frame(self.menu_left_color, bg="green",borderwidth=2)
        self.GREEN.grid(column=2,row=1)
 
        self.YELLOW = tk.Frame(self.menu_left_color, bg="yellow",borderwidth=2)
        self.YELLOW.grid(column=3,row=1)

        self.MUAD = tk.Frame(self.menu_left_color, bg="teal", borderwidth=2)
        self.MUAD.grid(column=4,row=1)

        self.BLUE = tk.Frame(self.menu_left_color, bg="blue",borderwidth=2)
        self.BLUE.grid(column=5,row=1)

        # Кнопка удаления выбраной кнопки
        self.delete_all = tk.Button(self.menu_left_Delete,text = "Delete", command=self.DeleteCard)

        # Правая область вся
        self.right = tk.Frame(self.root, bg="#dfdfdf")
        # Строка с аддонами
        self.right_Addons = tk.Frame(self.right, bg="#dfdfdf")
        # Область с картами Империума
        self.righе_Imperium_Cards = tk.Frame(self.right, )

        # Область с Сёстрами/Червём/Свёрнутым пространством TODO доделать!
        self.right_down_worm = tk.Frame(self.right, bg="red")

        # Стартуем с Дюны Империи
        self.Addon = StringVar(value="I")
        shortList=list(listOfAddons.keys())
        self.listOfAddonsRadio = []
        c=0
        # Добавляем все Аддоны из json
        for key in shortList[4:]:
            self.listOfAddonsRadio.append(tk.Radiobutton(self.right_Addons, text=key,  value=listOfAddons[key], variable=self.Addon, command=self.SmenaAddona, anchor="w"))
            self.listOfAddonsRadio[c].pack(side = tk.LEFT,anchor="w")
            c+=1

        # Размещаем панели
        self.menu_left.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.menu_size.grid(row=2,column=0,columnspan=2)
        self.right.grid(row=0, column=1, sticky="ew")
        self.right_Addons.grid(row=0,column=0)
        self.righе_Imperium_Cards.grid(row=1,column=0)
        self.right_down_worm.grid(row=2,column=0)
        

        self.SizeMode  = StringVar(value="72x100")

        self.menu_size_radio72 = tk.Radiobutton(self.menu_size, text="72x100", value="72x100", variable=self.SizeMode, command=self.ChangeSize)
        self.menu_size_radio58 = tk.Radiobutton(self.menu_size, text="58x80" ,value="58x80", variable=self.SizeMode, command=self.ChangeSize)
        self.menu_size_radio51 = tk.Radiobutton(self.menu_size, text="51x70" ,value="51x70", variable=self.SizeMode, command=self.ChangeSize)
        self.menu_size_radio44 = tk.Radiobutton(self.menu_size, text="44x60" ,value="44x60", variable=self.SizeMode, command=self.ChangeSize)
        self.menu_size_radio37 = tk.Radiobutton(self.menu_size, text="37x50" ,value="37x50", variable=self.SizeMode, command=self.ChangeSize)
        self.menu_size_radio35 = tk.Radiobutton(self.menu_size, text="35x49" ,value="35x49", variable=self.SizeMode, command=self.ChangeSize)

        self.menu_size_radio72.grid(column=0,row=0)
        self.menu_size_radio58.grid(column=1,row=0)
        self.menu_size_radio51.grid(column=2,row=0)
        self.menu_size_radio44.grid(column=3,row=0)
        self.menu_size_radio37.grid(column=4,row=0)
        self.menu_size_radio35.grid(column=5,row=0)

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.listOfButtonsButt = []

        # Подготавливаем стартовые карты
        self.StartCards()
        # Рисуем Империум

        self.SmenaAddona()

        # Запускаем аддон
        # !!!!!!!!!!!!!!!!!!!
        self.root.call('wm', 'attributes', '.', '-topmost', '1') 
        
        self.root.mainloop()
    def ChangeSize(self):
        self.listOfDisabled = []
# "58x80"
# "51x70"
# "44x60"
# "37x50"
# "35x49"
        if self.SizeMode.get() == "72x100":
            self.wid=72
            self.hey=100
        else:
            self.wid = int(self.SizeMode.get()[0:2])
            self.hey = int(self.SizeMode.get()[3:])
        self.SmenaAddona()
        self.StartCards()
        # self.Redraw(self.listRed)
        # self.Redraw(self.listGreen)
        # self.Redraw(self.listYellow)
        # self.Redraw(self.listBlue)
        # self.Redraw(self.listMuad)
        # self.Redraw(self.listEmperor)
    def ModeRadio(self):
        if self.mode.get() == "play4":
            self.StartCards()
        else:
            self.StartCards()
    def AlwaysOnTopFunc(self):
        if self.AlwaysOnTop.get() == 1:
            self.root.call('wm', 'attributes', '.', '-topmost', '1') 
        else:
            self.root.call('wm', 'attributes', '.', '-topmost', False)
    def SmenaAddona(self):
        # Убираем ВСЕ кнопки Империума
        for button in self.listOfButtonsButt:
            button.destroy()
     
        # Готовим хранилища для размещения
        self.listOfButtons = {
            "1":[],
            "2":[],
            "3":[],
            "4":[],
            "5":[],
            "6":[],
            "7":[],
            "8":[],
        }
        directory = ".\Images\\"+self.Addon.get()+"\\"
        # Создаем пустой список
        files = []
        # Добавляем файлы в список
        files += os.listdir(directory)

        # Добавляем все пути до картинок в список картинок по ценам
        for f in files:
            # if f[0]==self.Addon.get():
                self.listOfButtons[str(f[1])].append(str(f))
                
        # Список самих кнопок
        self.listOfButtonsButt =[]
        for price in range(1,9):
            col=1
            for but in self.listOfButtons[str(price)]:
                img_dir = directory + but
                
                # Размер картинок
                # w = 35
                # h = 49

                # w=50
                # h = 70

                img = Image.open(img_dir)

                img = img.resize((self.wid,self.hey))

                img = ImageTk.PhotoImage(img)
                
                button = tk.Button(self.righе_Imperium_Cards, image=img,width=self.wid,height=self.hey,bd=0,text=img_dir)
                button.image = img
                self.listOfButtonsButt.append(button)
                # Помечаем карты, что отмечены отключением как отключённые
                if img_dir in self.listOfDisabled:
                    button['state'] = 'disabled'
                # Размещаем кнопку-карту
                button.grid(row=price-1,column=col,ipadx=0,ipady=0,padx=0,pady=0)
                button.bind('<Button-1>',self.AddCard)
                col+=1

    # Раздача игрокам стартовых карт
    def StartCards(self):
        for card in self.listGreen:
            card.destroy()
        for card in self.listRed:
            card.destroy()
        for card in self.listYellow:
            card.destroy()
        for card in self.listBlue:
            card.destroy()
        for card in self.listMuad:
            card.destroy()
        for card in self.listEmperor:
            card.destroy()
        self.listGreen = []
        self.listYellow = []
        self.listRed=[]
        self.listBlue = []
        self.listMuad = []
        self.listEmperor = []

        self.EMPEROR["width"]=1
        self.MUAD["width"]=1

        directory = ".\Images\\S\\"
        files = []
        files += os.listdir(directory)
        n=0
        
        for f in files:
            img_dir = directory + f
            
            # w=25
            # h = 35
            
            img = Image.open(img_dir)
            img = img.resize((self.wid,self.hey))
            img = ImageTk.PhotoImage(img)
            
            # r = n//2+1
            # c = n%2
            
            button = tk.Button(self.RED, image=img,width=self.wid,height=self.hey,bd=0,bg='red')
            button.image = img
            button.bind('<Button-1>',self.SelectCardPlayer)
            self.listRed.append(button)

            button = tk.Button(self.GREEN, image=img,width=self.wid,height=self.hey,bd=0,bg = 'green')
            button.image = img
            button.bind('<Button-1>',self.SelectCardPlayer)
            self.listGreen.append(button)

            button = tk.Button(self.YELLOW, image=img,width=self.wid,height=self.hey,bd=0,bg='yellow')
            button.image = img
            button.bind('<Button-1>',self.SelectCardPlayer)
            self.listYellow.append(button)
            
            button = tk.Button(master=self.BLUE, image=img,width=self.wid,height=self.hey,bd=0,bg = 'blue')
            button.image = img
            button.bind('<Button-1>',self.SelectCardPlayer)
            self.listBlue.append(button)
            
            n+=1
        # TODO Сделать раздачу 6 игрокам
        # if

        # отрисовка кнопок-карт игроков
        self.Redraw(self.listRed)
        self.Redraw(self.listGreen)
        self.Redraw(self.listYellow)
        self.Redraw(self.listBlue)
        # Отрисовка кнопки удаления
        self.delete_all.grid  (column=0, row=0, columnspan=1)

        if self.mode.get() == "play6":
            directoryE = ".\Images\\E\\"
            files = []
            files += os.listdir(directoryE)
            n=0
            for f in files:
                img_dir = directoryE + f
                # w=25
                # h = 35
                
                img = Image.open(img_dir)
                img = img.resize((self.wid, self.hey))
                img = ImageTk.PhotoImage(img)
                
                button = tk.Button(self.EMPEROR, image=img, width=self.wid, height=self.hey, bd=0, bg = 'white')
                button.image = img
                button.bind('<Button-1>',self.SelectCardPlayer)
                self.listEmperor.append(button)

            directoryM = ".\Images\\M\\"
            files = []
            files += os.listdir(directoryM)
            n=0
            for f in files:
                img_dir = directoryM + f
                
                # w=25
                # h = 35
                
                img = Image.open(img_dir)
                img = img.resize((self.wid, self.hey))
                img = ImageTk.PhotoImage(img)
                
                button = tk.Button(self.MUAD, image=img,width=self.wid,height=self.hey,bd=0,bg='teal')
                button.image = img
                button.bind('<Button-1>',self.SelectCardPlayer)
                self.listMuad.append(button)
            self.Redraw(self.listEmperor)
            self.Redraw(self.listMuad)
        


    # Добавление карт из империума
    def AddCard(self,e):
        # Заранее перерисовываем карту
        w = e.widget
        # wid =25
        # h = 35
        wid = self.wid
        h = self.hey
        
        img = Image.open( w['text'])
        img.resize((self.wid,self.hey))
        img = ImageTk.PhotoImage(img)
        # Если карта-кнопка доступна
        if w["state"] == "normal":
            try:  
                # Если последняя кнопка карта использованая на игроке - это красная 
                if self.curButt['bg']=='red':
                    # Деактивируем кнопку
                    w["state"] = "disabled"
                    # Добавляем карту в список неактивных
                    self.listOfDisabled.append(w["text"])
                    # Добавляем кнопку 
                    button = tk.Button(self.RED,width=wid,height=h,bd=0,image = img, bg='red')
                    button.image = img
                    button.bind('<Button-1>',self.SelectCardPlayer)
                    self.listRed.append(button)
                    # перерисовываем красныую колоду
                    self.Redraw(self.listRed)
                elif self.curButt['bg']=='green':
                    w["state"] = "disabled"
                    self.listOfDisabled.append(w["text"])
                    button = tk.Button(self.GREEN,width=wid,height=h,bd=0,image = img, bg='green')
                    button.image = img
                    button.bind('<Button-1>',self.SelectCardPlayer)
                    self.listGreen.append(button)
                    self.Redraw(self.listGreen)
                elif self.curButt['bg']=='yellow':
                    w["state"] = "disabled"
                    self.listOfDisabled.append(w["text"])
                    button = tk.Button(self.YELLOW,width=wid,height=h,bd=0,image = img, bg='yellow')
                    button.image = img
                    button.bind('<Button-1>', self.SelectCardPlayer)
                    self.listYellow.append(button)
                    self.Redraw(self.listYellow)
                elif self.curButt['bg']=='blue':
                    w["state"] = "disabled"
                    self.listOfDisabled.append(w["text"])
                    button = tk.Button(self.BLUE,width=wid,height=h,bd=0,image = img, bg='blue')
                    button.image = img
                    button.bind('<Button-1>',self.SelectCardPlayer)
                    self.listBlue.append(button)
                    self.Redraw(self.listBlue)
                elif self.curButt['bg']=='teal':
                    w["state"] = "disabled"
                    self.listOfDisabled.append(w["text"])
                    button = tk.Button(self.MUAD,width=wid,height=h,bd=0,image = img, bg='teal')
                    button.image = img
                    button.bind('<Button-1>',self.SelectCardPlayer)
                    self.listMuad.append(button)
                    self.Redraw(self.listMuad)
                elif self.curButt['bg']=='white':
                    w["state"] = "disabled"
                    self.listOfDisabled.append(w["text"])
                    button = tk.Button(self.EMPEROR,width=wid,height=h,bd=0,image = img, bg='white')
                    button.image = img
                    button.bind('<Button-1>',self.SelectCardPlayer)
                    self.listEmperor.append(button)
                    self.Redraw(self.listEmperor)
            except:
                print("somthing wrong")
                

    # Перерисовываем карты
    def Redraw(self, listColor):
        n=0
        for card in listColor:
            r = n//2+1
            c = n%2
            card.grid(row=r,column=c)
            n+=1
        r = n//2+1
        c = n%2
        listColor[0].grid(row=r,column=c)
        listColor[0].grid(row=1,column=0)
        pass
    
    # Если карту в колоде игрока нажали, она сереет или наоборот светлеет
    def SelectCardPlayer(self,e):
        w = e.widget
        self.curButt = w
        if w["state"] == "normal":
            w["state"] = "disabled"
        else:
            w["state"] = "normal"
        
    # Удаление карты
    def DeleteCard(self):
        if self.curButt['bg']=='red':
            self.listRed.remove(self.curButt)
            self.curButt.destroy()
            self.Redraw(self.listRed)
        elif self.curButt['bg']=='green':
            self.listGreen.remove(self.curButt)
            self.curButt.destroy()
            self.Redraw(self.listGreen)
        elif self.curButt['bg']=='yellow':
            self.listYellow.remove(self.curButt)
            self.curButt.destroy()
            self.Redraw(self.listYellow)
        elif self.curButt['bg']=='blue':
            self.listBlue.remove(self.curButt)
            self.curButt.destroy()
            self.Redraw(self.listBlue)
        elif self.curButt['bg']=='white':
            self.listEmperor.remove(self.curButt)
            self.curButt.destroy()
            self.Redraw(self.listEmperor)
        elif self.curButt['bg']=='teal':
            self.listMuad.remove(self.curButt)
            self.curButt.destroy()
            self.Redraw(self.listMuad)
okno = Example()
