import tkinter as tk

import panel_detect

def fun1():
    print ("yes")
    pass


def fun2():
    print ("det")
    # image_demo.image_detect()
    pass



def forml1():
    forml = tk.Tk()

    forml.title("detecting")
    forml.geometry('%dx%d+%d+%d' % (800, 600, 200, 100))

    menubar = tk.Menu(forml)

    fileMenu = tk.Menu(menubar, tearoff=False)

    fileMenu.add_command(label="open_picture", command=fun1())
    #
    # fileMenu.add_command(label="exit", command=fun2())

    menubar.add_cascade(label="picture", menu=fileMenu)

    forml.config(menu=menubar)


    # label = tk.Label(forml,text = "this is a word",
    #                       bg = "pink", fg = "red",
    #                       width = 20,height = 10,
    #                       wraplength = 100,
    #                       justify = "left",anchor = "ne")
    # label.pack()

    button1 = tk.Button(forml, text="ooo")

    # button1.pack()
    # entry = tk.Entry(forml)
    #
    # def showinfo():
    #     print(entry.get())
    #
    # buttun = tk.Button(forml, text="set", commamd=showinfo())
    # buttun.pack()
    button1.pack()
    button1.bind("<Button-1>", func=fun1())


    forml.mainloop()


def main():
    forml1()


if __name__ == '__main__':
    main()
