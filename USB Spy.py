from tkinter import *
from tkinter import font
from tkinter import messagebox
import keyboard
from tkinter import filedialog
from DetectingDrive import UsbDetection
from distutils.dir_util import copy_tree
import os

status = "shown"
folder_location = "C:/USB Spy"
fromDirectory = ""
copied = 0

class UsbSpy:
    def __init__(self):
        global copied, status, folder_location
        copied = 0
        status = "shown"
        folder_location = "C:/USB Spy"
        self.root = Tk()
        self.root.title("USB Spy")
        self.root.geometry("320x350")
        self.root.resizable(0,0)
        self.root['bg'] = "white"
        self.myHotKey = 'ctrl+alt+h'
        self.key = 'H'
        #..........IMAGE VARIABLES...................
        self.img_Spy = PhotoImage(file = r"C:\Users\manik\Desktop\USB Spy\Images\Final Spy.png")
        self.img_RedDot = PhotoImage(file = r"C:\Users\manik\Desktop\USB Spy\Images\RedDot.png")
        self.img_GreenDot = PhotoImage(file = r"C:\Users\manik\Desktop\USB Spy\Images\GreenDot.png")
        self.img_Browse = PhotoImage(file = r"C:\Users\manik\Desktop\USB Spy\Images\Browse.png")
        self.img_Hide = PhotoImage(file = r"C:\Users\manik\Desktop\USB Spy\Images\Hide.png")
        self.img_OpenFolder = PhotoImage(file = r"C:\Users\manik\Desktop\USB Spy\Images\OpenFolder.png")
        self.root.iconbitmap(r"C:\Users\manik\Desktop\USB Spy\Images\USB_icon.ico")

        self.createMainWindow()
        keyboard.add_hotkey(self.myHotKey, self.toogleHideShow)
        self.root.mainloop()

    def toogleHideShow(self):
        global status

        if status == "shown":
            status = "hidden"
            messagebox.showwarning("Hiding Window", "Please note that\n" + self.myHotKey + "\nis the shortcut to display USB Spy back.\n Press 'OK' to hide.")
            self.root.withdraw()
        else:
            status = "shown"
            self.root.update()
            self.root.deiconify()
    
    def detect(self):
        global fromDirectory, folder_location, copied

        usb = UsbDetection()
        detection = usb.isUsbDetected()
        if detection != None:
            fromDirectory = detection
            self.lbl_conn_dot['image'] = self.img_GreenDot
            self.lbl_conn_msg['text'] = "USB Connected !"
            if copied == 0:
                copy_tree(fromDirectory, folder_location)
                copied = 1
                self.lbl_UseMsg['text'] = "Hurray ! Files Copied Succefully.\nPress REFRESH and hide to copy from other USB"
                self.btn_OpenFolder.grid(row=2, column=0, columnspan=3)
        elif copied == 1:
            self.lbl_UseMsg['text'] = "Hurray ! Files Copied Succefully.\nPress REFRESH and hide to copy from other USB"
        else:
            self.lbl_conn_dot['image'] = self.img_RedDot
            self.lbl_conn_msg['text'] = "USB not connected :("
            self.lbl_UseMsg['text'] = "Please hide the window and wait\nfor USB to be inserted.\nThe files will be copied automatically\nto the destination folder."       
        self.root.after(200,self.detect)

    def browseFolder(self):
        global folder_location
        here = filedialog.askdirectory()
        if here.endswith('/'):
            here = here[:2]
        if here != "":
            folder_location = here + "/USB Spy"
        if len(folder_location) > 34:
            self.lbl_Path['text'] = folder_location[:38] + "..."
        else:
            self.lbl_Path['text'] = folder_location

    def setHotKey(self, key='H'):
        
        key = self.var.get()
        keys = []
        if self.CheckVar.get() == 1:
            keys.append('ctrl')
        if self.CheckVar2.get() == 1:
            keys.append('alt')
        if self.CheckVar3.get() == 1:
            keys.append('shift')
        if len(keys) == 0:
            messagebox.showwarning("Warning", "You have to select at least one HotKey\n Ctrl is selected by default.")
            self.CheckVar.set(1)
            self.myHotKey = "ctrl+" + key
        else:
            keys.append(key)
            self.myHotKey = '+'.join(keys)
        
        keyboard.clear_all_hotkeys()
        keyboard.add_hotkey(self.myHotKey, self.toogleHideShow)

    def openFolder(self):
        global folder_location
        os.open(folder_location)

    def on_enter(self, event):
        if len(folder_location) > 35:
            loc = folder_location[:35] + "\n" + folder_location[35:]
            self.lbl_Hover['text'] = loc
    def on_leave(self, event):
        self.lbl_Hover['text'] = ""

    #............................... Main Window .................................

    def createMainWindow(self):
        global folder_location

        #.............................. Fonts ....................................

        my_font = font.Font(size=12,family='Avenir Next LT Pro')
        my_font2 = font.Font(size=9,family='Avenir Next LT Pro')
        my_font3 = font.Font(size=9,family='Dungeon')

        self.frm_first = Frame(self.root, bg='white')
        self.frm_first.grid(row=0, column=0)

        self.frm_second = Frame(self.root, bg='white')
        self.frm_second.grid(row=1, column=0, padx=20, pady=15)

        self.frm_third = Frame(self.root, bg='white')
        self.frm_third.grid(row=2, column=0, padx=20)

        #.............................. First Frame ....................................

        lbl_Spy = Label(self.frm_first, image=self.img_Spy, font=my_font, border=0, anchor='w')
        self.lbl_conn_dot = Label(self.frm_first, image=self.img_RedDot, border=0, compound= RIGHT)
        self.lbl_conn_msg = Label(self.frm_first, text="USB not connected :(", bg='white', font=my_font2, anchor='e')
        self.lbl_UseMsg = Label(self.frm_first, text="", bg='white', fg='green', font=my_font2)
        self.btn_OpenFolder = Button(self.frm_first, image=self.img_OpenFolder, border=0, bg='white', command=self.openFolder)

        lbl_Spy.grid(row=0,column=0)
        self.lbl_conn_dot.grid(row=0, column=1)
        self.lbl_conn_msg.grid(row=0, column=2)
        self.lbl_UseMsg.grid(row=1, column=0, columnspan=3)

        #............................... Second Frame ....................................

        lbl_Target =Label(self.frm_second, text="Spy files to Folder:", font=my_font, bg='white')
        lbl_Target.grid(row=0, column=0)

        self.lbl_Path = Label(self.frm_second, text=folder_location, bg='black',width=35, fg='white', anchor='w', font=my_font2)
        self.lbl_Path.bind('<Enter>', self.on_enter)
        self.lbl_Path.bind('<Leave>', self.on_leave)

        btn_Browse = Button(self.frm_second, image=self.img_Browse, border=0, bg='white', command=self.browseFolder, cursor="hand2")
        
        self.lbl_Path.grid(row=1, column=0)
        btn_Browse.grid(row=1, column=1)

        self.lbl_Hover = Label(self.frm_second, fg='#8a8a8a', bg='white')
        self.lbl_Hover.grid(row=2, column=0)

        #............................... Third Frame .....................................

        lbl_Hotkey = Label(self.frm_third, text="Hotkey to toogle Hide/Show", bg='white', font=my_font)
        lbl_Hotkey.grid(row=0, column=0, columnspan=5)
        self.CheckVar = IntVar(value=1)
        self.CheckVar2 = IntVar(value=1)
        self.CheckVar3 = IntVar(value=0)
        self.var = StringVar(self.root)
        self.var.set('H')

        self.chk_Ctrl = Checkbutton(self.frm_third, text="Ctrl", bg='white', font=my_font3, variable = self.CheckVar, command=self.setHotKey)
        self.chk_Altr = Checkbutton(self.frm_third, text="Altr", bg='white', font=my_font3, variable = self.CheckVar2, command=self.setHotKey)
        self.chk_Shift = Checkbutton(self.frm_third, text="Shift", bg='white', font=my_font3, variable = self.CheckVar3, command=self.setHotKey)
        self.opt_Alphabet = OptionMenu(self.frm_third, self.var, 'A', 'B', 'C', 'D', 'F', 'G', 'H', command=self.setHotKey)
        self.opt_Alphabet.config(bg='white', border=0, width=2)
        self.btn_Hide = Button(self.frm_third, image=self.img_Hide, border=0, bg='white', text="Hide", cursor="hand2", command=self.toogleHideShow)

        self.chk_Ctrl.grid(row=1, column=0)
        self.chk_Altr.grid(row=1, column=1)
        self.chk_Shift.grid(row=1, column=2)
        self.opt_Alphabet.grid(row=1, column=3)
        self.btn_Hide.grid(row=1, column=4, padx=5)

        self.detect()

instance = UsbSpy()