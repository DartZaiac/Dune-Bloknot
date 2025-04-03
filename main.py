import tkinter as tk
from tkinter import *
import json
import os
from PIL import ImageTk, Image

class Example:
    def __init__(self):

        self.curButt = ""

        self.listRed=[]
        self.listBlue = []
        self.listYellow = []
        self.listGreen = []

        self.listOfDisabled = []

        file = open('AddList.json')
        listOfAddons = json.load(file)
        file.close()
        
        directory = ".\Images"
        # Создаем пустой список
        files = []

        # Добавляем файлы в список
        files += os.listdir(directory)
        # print(files)


        self.columsPlayers = 3

        wid = 4 * self.columsPlayers * 25
        print(wid)
        wid4 = wid//2
        print(wid4)
        self.root = tk.Tk()
        self.root.title("Dune Imperium Блокнот")

        # menu left
        self.menu_left = tk.Frame(self.root, width= wid, bg="#f0f0f0")
        self.menu_left_upper = tk.Frame(self.menu_left,   bg="red",)
        self.menu_left_color = tk.Frame(self.menu_left,  bg="blue")
        self.menu_left_cards = tk.Frame(self.menu_left,  bg="orange")
        self.menu_left_Delete = tk.Frame(self.menu_left,  bg="blue")
        # self.test = tk.Label(self.menu_left_upper, text="test")
        # self.test.pack()

        self.menu_left_upper.grid(column=0,row=0)
        self.menu_left_color.grid(column=0,row=1)
        self.menu_left_cards.grid(column=0,row=2)
        self.menu_left_Delete.grid(column=0,row=3)
        # self.menu_left_upper.pack(side="top", fill="both", expand=True)
        # self.menu_left_lower.pack(side="top", fill="both", expand=True)

        self.mode  = StringVar(value="play4") 
        self.play4 = tk.Radiobutton(self.menu_left_upper, text="4 игрока",  value="play4", variable=self.mode)
        self.play6 = tk.Radiobutton(self.menu_left_upper, text="6 игроков", value="play6", variable=self.mode)
        self.play4.grid(row = 0, column = 0)
        self.play6.grid(row = 0, column = 1)

        

        

        # Menu Colors
        

        self.RED = tk.Frame(self.menu_left_color, bg="red", borderwidth=2)
        self.RED.grid(column=0,row=1)

        self.GREEN = tk.Frame(self.menu_left_color, bg="green",borderwidth=2)
        self.GREEN.grid(column=1,row=1)
 
        self.YELLOW = tk.Frame(self.menu_left_color, bg="yellow",borderwidth=2)
        self.YELLOW.grid(column=2,row=1)

        self.BLUE = tk.Frame(self.menu_left_color, bg="blue",borderwidth=2)
        self.BLUE.grid(column=3,row=1)

        # self.radioRed = tk.Radiobutton(self.RED,bg="red")
        # self.radioRed.grid(column=0,row=0,columnspan=2)

        # self.radioGreen = tk.Radiobutton(self.GREEN,bg="green")
        # self.radioGreen.grid(column=0,row=0,columnspan=2)

        # self.radioYellow = tk.Radiobutton(self.YELLOW,bg="yellow")
        # self.radioYellow.grid(column=0,row=0,columnspan=2)
        
        # self.radioBlue = tk.Radiobutton(self.BLUE,bg="blue")
        # self.radioBlue.grid(column=0,row=0,columnspan=2)
        
        # self.delete_red = tk.Button(self.RED,text = "Delete", command=self.DeleteCard)
        # self.delete_green = tk.Button(self.GREEN,text = "Delete", command=self.DeleteCard)
        # self.delete_yellow = tk.Button(self.YELLOW,text = "Delete", command=self.DeleteCard)
        self.delete_all = tk.Button(self.menu_left_Delete,text = "Delete", command=self.DeleteCard)

        

        # right area
        self.right = tk.Frame(self.root, bg="#dfdfdf")
        self.right_up = tk.Frame(self.right, bg="#dfdfdf")
        self.right_mid = tk.Frame(self.right, bg="blue")
        self.right_down_worm = tk.Frame(self.right, bg="red")

        # self.some_title = tk.Label(self.some_title_frame, text="some title", bg="#dfdfdf")
        # self.some_title.pack()
        self.Addon = StringVar(value="I")
        print(self.Addon.get())
        shortList=list(listOfAddons.keys())
        self.listOfAddonsRadio = []
        c=0
        for key in shortList[4:]:
            self.listOfAddonsRadio.append(tk.Radiobutton(self.right_up, text=key,  value=listOfAddons[key], variable=self.Addon, command=self.SmenaAddona, anchor="w"))
            # self.listOfAddonsRadio[c].grid(column = c, row=0)
            self.listOfAddonsRadio[c].pack(side = tk.LEFT,anchor="w")
            c+=1

        # self.canvas_area = tk.Canvas(self.root, width=500, height=400, background="#ffffff")
        # self.canvas_area.grid(row=1, column=1)

        # # status bar
        self.status_frame = tk.Frame(self.root)
        self.status = tk.Label(self.status_frame, text="this is the status bar")
        self.status.pack(fill="both", expand=True)

        self.menu_left.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.right.grid(row=0, column=1, sticky="ew")
        self.right_up.grid(row=0,column=0)
        
        self.right_mid.grid(row=1,column=0)
        self.right_down_worm.grid(row=2,column=0)
        # self.canvas_area.grid(row=1, column=1, sticky="nsew") 
        self.status_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.listOfButtonsButt = []
        self.StartCards()
        self.SmenaAddona()

        self.root.mainloop()

    def SmenaAddona(self):
        # print(self.Addon.get())
        for button in self.listOfButtonsButt:
            button.destroy()
     
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

        for f in files:
            if f[0]==self.Addon.get():
                self.listOfButtons[str(f[1])].append(str(f))
                
        # print(self.listOfButtons)
        self.listOfButtonsButt =[]
        for price in range(1,9):
            col=1
            for but in self.listOfButtons[str(price)]:
                img_dir = directory + but
                
                w = 35
                h = 49

                # w=50
                # h = 70

                img = Image.open(img_dir)

                img = img.resize((w,h))
                # img.save(img_dir)

                img = ImageTk.PhotoImage(img)
                
                button = tk.Button(self.right_mid, image=img,width=w,height=h,bd=0,text=img_dir)
                button.image = img
                self.listOfButtonsButt.append(button)
                if img_dir in self.listOfDisabled:
                    button['state'] = 'disabled'
                button.grid(row=price-1,column=col,ipadx=0,ipady=0,padx=0,pady=0)
                button.bind('<Button-1>',self.AddCard)
                col+=1

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
            button.grid(row=r,column=c)
            button.bind('<Button-1>',self.SelectCardPlayer)

            button = tk.Button(self.YELLOW, image=img,width=w,height=h,bd=0,bg='yellow')
            button.image = img
            button.grid(row=r,column=c)
            button.bind('<Button-1>',self.SelectCardPlayer)
            
            button = tk.Button(master=self.BLUE, image=img,width=w,height=h,bd=0,bg = 'blue')
            button.image = img
            button.grid(row=r,column=c)
            button.bind('<Button-1>',self.SelectCardPlayer)
            
            n+=1

        # self.delete_red.grid   (column=0, row=r+1, columnspan=2)
        # self.delete_green.grid (column=0, row=r+1, columnspan=2)
        # self.delete_yellow.grid(column=0, row=r+1, columnspan=2)
        self.Redraw(self.listRed)
        self.delete_all.grid  (column=0, row=0, columnspan=1)

    def AddCard(self,e):
        w = e.widget
        if w["state"] == "normal":
    # try:  
            if self.curButt['bg']=='red':
                w["state"] = "disabled"
                self.listOfDisabled.append(w["text"])
                # img = w.image
                # print(img)
                wid =25
                h = 35
                # img = ImageTk.getimage( imgTk )
                img = Image.open( w['text'])
                img = img.resize((wid,h))
                # img.save("123")
                img = ImageTk.PhotoImage(img)

                button = tk.Button(self.RED,width=wid,height=h,bd=0,image = img, bg='red')
                button.image = img

                button.bind('<Button-1>',self.SelectCardPlayer)
                
                self.listRed.append(button)
                print(self.listRed)
                self.Redraw(self.listRed)
    # except:
        print("somthing wrong")


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
    
    def SelectCardPlayer(self,e):
        # print(123)
        w = e.widget
        self.curButt = w

        # print(w.keys())
        # print(w["bg"])
        # print(w["state"])
        if w["state"] == "normal":
            w["state"] = "disabled"
        else:
            w["state"] = "normal"
        # print(self.RED.grid_slaves())
        
        
    def DeleteCard(self):
        self.listRed.remove(self.curButt)
        self.curButt.destroy()
        self.Redraw(self.listRed)
okno = Example()
