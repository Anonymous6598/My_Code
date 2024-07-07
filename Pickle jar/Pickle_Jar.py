from tkinterdnd2 import *
import pywinstyles, Pickle_Jar_Interface, tkinter.messagebox, tkinter.filedialog, typing, chlorophyll, pygments.lexers.python, locale, tkinter, Pickle_Jar_AI_window

class Program(Tk, Pickle_Jar_Interface.Pickle_Jar_Interface):
    
    TITLE: typing.Final[str] = f"Pickle Jar"
    ICON: typing.Final[str] = f"Pickle jar icon.ico"
    STYLE: typing.Final[str] = f"native"
    
    def __init__(self: typing.Self, *args: typing.Any, **kwargs: typing.Any) -> None:
        TkinterDnD.Tk.__init__(self, *args, **kwargs)
        
        self.title(self.TITLE)
        self.iconbitmap(self.ICON)
        
        pywinstyles.apply_style(self, style=self.STYLE)
        pywinstyles.change_header_color(window=self, color=f"green")

        self.main_screen_code_field: chlorophyll.Codeview = chlorophyll.CodeView(self, lexer=pygments.lexers.python.PythonLexer, color_scheme=f"ayu-dark", undo=True)
        self.main_screen_code_field.pack(fill=f"both", expand=True)
        
        self.main_screen_code_field.drop_target_register(DND_ALL)
        self.main_screen_code_field.dnd_bind(f"<<Drop>>", self.__drop_file_into_code_field__)
        
        self.main_screen_menu: tkinter.Menu = tkinter.Menu()
        
        self.main_screen_menu.add_cascade(label=f"⟲", command=lambda: self.main_screen_code_field.edit_undo())
        self.main_screen_menu.add_cascade(label=f"⟳", command=lambda: self.main_screen_code_field.edit_redo())
        
        if locale.getdefaultlocale()[0] == f"sr_RS":
            self.main_screen_menu.add_cascade(label=f"пусти", command=self.__run_code__)
            self.main_screen_menu.add_cascade(label=f"отвори", command=self.__open_code__)
            self.main_screen_menu.add_cascade(label=f"сачувај", command=self.__save_code__)
            self.main_screen_menu.add_cascade(label=f"обриши", command=self.__delete_code__)
            self.main_screen_menu.add_cascade(label=f"AI", command=self.__open_ai_window__) 

        elif locale.getdefaultlocale()[0] == f"ru_RU":
            self.main_screen_menu.add_cascade(label=f"запустить", command=self.__run_code__)
            self.main_screen_menu.add_cascade(label=f"открыть", command=self.__open_code__)
            self.main_screen_menu.add_cascade(label=f"сохранить", command=self.__save_code__)
            self.main_screen_menu.add_cascade(label=f"стереть", command=self.__delete_code__)
            self.main_screen_menu.add_cascade(label=f"ИИ (локальная нейросеть)", command=self.__open_ai_window__)

        else:
            self.main_screen_menu.add_cascade(label=f"run", command=self.__run_code__)
            self.main_screen_menu.add_cascade(label=f"open", command=self.__open_code__)
            self.main_screen_menu.add_cascade(label=f"save", command=self.__save_code__)
            self.main_screen_menu.add_cascade(label=f"delete", command=self.__delete_code__)
            self.main_screen_menu.add_cascade(label=f"AI", command=self.__open_ai_window__)

        self.config(menu=self.main_screen_menu)
        
        self.bind(f"<F1>", lambda event: self.main_screen_code_field.edit_undo())
        self.bind(f"<F2>", lambda event: self.main_screen_code_field.edit_redo())
        self.bind(f"<F3>", self.__open_code__)
        self.bind(f"<F4>", self.__save_code__)
        self.bind(f"<F5>", self.__run_code__)
        self.bind(f"<F6>", self.__delete_code__)
        self.bind(f"<F7>", self.__open_ai_window__)
        
    def __run_code__(self: typing.Self, event: str | None = None) -> None:
        try:
            exec(f"{self.main_screen_code_field.get(f'1.0', tkinter.END)}")
            
        except Exception as exception:
            if locale.getdefaultlocale()[0] == f"sr_RS":
                tkinter.messagebox.showerror(title=f"грешка", message=f"{exception}")
                
            elif locale.getdefaultlocale()[0] == f"ru_RU":
                tkinter.messagebox.showerror(title=f"ошибка", message=f"{exception}")
                
            else:
                tkinter.messagebox.showerror(title=f"error", message=f"{exception}")
        
    def __save_code__(self: typing.Self, event: str | None = None) -> None:
        self.file_name: tkinter.filedialog = tkinter.filedialog.asksaveasfilename(title=f"save python file", filetypes=[(f"Python file (*.py)", f"*.py")], defaultextension=[(f"Python file (*.py)", f"*.py")])

        with open(self.file_name, f"w+", encoding=f"UTF-8") as self.file:
            self.file_data: str = self.main_screen_code_field.get("1.0", tkinter.END)
            self.file.write(self.file_data)

    def __open_code__(self: typing.Self, event: str | None = None) -> None:
        self.opened_name_file: tkinter.filedialog = tkinter.filedialog.askopenfilename(title=f"open python file", filetypes=[(f"Python file (*.py)", f"*.py")], defaultextension=[(f"Python file (*.py)", f"*.py")])

        with open(self.opened_name_file, f"r+", encoding=f"UTF-8") as self.openned_file: self.main_screen_code_field.insert(f"1.0", self.openned_file.read())
    
    def __drop_file_into_code_field__(self: typing.Self, event: str | None = None) -> None:
        self.main_screen_code_field.delete(f"1.0", tkinter.END)
        if event.data.endswith(f".py"):
            with open(event.data, f"r+", encoding=f"UTF-8") as self.openned_file: 
                self.main_screen_code_field.insert(f"1.0", self.openned_file.read())
                
        else:
            if locale.getdefaultlocale()[0] == f"sr_RS":
                tkinter.messagebox.showerror(title=f"грешка", message=f"то није python фајл")
                
            elif locale.getdefaultlocale()[0] == f"ru_RU":
                tkinter.messagebox.showerror(title=f"ошибка", message=f"это не python файл")
                
            else:
                tkinter.messagebox.showerror(title=f"error", message=f"this is not python file")

    def __delete_code__(self: typing.Self, event: str | None = None) -> None:
        self.main_screen_code_field.delete(f"1.0", tkinter.END)
    
    def __open_ai_window__(self: typing.Self, event: str | None = None) -> None:
        self.ai_window: Pickle_Jar_AI_window.AI_Window = Pickle_Jar_AI_window.AI_Window()
        
if __name__ == f"__main__":
    program: Program = Program()
    program.mainloop()