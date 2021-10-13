#!/usr/bin/python3
# Black Wikipedia
import os
import sys
import webbrowser

try:
    from tkinter import scrolledtext
    from tkinter import *
    from tkinter.ttk import Button as TButton ,Label as TLabel
    from tkinter.messagebox import showerror
    from tkinter.colorchooser import askcolor
    from tkinter import filedialog
    from tkinter.scrolledtext import ScrolledText
except (ImportError,ModuleNotFoundError):
    os.system("pip install tk-tools")
try:
    import wikipedia
    from wikipedia import exceptions
except (ImportError,ModuleNotFoundError):
    os.system("pip install wikipedia")
class black_wikipedia(Tk):
    def __init__(self):
        super(black_wikipedia,self).__init__()
        global window,label_b,label_s,search_b,i3,label,m
        self.title('Black Wikipedia')
        self.geometry("400x300")
        self.resizable(0,0)
        label = Label(self,text='Black-Wikipedia',bg='white',fg='black')
        label.pack(side = BOTTOM)
        m = Menu(self,tearoff=0)
        m.add_command(label='Cut',accelerator='Ctrl+X',command=self.cut_text)
        m.add_command(label='Copy',accelerator='Ctrl+C',command=self.copy_text)
        m.add_command(label='Paste',accelerator='Ctrl+V',command=self.paste_text)
        m.add_command(label='Reload',command=self.reload_text)
        m.add_separator()
        m.add_command(label='Exit',accelerator='Ctrl+F4',command=self.ext)
        menu = Menu(self)
        filemenu = Menu(menu,tearoff=0)
        aboutmenu = Menu(menu,tearoff=0)
        themefile = Menu(menu,tearoff=0)
        filemenu.add_command(label='New',accelerator="Ctrl+N",command=self.new)
        filemenu.add_command(label='Open',accelerator="Ctrl+O",command=self.open_f)
        filemenu.add_command(label='Close All',accelerator='Ctrl+F4',command=self.close_all)
        filemenu.add_separator()
        filemenu.add_command(label='Exit',accelerator='Alt+F4',command=self.ext)
        aboutmenu.add_command(label='Black',accelerator='F1',command=self.black)
        aboutmenu.add_command(label='Dev',accelerator='F2',command=self.dev)
        themefile.add_radiobutton(label='Dark',command=self.dark,value="dark")
        themefile.add_radiobutton(label='Light',command=self.light,value="light")
        themefile.add_separator()
        themefile.add_radiobutton(label='Costumize',command=self.costumize,value="costumize")
        # themefile.add_radiobutton(label='',command='',value='')
        menu.add_cascade(label='File',menu=filemenu)
        menu.add_cascade(label='About',menu=aboutmenu)
        menu.add_cascade(label='Theme',menu=themefile)
        self.config(menu=menu)

        label_b = Label(self,text='Black Wikipedia',font=("None",25),bg='white',fg='black')
        label_b.place(bordermode=INSIDE,x=90,y=20)
        label_s = TLabel(self,text='Search:',background='white',foreground='black')
        label_s.place(bordermode=INSIDE,x=65,y=80)
        search_b = Entry(self,width=25,borderwidth=3)
        search_b.place(bordermode=OUTSIDE,x=128,y=80)

        self.search_button = Button(self,text='Search',width=9,height=3,command=self.start)
        self.search_button.place(bordermode=OUTSIDE,x=160,y=120)
        self.exit_button = Button(self,text='Exit',width=9,height=3,command=self.ext)
        self.exit_button.place(bordermode=OUTSIDE,x=160,y=180)
        self.config(bg='white')
        self.bind("<Button-3>",self.do_popup)
        self.bind("<Return>",lambda x: self.start_2(x))
        self.bind("<F1>",lambda x: self.dev_2(x))
        self.bind("<Control-F4>",lambda x: self.close_all_2(x))
        self.bind("<F2>",lambda x: self.black_2(x))
        self.bind("<Control-o>",lambda x: self.open_f_2(x))
        self.bind("<Control-n>",lambda x: self.new_3(x))
        self.photo = PhotoImage(file = './Scr/black.png')
        self.iconphoto(False,self.photo)
        self.mainloop()
    def do_popup(self,event):
        try:
            m.tk_popup(event.x_root, event.y_root)
        finally:
            m.grab_release()
    def cut_text(self):
        label.event_generate(("<<Cut>>"))
    def copy_text(self):
        label.event_generate(("<<Copy>>"))
    def paste_text(self):
        label.event_generate(("<<Paste>>"))
    def reload_text(self):
        label.event_generate(('<<Reload>>'))

    def new(self):
        global window,txt
        window = Tk()
        window.title('Untitled')
        window.geometry("500x400")
        window.maxsize(700,700)
        window.minsize(300,300)
        menu = Menu(window)
        filemenu = Menu(menu,tearoff=0)
        thememenu = Menu(menu,tearoff=0)
        filemenu.add_command(label='New',command=self.new)
        filemenu.add_command(label='Save',command=self.save3)
        filemenu.add_command(label='Open',command=self.open_f)
        filemenu.add_command(label='Close',command=window.destroy)
        filemenu.add_separator()
        filemenu.add_command(label='Exit',accelerator='Alt+F4',command=self.ext)
        thememenu.add_command(label='Dark',command=self.dark_2)
        thememenu.add_command(label='Light',command=self.light_2)
        thememenu.add_separator()
        thememenu.add_command(label='Costumize',command=self.costumize_2)
        menu.add_cascade(label='File',menu=filemenu)
        menu.add_cascade(label='Theme',menu=thememenu)
        txt = ScrolledText(window)
        txt.pack()
        self.c = False
        txt['state'] = 'normal'
        window.config(menu=menu)
        window.mainloop()
    def new_2(self,x):
        global window,txt
        window = Tk()
        window.title('Untitled')
        window.geometry("500x400")
        window.maxsize(700,700)
        window.minsize(300,300)
        menu = Menu(window)
        filemenu = Menu(menu,tearoff=0)
        thememenu = Menu(menu,tearoff=0)
        filemenu.add_command(label='New',command=self.new)
        filemenu.add_command(label='Save',command=self.save3)
        filemenu.add_command(label='Open',command=self.open_f)
        filemenu.add_command(label='Close',command=window.destroy)
        filemenu.add_separator()
        filemenu.add_command(label='Exit',accelerator='Alt+F4',command=self.ext)
        thememenu.add_command(label='Dark',command=self.dark_2)
        thememenu.add_command(label='Light',command=self.light_2)
        thememenu.add_separator()
        thememenu.add_command(label='Costumize',command=self.costumize_2)
        menu.add_cascade(label='File',menu=filemenu)
        menu.add_cascade(label='Theme',menu=thememenu)
        txt = ScrolledText(window)
        txt.pack()
        self.c = False
        txt['state'] = 'normal'
        window.config(menu=menu)
        window.mainloop()
    def new_3(self,x):
        global window,txt
        window = Tk()
        window.title('Untitled')
        window.geometry("500x400")
        window.maxsize(700,700)
        window.minsize(300,300)
        menu = Menu(window)
        filemenu = Menu(menu,tearoff=0)
        thememenu = Menu(menu,tearoff=0)
        filemenu.add_command(label='New',command=self.new)
        filemenu.add_command(label='Save',command=self.save3)
        filemenu.add_command(label='Open',command=self.open_f)
        filemenu.add_command(label='Close',command=window.destroy)
        filemenu.add_separator()
        filemenu.add_command(label='Exit',accelerator='Alt+F4',command=self.ext)
        thememenu.add_command(label='Dark',command=self.dark_2)
        thememenu.add_command(label='Light',command=self.light_2)
        thememenu.add_separator()
        thememenu.add_command(label='Costumize',command=self.costumize_2)
        menu.add_cascade(label='File',menu=filemenu)
        menu.add_cascade(label='Theme',menu=thememenu)
        txt = ScrolledText(window)
        txt.pack()
        self.c = False
        txt['state'] = 'normal'
        window.config(menu=menu)
        window.mainloop()
    def save3(self):
        global file_s_2
        if self.c:
            file_s_2.write(str(txt.get("1.0",END)))
            file_s_2.close()
        else:
            file_s_2 = filedialog.asksaveasfile(title='Save As')
            file_s_2.write(str(txt.get("1.0",END)))
            file_s_2.close()
            c = True
    def open_f(self):
        global window,i,file,txt
        file = filedialog.askopenfile(title='Select File',mode="r+")
        i = True
        window = Tk()
        window.title(file.name)
        menu = Menu(window)
        filemenu = Menu(menu,tearoff=0)
        filemenu.add_command(label='New',command=self.new)
        filemenu.add_command(label='Save',command=self.save)
        filemenu.add_command(label='Open',command=self.open_f)
        filemenu.add_command(label='Close',command=window.destroy)
        filemenu.add_separator()
        filemenu.add_command(label='Exit',accelerator='Alt+F4',command=self.ext)
        menu.add_cascade(label='File',menu=filemenu)
        window.config(menu=menu)
        window.geometry("500x400")
        window.maxsize(700,700)
        window.minsize(300,300)
        txt = ScrolledText(window)
        txt.pack()
        txt['state'] = 'normal'
        txt.insert(END,str(file.read()))
        window.mainloop()
    def open_f_2(self,x):
        global window,i,file,txt
        file = filedialog.askopenfile(title='Select File',mode="r+")
        i = True
        window = Tk()
        window.title(file.name)
        menu = Menu(window)
        filemenu = Menu(menu,tearoff=0)
        filemenu.add_command(label='New',command=self.new)
        filemenu.add_command(label='Save',command=self.save)
        filemenu.add_command(label='Open',command=self.open_f)
        filemenu.add_command(label='Close',command=window.destroy)
        filemenu.add_separator()
        filemenu.add_command(label='Exit',accelerator='Alt+F4',command=self.ext)
        menu.add_cascade(label='File',menu=filemenu)
        window.config(menu=menu)
        window.geometry("500x400")
        window.maxsize(700,700)
        window.minsize(300,300)
        txt = ScrolledText(window)
        txt.pack()
        txt['state'] = 'normal'
        txt.insert(END,str(file.read()))
        window.mainloop()
    def save(self):
        global file_s
        if i:
            file.write(txt.get("1.0",END))
            file.close()
        else:
            file_s = filedialog.asksaveasfile(title='Save As')
    def close_all(self):
        try:
            window.destroy()
        except TclError:
            print(False)
    def close_all_2(self,x):
        try:
            window.destroy()
        except TclError:
            print(False)
    def ext(self):
        self.destroy()
        self.quit()
        quit()
    def dev(self):
        webbrowser.open_new_tab('https://github.com/mrprogrammer2938')
    def black(self):
        webbrowser.open_new_tab('https://black-software.ir')
    def dev_2(self,x):
        webbrowser.open_new_tab('https://github.com/mrprogrammer2938')
    def black_2(self,x):
        webbrowser.open_new_tab('https://black-software.ir')
    def save_2(self):
        global i2
        file_s = filedialog.asksaveasfile(title='Save As')
        file_s.write(str(txt2.get("1.0",END)))
        file_s.close()
        i2 = True

    def start(self):
        try:
            global window,txt2
            window = Tk()
            window.title(search_b.get())
            window.geometry("500x400")
            window.maxsize(1000,700)
            window.minsize(300,300)
            menu = Menu(window)
            filemenu = Menu(menu,tearoff=0)
            filemenu.add_command(label='New',command=self.new)
            filemenu.add_command(label='Save',command=self.save_2)
            filemenu.add_command(label='Open',command=self.open_f)
            filemenu.add_command(label='Close All',command=self.close_all)
            filemenu.add_separator()
            filemenu.add_command(label='Exit',accelerator='Alt+F4',command=self.ext)
            menu.add_cascade(label='File',menu=filemenu)
            txt2 = ScrolledText(window)
            txt2.pack()
            r = wikipedia.summary(search_b.get(),sentences=1000)
            txt2.insert(END,str(r))
            txt2['state'] = 'disabled'
            window.config(menu=menu)
            window.mainloop()
        except exceptions.WikipediaException:
            print(False)
            window.destroy()
            showerror(title='Cannot Search',message='Please, Check Input Key!')
    def start_2(self,x):
        try:
            global window,txt2
            window = Tk()
            window.title(search_b.get())
            window.geometry("500x400")
            window.maxsize(1000,700)
            window.minsize(300,300)
            menu = Menu(window)
            filemenu = Menu(menu,tearoff=0)
            filemenu.add_command(label='New',command=self.new)
            filemenu.add_command(label='Save',command=self.save_2)
            filemenu.add_command(label='Open',command=self.open_f)
            filemenu.add_command(label='Close All',command=self.close_all)
            filemenu.add_separator()
            filemenu.add_command(label='Exit',accelerator='Alt+F4',command=self.ext)
            menu.add_cascade(label='File',menu=filemenu)
            txt2 = ScrolledText(window)
            txt2.pack()
            r = wikipedia.summary(search_b.get(),sentences=1000)
            txt2.insert(END,str(r))
            txt2['state'] = 'disabled'
            window.config(menu=menu)
            window.mainloop()
        except exceptions.WikipediaException:
            print(False)
            window.destroy()
            showerror(title='Cannot Search',message='Please, Check Input Key')
    def dark(self):
        # window.config(bg='black')
        self.config(bg='black')
        search_b.config(background='black',foreground='green')
        label_b.config(background='black',foreground='green')
        label_s.config(background='black',foreground='green')
        label.config(bg='black',fg='green')
        self.exit_button.config(bg='black',fg='green')
        self.search_button.config(bg='black',fg='green')
        
    def light(self):
        # window.config(bg='black')
        self.config(bg='white')
        search_b.config(background='white',foreground='black')
        label_b.config(background='white',foreground='black')
        label_s.config(background='white',foreground='black')
        label.config(bg='white',fg='black')
        self.exit_button.config(bg='white',fg='black')
        self.search_button.config(bg='white',fg='black')
    
    def costumize(self):
        color = askcolor(title='Choose Color')
        self.config(background=color[1])
    def dark_2(self):
        window.config(bg='black')
    def light_2(self):
        window.config(bg='white')
    def costumize_2(self):
        color = askcolor(title='Choose Color')
        window.config(bg=color[1])
if __name__ == '__main__':
    window = black_wikipedia()
