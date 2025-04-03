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
        self.listRed=[]
        self.listBlue = []
        self.listYellow = []
        self.listGreen = []

        # Список отключённых карт из империума
        self.listOfDisabled = []

        # Загружаем список колод
        file = open('AddList.json')
        listOfAddons = json.load(file)
        file.close()
        

        # directory = ".\Images"
        # # Создаем пустой список
        # files = []

        # # Добавляем файлы в список
        # files += os.listdir(directory)


        # self.columsPlayers = 3

        # wid = 4 * self.columsPlayers * 25

        # Создаём окно
        self.root = tk.Tk()
        self.root.title("Dune Imperium Блокнот")

        # menu left
        self.menu_left = tk.Frame(self.root, bg="#f0f0f0")
        # Поле для режима игроков (4 или 6)
        self.menu_left_upper = tk.Frame(self.menu_left,   bg="red",)
        # Поле для 4 полей колод игроков
        self.menu_left_color = tk.Frame(self.menu_left,  )
        # self.menu_left_cards = tk.Frame(self.menu_left,  bg="orange")
        # Поле для кнопки удаления
        self.menu_left_Delete = tk.Frame(self.menu_left,  bg="blue")
        
        # Размещаем девые поля
        self.menu_left_upper.grid(column=0,row=0)
        self.menu_left_color.grid(column=0,row=1)
        self.menu_left_Delete.grid(column=0,row=2)

        # self.menu_left_upper.pack(side="top", fill="both", expand=True)
        # self.menu_left_lower.pack(side="top", fill="both", expand=True)

        # Добавляем кружки выбора количества игроков TODO: сделать для 6 игроков
        self.mode  = StringVar(value="play4") 
        self.play4 = tk.Radiobutton(self.menu_left_upper, text="4 игрока",  value="play4", variable=self.mode)
        self.play6 = tk.Radiobutton(self.menu_left_upper, text="6 игроков", value="play6", variable=self.mode)
        self.play4.grid(row = 0, column = 0)
        self.play6.grid(row = 0, column = 1)

        # Menu Colors. Поля цветов игроков       
        self.RED = tk.Frame(self.menu_left_color, bg="red", borderwidth=2)
        self.RED.grid(column=0,row=1)

        self.GREEN = tk.Frame(self.menu_left_color, bg="green",borderwidth=2)
        self.GREEN.grid(column=1,row=1)
 
        self.YELLOW = tk.Frame(self.menu_left_color, bg="yellow",borderwidth=2)
        self.YELLOW.grid(column=2,row=1)

        self.BLUE = tk.Frame(self.menu_left_color, bg="blue",borderwidth=2)
        self.BLUE.grid(column=3,row=1)

        # Кнопка удаления выбраной кнопки
        self.delete_all = tk.Button(self.menu_left_Delete,text = "Delete", command=self.DeleteCard)

        # Правая область вся
        self.right = tk.Frame(self.root, bg="#dfdfdf")
        # Строка с аддонами
        self.right_Addons = tk.Frame(self.right, bg="#dfdfdf")
        # Область с картами Империума
        self.righе_Imperium_Cards = tk.Frame(self.right, bg="blue")

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
        self.right.grid(row=0, column=1, sticky="ew")
        self.right_Addons.grid(row=0,column=0)
        self.righе_Imperium_Cards.grid(row=1,column=0)
        self.right_down_worm.grid(row=2,column=0)
        

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.listOfButtonsButt = []

        # Подготавливаем стартовые карты
        self.StartCards()
        # Рисуем Империум
        self.SmenaAddona()

        # Запускаем аддон
        # !!!!!!!!!!!!!!!!!!!
        # self.root.call('wm', 'attributes', '.', '-topmost', '1') 
        # self.root.call('wm', 'attributes', '.', '-topmost', False)

        
        self.root.mainloop()

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
                w = 35
                h = 49

                # w=50
                # h = 70

                img = Image.open(img_dir)

                img = img.resize((w,h))

                img = ImageTk.PhotoImage(img)
                
                button = tk.Button(self.righе_Imperium_Cards, image=img,width=w,height=h,bd=0,text=img_dir)
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
        directory = ".\Images\\S\\"
        files = []
        files += os.listdir(directory)
        n=0
        
        for f in files:
            img_dir = directory + f
            
            w=25
            h = 35
            
            img = Image.open(img_dir)
            img = img.resize((w,h))
            img = ImageTk.PhotoImage(img)
            
            r = n//2+1
            c = n%2
            
            button = tk.Button(self.RED, image=img,width=w,height=h,bd=0,bg='red')
            button.image = img
            button.bind('<Button-1>',self.SelectCardPlayer)
            self.listRed.append(button)

            button = tk.Button(self.GREEN, image=img,width=w,height=h,bd=0,bg = 'green')
            button.image = img
            button.bind('<Button-1>',self.SelectCardPlayer)
            self.listGreen.append(button)

            button = tk.Button(self.YELLOW, image=img,width=w,height=h,bd=0,bg='yellow')
            button.image = img
            button.bind('<Button-1>',self.SelectCardPlayer)
            self.listYellow.append(button)
            
            button = tk.Button(master=self.BLUE, image=img,width=w,height=h,bd=0,bg = 'blue')
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

    # Добавление карт из империума
    def AddCard(self,e):
        # Заранее перерисовываем карту
        w = e.widget
        wid =25
        h = 35
        img = Image.open( w['text'])
        img = img.resize((wid,h))
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
okno = Example()
