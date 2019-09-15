import tkinter
print(tkinter.TkVersion)


mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480+8+400')

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')
canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.pack(side='top', fill=tkinter.Y, expand=True)
mainWindow.mainloop()