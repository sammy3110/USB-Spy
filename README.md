# **** USB-Spy ****
USB Spy is a tool which is used for spying someones USB drive inserted in your PC.

Credits: A USB Spy tool is already available.
I created a simple and easy to use version for it.

The structure contains two codes.
1. USB Spy.py (Main GUI code)
2. DetectingDrive.py (Code to detect pendrive)

The tool has a simple interface. You can set up the tool and hide it. It will not be visible either on taskbar or hidden icons. Whenever a pendrive will be inserted in the PC the tool will detect it and will automatically copy all of its folders, sub-folders and the contents in it to the folder specified by you. If no folder is selected by you in the tool menu the default location to copy fils is `C:/USB Spy`. It will automatically create the folder and copy files there.

# Working with the code
____________________________________________
For using the python code in your machine, you will have to install python obviously and furthermore install some of the modules.

Open 'command prompt' and use these commands to install the modules

* `pip install tkinter`
* `pip install keyboard`

# Using the Tool
______________________________________________
When you are all set and work with the tool.
Here is some directions with the images. Please have a look how the tool works :grin:

1) Very first screen when the tool is started.
______________________________________________
![Main Screen](/Images/Main_Screen.jpg)

2) You can select path on your PC to store files.
______________________________________________
![Select Store Path](/Images/Select_Path.jpg)

3) Use shortcut to toogle Hide/Show the main window.
______________________________________________
![Select Shorcut](/Images/Select_Shortcut.jpg)

4) Hide the window and wait for USB to be inserted. When you hide a window a pop-up warning message will be displayed showing you to remember the shortcut to re-display the main window.
______________________________________________
![Hide Pop-up](/Images/Hide_Popup.jpg)

5) When the USB is connected the files will be copied to the destination folder (Default: C:/USB Spy). As you can see files in my pen drive is same as files copied to the destination folder.
______________________________________________
![Destination Folder](/Images/Destination_Folder.jpg)

6) After the files are copied and you unhide the main window you will see a folder icon. Click it to open the folder where the files are copied.
______________________________________________
![Open Destination](/Images/Open_Destination.jpg)

# Congrates ! You Spied USB Files to your PC :wink:

Thank You !
Stay Safe !
Peace !