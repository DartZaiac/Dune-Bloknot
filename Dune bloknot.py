import tkinter as tk
from tkinter import *
import json
import os
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo, askyesno
import time

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

        # Список отключённых карт из империума
        self.listOfDisabled = []

        # Загружаем список колод
        file = open('AddList.json')
        listOfAddons = json.load(file)
        file.close()

        # Спрашиваем про 11ю карту
        self.click()

        # Создаём окно
        self.root = tk.Tk()
        
        self.root.title("Dune Imperium Блокнот")
        # self.root.iconbitmap(".\Korzina\Iconka1.ico")


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
        self.Krasit = IntVar(value=0)
        self.mode  = StringVar(value="play4") 
        self.play4 = tk.Radiobutton(self.menu_left_upper, text="4 players",  value="play4", variable=self.mode, command=self.ModeRadio)
        self.play6 = tk.Radiobutton(self.menu_left_upper, text="6 players", value="play6", variable=self.mode, command=self.ModeRadio)
        self.AlwaysOnTopCheck = tk.Checkbutton(self.menu_left_upper, text = "Alwats on Top",variable=self.AlwaysOnTop,command=self.AlwaysOnTopFunc)
        self.play4.grid(row = 1, column = 0)
        self.play6.grid(row = 1, column = 1)
        self.AlwaysOnTopCheck.grid(column=0,row=0,columnspan=1)
        self.Pokras = tk.Checkbutton(self.menu_left_upper, text = "Красить карты?",variable=self.Krasit,)
        self.Pokras.grid(column=1,row=0,columnspan=1)


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
        self.delete_all = tk.Button(self.menu_left_Delete,text = "Delete", )
        self.delete_all.bind('<Button-1>',self.DeleteCard)

        # Правая область вся
        self.right = tk.Frame(self.root, bg="#dfdfdf")
        # Строка с аддонами
        self.right_Addons = tk.Frame(self.right, bg="#dfdfdf")
        # Область с картами Империума
        self.right_Imperium_Cards = tk.Frame(self.right, )

        # Область с Сёстрами/Червём/Свёрнутым пространством TODO доделать!
        self.right_down_worm = tk.Frame(self.right, )

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
        self.menu_size.grid(row=2,column=0,columnspan=1)
        self.right.grid(row=0, column=1, sticky="ew")
        self.right_Addons.grid(row=0,column=0)
        self.right_Imperium_Cards.grid(row=1,column=0)
        self.right_down_worm.grid(row=2,column=0,sticky="ew")
        

        self.wid = 51
        self.hey = 70

        self.SizeMode  = StringVar(value="51x70")

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

        self.LabelArrakin = tk.Label(self.right_down_worm,text="8")
        self.LabelFold = tk.Label(self.right_down_worm,text = "6")
        self.LabelSMF = tk.Label(self.right_down_worm,text = "10")
        
        self.LabelArrakin.grid(row=0,column=0,ipadx=0,ipady=0,padx=0,pady=0)
        self.LabelFold.grid(row=0,column=2,ipadx=0,ipady=0,padx=0,pady=0)
        self.LabelSMF.grid(row=0,column=4,ipadx=0,ipady=0,padx=0,pady=0)



        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.listOfButtonsButt = []

        
        self.LoadButt = tk.Button(self.menu_left_upper, text = "UNDO", command=self.Loading)
        self.LoadButt.grid(row=0,column=2)
        self.listSAVE=[]

        img = Image.new("RGB",(1,1),"blue")
        img = img.resize((self.wid*3,self.hey*3))
        img = ImageTk.PhotoImage(img)
        self.DrawCard = tk.Label(self.right_Imperium_Cards,image=img)
        self.DrawCard.image = img
        # self.DrawCard.grid(row=5,column=15,columnspan=3,rowspan=3,)

        # Подготавливаем стартовые карты
        self.StartCards()
        # Рисуем Империум

        self.SmenaAddona()

        # Запускаем аддон
        # !!!!!!!!!!!!!!!!!!!
        self.root.call('wm', 'attributes', '.', '-topmost', '1') 
        self.Saving()
        self.root.mainloop()

    def Delete(self,e):
        try:
            w = e.widget
        except:
            w=e
        self.Saving()
        self.listOfDisabled.append(w['text'])
        w.destroy()

    def click(self): 
        result =  askyesno(title="Is it Epic mode?", message="Do you want add \"Control the Spice\" in players decks?")
        if result: 
            self.Epic=True
        else: 
            self.Epic=False

    def Saving(self):
        self.listSAVE.append((
                self.listRed[:],
                self.listGreen[:],
                self.listYellow[:],
                self.listBlue[:],
                self.listEmperor[:],
                self.listMuad[:],
                self.listOfDisabled[:],
                self.LabelArrakin["text"],
                self.LabelFold["text"],
                self.LabelSMF["text"],
            ))

    def Loading(self):
        if len(self.listSAVE)>1:
            for pack in self.listBlue:
                pack.grid_forget()
            for pack in self.listYellow:
                pack.grid_forget()
            for pack in self.listGreen:
                pack.grid_forget()
            for pack in self.listRed:
                pack.grid_forget()
            for pack in self.listEmperor:
                pack.grid_forget()
            for pack in self.listMuad:
                pack.grid_forget()
            self.listRed =              self.listSAVE[-1][0][:]
            self.listGreen =            self.listSAVE[-1][1][:]
            self.listYellow =           self.listSAVE[-1][2][:]
            self.listBlue =             self.listSAVE[-1][3][:]
            self.listEmperor =          self.listSAVE[-1][4][:]
            self.listMuad =             self.listSAVE[-1][5][:]
            self.listOfDisabled =       self.listSAVE[-1][6][:]
            self.LabelArrakin["text"] = self.listSAVE[-1][7][:]
            self.LabelFold["text"] =    self.listSAVE[-1][8][:]
            self.LabelSMF["text"] =     self.listSAVE[-1][9][:]
            self.listSAVE.pop(-1)

            self.SmenaAddona()
            self.Redraw(self.listRed)
            self.Redraw(self.listGreen)
            self.Redraw(self.listYellow)
            self.Redraw(self.listBlue)
            if self.mode.get() == "play6":
                self.Redraw(self.listEmperor)
                self.Redraw(self.listMuad)

    def Arrakin(self):
        if int(self.LabelArrakin["text"])>0:
            if self.AddCard(self.CardArrakin):
                # self.Saving()
                self.LabelArrakin["text"] = str(int(self.LabelArrakin["text"])-1)
                # self.CardArrakin["state"]="normal"

    def Fold(self):
        if int(self.LabelFold["text"])>0:
            if self.AddCard(self.CardFold):
                # self.Saving()
                self.LabelFold["text"] = str(int(self.LabelFold["text"])-1)
                # self.CardFold["state"]="normal"
    def SMF(self):
        if int(self.LabelSMF["text"])>0:
            if self.AddCard(self.CardSMF):
                # self.Saving()
                self.LabelSMF["text"] = str(int(self.LabelSMF["text"])-1)
                # self.CardSMF["state"]="normal"
    
    def ChangeSize(self):
        self.Saving()
        # self.Saving()
        # self.listOfDisabled = []
        if self.SizeMode.get() == "72x100":
            self.wid=72
            self.hey=100
        else:
            self.wid = int(self.SizeMode.get()[0:2])
            self.hey = int(self.SizeMode.get()[3:])
        self.CardArrakin.destroy()
        self.CardFold.destroy()
        self.CardSMF.destroy()
        self.Loading()

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
        directory = ".\\Images\\"+self.Addon.get()+"\\"
        # Создаем пустой список
        files = []
        # Добавляем файлы в список
        files += os.listdir(directory)

        # Добавляем все пути до картинок в список картинок по ценам
        for f in files:
            # if f[0]==self.Addon.get():
                self.listOfButtons[str(f[1])].append(str(f))

        maxi = max([len(self.listOfButtons[str(6)]),len(self.listOfButtons[str(7)]),len(self.listOfButtons[str(8)])])
        
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

                if img_dir not in self.listOfDisabled: 
                # and self.Krasit.get() == 1:
                    # button['state'] = 'disabled'
                    img = Image.open(img_dir)
                    img = img.resize((self.wid,self.hey))
                    img = ImageTk.PhotoImage(img)
                    button = tk.Button(self.right_Imperium_Cards, image=img,width=self.wid,height=self.hey,bd=0,text=img_dir)
                    button.image = img
                    self.listOfButtonsButt.append(button)
                    # Помечаем карты, что отмечены отключением как отключённые
                    # Размещаем кнопку-карту
                    button.grid(row=price-1,column=col,ipadx=0,ipady=0,padx=0,pady=0)
                    button.bind('<Button-1>',self.AddCard)
                    button.bind('<Button-3>',self.Delete)
                    button.bind('<Enter>', self.entered)
                                
                    col+=1

        try:
            # self.CardArrakin.destroy()        
            # self.CardFold.destroy()
            # self.CardSMF.destroy()
            pass
        except:
            pass
        img = Image.open(".\\Images\\W\\Arrakin.png")
        img = img.resize((self.wid,self.hey))
        img = ImageTk.PhotoImage(img)
        self.CardArrakin = tk.Button(self.right_down_worm,width=self.wid,height=self.hey,bd=0,image = img,command=self.Arrakin, text = ".\\Images\\W\\Arrakin.png")
        self.CardArrakin.image = img
        self.CardArrakin.grid(column=1,row=0)
        self.CardArrakin.bind("<Enter>", self.entered)

        img = Image.open(".\\Images\\W\\Fold.png")
        img = img.resize((self.wid,self.hey))
        img = ImageTk.PhotoImage(img)
        self.CardFold = tk.Button(self.right_down_worm,width=self.wid,height=self.hey,bd=0,image = img, text=".\\Images\\W\\Fold.png",command=self.Fold)
        self.CardFold.image = img
        self.CardFold.grid(column=3,row=0)
        self.CardFold.bind("<Enter>", self.entered)

        img = Image.open(".\\Images\\W\\Worm.png")
        img = img.resize((self.wid,self.hey))
        img = ImageTk.PhotoImage(img)
        self.CardSMF = tk.Button(self.right_down_worm,width=self.wid,height=self.hey,bd=0,image = img, text = ".\\Images\\W\\Worm.png",command=self.SMF)
        self.CardSMF.image = img
        self.CardSMF.grid(column=5,row=0)
        self.CardSMF.bind("<Enter>", self.entered)

        self.DrawCard.grid(row=5,column= maxi+2,columnspan=3,rowspan=3,)
        
    def entered(self,e):
        try:
            w=e.widget
        except:
            w=e
        time.sleep(0.01)
        img = Image.open(w['text'])
        img = img.resize((self.wid*3,self.hey*3))
        img = ImageTk.PhotoImage(img)
        self.DrawCard['image'] = img
        self.DrawCard.image = img
        # self.root.config(cursor="plus")
        # print("enter")
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

        directory = ".\\Images\\S\\"
        files = []
        files += os.listdir(directory)
        n=0
        
        for f in files:
            img_dir = directory + f
            if "Epic" in img_dir and not self.Epic:
                continue
            img = Image.open(img_dir)
            if "zGran" not in img_dir:
                img = img.resize((self.wid,self.hey))
                img = ImageTk.PhotoImage(img)
                button = tk.Button(self.RED, image=img,width=self.wid,height=self.hey,bd=0,bg='red',text = img_dir)
                button.image = img
                button.bind('<Button-1>',self.SelectCardPlayer)
                button.bind('<Enter>', self.entered)
                button.bind('<Button-3>',self.DeleteCard)
                self.listRed.append(button)

                button = tk.Button(self.GREEN, image=img,width=self.wid,height=self.hey,bd=0,bg = 'green',text = img_dir)
                button.image = img
                button.bind('<Button-1>',self.SelectCardPlayer)
                button.bind('<Enter>', self.entered)
                button.bind('<Button-3>',self.DeleteCard)
                self.listGreen.append(button)

                button = tk.Button(self.YELLOW, image=img,width=self.wid,height=self.hey,bd=0,bg='yellow',text = img_dir)
                button.image = img
                button.bind('<Button-1>',self.SelectCardPlayer)
                button.bind('<Enter>', self.entered)
                button.bind('<Button-3>',self.DeleteCard)
                self.listYellow.append(button)
                
                button = tk.Button(master=self.BLUE, image=img,width=self.wid,height=self.hey,bd=0,bg = 'blue',text = img_dir)
                button.image = img
                button.bind('<Button-1>',self.SelectCardPlayer)
                button.bind('<Enter>', self.entered)
                button.bind('<Button-3>',self.DeleteCard)
                self.listBlue.append(button)
                
                n+=1
            
        self.height =20
        
        
        img = Image.new("RGB",(1,1),"red")
        img = ImageTk.PhotoImage(img)
        label = tk.Label(self.RED, image=img,width=self.wid*2, height=self.height, text = "zGran", bg="red")
        label.image = img
        self.listRed.append(label)

        img = Image.new("RGB",(1,1),"green")
        img = ImageTk.PhotoImage(img)
        label = tk.Label(self.GREEN, image=img,width=self.wid*2, height=self.height, text = "zGran", bg="green")
        label.image = img
        self.listGreen.append(label)

        img = Image.new("RGB",(1,1),"yellow")
        img = ImageTk.PhotoImage(img)
        label = tk.Label(self.YELLOW, image=img,width=self.wid*2, height=self.height, text = "zGran",bg='yellow')
        label.image = img
        self.listYellow.append(label)


        img = Image.new("RGB",(1,1),"blue")
        img = ImageTk.PhotoImage(img)
        label = tk.Label(self.BLUE, image=img,width=self.wid*2, height=self.height, text = "zGran",bg='blue')
        label.image = img
        self.listBlue.append(label)


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
            directoryE = ".\\Images\\E\\"
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
                
                button = tk.Button(self.EMPEROR, image=img, width=self.wid, height=self.hey, bd=0, bg = 'white', text = img_dir)
                button.image = img
                button.bind('<Button-1>',self.SelectCardPlayer)
                button.bind('<Enter>', self.entered)
                button.bind('<Button-3>',self.DeleteCard)
                self.listEmperor.append(button)
            
            img = Image.new("RGB",(1,1),"white")
            img = ImageTk.PhotoImage(img)
            label = tk.Label(self.EMPEROR, image=img,width=self.wid*2, height=self.hey, text = "zGran", bg='white')
            label.image = img
            self.listEmperor.append(label)
            self.Redraw(self.listEmperor)


            directoryM = ".\\Images\\M\\"
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
                
                button = tk.Button(self.MUAD, image=img,width=self.wid,height=self.hey,bd=0,bg='teal', text = img_dir)
                button.image = img
                button.bind('<Button-1>',self.SelectCardPlayer)
                button.bind('<Enter>', self.entered)
                button.bind('<Button-3>',self.DeleteCard)
                self.listMuad.append(button)

            img = Image.new("RGB",(1,1),"teal")
            img = ImageTk.PhotoImage(img)
            label = tk.Label(self.MUAD, image=img,width=self.wid*2, height=self.hey, text = "zGran", bg='teal')
            label.image = img
            self.listMuad.append(label)
            self.Redraw(self.listMuad)
        


    # Добавление карт из империума
    def AddCard(self,e):
        self.Saving()
        try:
            # Заранее перерисовываем карту
            w = e.widget
        except:
            w=e
        # wid =25
        # h = 35
        img = Image.open( w['text'])
        img = img.resize((self.wid, self.hey))
        img = ImageTk.PhotoImage(img)

        field=0
        colorList = []
        bg=''
        # Если карта-кнопка доступна
        if w["state"] == "normal":
            try:  
                # Если последняя кнопка карта использованая на игроке - это красная 
                if self.curButt['bg']=='red':
                    field = self.RED
                    colorList=self.listRed
                    bg = 'red'
                elif self.curButt['bg']=='green':
                    field = self.GREEN
                    colorList=self.listGreen
                    bg = 'green'
                elif self.curButt['bg']=='yellow':
                    field = self.YELLOW
                    colorList=self.listYellow
                    bg = 'yellow'
                elif self.curButt['bg']=='blue':
                    field = self.BLUE
                    colorList=self.listBlue
                    bg = 'blue'
                elif self.curButt['bg']=='teal':
                    field = self.MUAD
                    colorList=self.listMuad
                    bg = 'teal'
                elif self.curButt['bg']=='white':
                    field = self.EMPEROR
                    colorList=self.listEmperor
                    bg = 'white'
                # Добавляем карту в список неактивных
                self.listOfDisabled.append(w["text"])
                # if self.Krasit.get() == 1:
                #     w["state"] = "disabled"
                # Добавляем кнопку 
                button = tk.Button(field, width=self.wid, height=self.hey,bd=0, image = img, bg=bg, text = w["text"])
                button.image = img
                button.bind('<Button-1>',self.SelectCardPlayer)
                button.bind('<Enter>', self.entered)
                button.bind('<Button-3>',self.DeleteCard)
                colorList.append(button)
                # перерисовываем красныую колоду
                if "Fold" not in w['text'] and "Worm" not in w['text'] and "Arrakin" not in w['text']:
                    w.destroy()
                self.Redraw(colorList)
                return 1
            except:
                print("somthing wrong")
                return 0
                

    # Перерисовываем карты
    def Redraw(self, listColor):
        n=0
        flagEndS = 0
        
        for card in listColor:
            # card.destroy()
            r = n//2+1+flagEndS
            c = n%2
            if card['width'] != self.wid:
                if card['text']!='zGran':
                    img = Image.open(card['text'])
                    img = img.resize((self.wid,self.hey))
                    img = ImageTk.PhotoImage(img)
                    card['image'] = img
                    card.image = img
                card['width'] = self.wid
                card['height'] = self.hey
            card.grid(row=r,column=c)
            if "zGran" in card["text"] and flagEndS==0:
                # r+=1
                flagEndS=2
                n=(n)//2*2-1
                card['height'] = self.height
                card.grid(column=0,row=r+1,columnspan=2)
            else:
                pass
            n+=1
        listColor[0].grid(row=r,column=c)
        listColor[0].grid(row=1,column=0)
        pass
    
    # Если карту в колоде игрока нажали, она сереет или наоборот светлеет
    def SelectCardPlayer(self,e):
        w = e.widget
        self.curButt = w
        if self.Krasit.get() == 1:
            if w["state"] == "normal":
                w["state"] = "disabled"
            else:
                w["state"] = "normal"
        
    # Удаление карты
    def DeleteCard(self,e):
        try:
            self.curButt = e.widget
        except:
            self.curButt = e
        self.Saving()
        if self.curButt['bg']=='red':
            self.listRed.remove(self.curButt)
            self.Redraw(self.listRed)
        elif self.curButt['bg']=='green':
            self.listGreen.remove(self.curButt)
            # self.curButt.destroy()
            self.Redraw(self.listGreen)
        elif self.curButt['bg']=='yellow':
            self.listYellow.remove(self.curButt)
            # self.curButt.destroy()
            self.Redraw(self.listYellow)
        elif self.curButt['bg']=='blue':
            self.listBlue.remove(self.curButt)
            # self.curButt.destroy()
            self.Redraw(self.listBlue)
        elif self.curButt['bg']=='white':
            self.listEmperor.remove(self.curButt)
            # self.curButt.destroy()
            self.Redraw(self.listEmperor)
        elif self.curButt['bg']=='teal':
            self.listMuad.remove(self.curButt)
            # self.curButt.destroy()
            self.Redraw(self.listMuad)
        
        if self.curButt["text"] == ".\\Images\\W\\Arrakin.png":
            self.LabelArrakin["text"] = str(int(self.LabelArrakin["text"])+1)
        elif self.curButt["text"] == ".\\Images\\W\\Worm.png":
            self.LabelSMF["text"] = str(int(self.LabelSMF["text"])+1)
        elif self.curButt["text"] == ".\\Images\\W\\Fold.png":
            self.LabelFold["text"] = str(int(self.LabelFold["text"])+1)
        self.curButt.grid_forget()
okno = Example()
