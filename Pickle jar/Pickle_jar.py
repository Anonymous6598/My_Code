import customtkinter, tkinter, pickle, tkinter.messagebox, os, sys, Pickle_jar_interface, functools, typing

with open("pickle_jar_settings.pickle", "rb+") as data:
	language_data: str = pickle.load(data)

with open("pickle_jar_text_color.pickle", "rb+") as text_color_data:
	text_color: str = pickle.load(text_color_data)

with open("pickle_jar_button_color.pickle", "rb+") as button_color_data:
	button_color: str = pickle.load(button_color_data)

class Program(customtkinter.CTk, Pickle_jar_interface.Pickle_jar_interface):
    
    TITLE: typing.Final[str] = "Pickle jar"
    ICON: typing.Final[str] = "Pickle jar icon.ico"
    COLOR_THEME: typing.Final[str] = "dark-blue"
    THEME: typing.Final[str] = "system"
    WIDGET_SCALING: typing.Final[float] = 1.251
    
    def __init__(self, *args, **kwargs) -> None:
        customtkinter.CTk.__init__(self, *args, **kwargs)
        
        customtkinter.deactivate_automatic_dpi_awareness()
        customtkinter.set_widget_scaling(self.WIDGET_SCALING)
        customtkinter.set_default_color_theme(self.COLOR_THEME)
        customtkinter.set_appearance_mode(self.THEME)
	
        self.bind("<Configure>", self.__frame_resize__)
        
        self.protocol("WM_DELETE_WINDOW", self.__exit__)
        
        self.iconbitmap(self.ICON)
        self.title(self.TITLE)
        
        self.main_screen_fullscreen_numbers: int = 1
        
        self.main_screen_undo_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="⟲", text_color=text_color, height=20, width=10, corner_radius=0, fg_color=button_color, font=("Roboto Bold", 22), command=self.__undo__)
        self.main_screen_undo_button.grid(column=1, row=0)

        self.main_screen_redo_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="⟳", text_color=text_color, height=20, width=10, corner_radius=0, fg_color=button_color, font=("Roboto Bold", 22), command=self.__redo__)
        self.main_screen_redo_button.grid(column=2, row=0)
	    
        self.main_screen_save_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="сачувај текст", text_color=text_color, height=20, width=195, corner_radius=0, fg_color=button_color, font=("Roboto Bold", 22), command=lambda: self.__save_file__(pickle))
        self.main_screen_save_button.grid(column=3, row=0)
	
        self.main_screen_open_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="отвори фајл", text_color=text_color, height=20, width=195, corner_radius=0, fg_color=button_color, font=("Roboto Bold", 22), command=lambda: self.__open_file__(pickle))
        self.main_screen_open_button.grid(column=4, row=0)
	
        self.main_screen_settings_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text="подешавања", text_color=text_color, height=20, width=195, corner_radius=0, fg_color=button_color, font=("Roboto Bold", 22), command=self.__settings__)
        self.main_screen_settings_button.grid(column=5, row=0)
	
        self.main_screen_frame: customtkinter.CTkFrame = customtkinter.CTkFrame(master=self, height=760, width=1535, border_width=1, border_color=("black", "white"), corner_radius=0)
        self.main_screen_frame.grid(column=0, row=1, columnspan=5000)
	    
        self.main_screen_frame_textbox: customtkinter.CTkTextbox = customtkinter.CTkTextbox(master=self.main_screen_frame, height=757.5, width=1533.57, corner_radius=0, undo=True, fg_color="transparent", text_color=("black", "white"), font=("Ubuntu", 22))
        self.main_screen_frame_textbox.place(x=1, y=1)
        
        if language_data == "Српски":
            self.main_screen_save_button.configure(text="сачувај текст")
			
            self.main_screen_open_button.configure(text="отвори фајл")

            self.main_screen_settings_button.configure(text="подешавања")

        elif language_data == "English":
            self.main_screen_save_button.configure(text="save text")
			
            self.main_screen_open_button.configure(text="open file")

            self.main_screen_settings_button.configure(text="settings")

        else:
            self.main_screen_save_button.configure(text="сохранить текст")
	
            self.main_screen_open_button.configure(text="открыть файл")

            self.main_screen_settings_button.configure(text="настройки")
            
    def __frame_resize__(self, event: str) -> None:
        if self.winfo_width() <= 958:
            self.main_screen_frame.configure(width=1535 / 2 - 2)
            self.main_screen_frame_textbox.configure(width=1535 / 2 - 5)

        else:
            self.main_screen_frame.configure(width=1535)
            self.main_screen_frame_textbox.configure(width=1533.57)
	    
    def __undo__(self) -> None:
        try:
            self.main_screen_frame_textbox.edit_undo()

        except tkinter.TclError:
            pass

    def __redo__(self) -> None:
        try:
            self.main_screen_frame_textbox.edit_redo()

        except tkinter.TclError:
            pass
        
    def __save_file__(self, pickle_serialization: pickle) -> None:
        try:
            with open(tkinter.filedialog.asksaveasfilename(title="save file", filetypes=[("Pickle file (*.pickle)", "*.pickle")], defaultextension=[("Pickle file (*.pickle)", "*.pickle")]), "wb+") as self.file:
                self.file_data: str = self.main_screen_frame_textbox.get("1.0", tkinter.END)
                pickle.dump(self.file_data, self.file)

        except FileNotFoundError:
            pass
        
    def __open_file__(self, event) -> None:
        try:
            with open(tkinter.filedialog.askopenfilename(title="open file", filetypes=[("Pickle file (*.pickle)", "*.pickle")], defaultextension=[("Pickle file (*.pickle)", "*.pickle")]), "rb+") as self.openned_file:
                self.main_screen_frame_textbox.insert("1.0", pickle.load(self.openned_file))

        except FileNotFoundError:
            pass
            
    @functools.cache
    def __settings__(self) -> None:
        try:
            import Pickle_jar_settings_window
            
            self.pickle_jar_settings_window: Pickle_jar_settings_window.Pickle_jar_settings_window = Pickle_jar_settings_window.Pickle_jar_settings_window()
        
        except ImportError:
            if language_data == "Српски":
                tkinter.messagebox.showerror(title="Грешка", message="Нема те фајл са подешавањима")

            elif language_data == "English":
                tkinter.messagebox.showerror(title="Error", message="You don't have settings file")

            else:
                tkinter.messagebox.showerror(title="Ошибка", message="У вас нет файла с настройками")
                
    def __exit__(self) -> None:
        if language_data == "Српски":
            self.main_screen_exit: tkinter.messagebox.askyesno = tkinter.messagebox.askyesno(title="излаз", message="желите да изађете?")
            if self.main_screen_exit: sys.exit()

        elif language_data == "English":
            self.main_screen_exit: tkinter.messagebox.askyesno = tkinter.messagebox.askyesno(title="exit", message="would you like to exit?")
            if self.main_screen_exit: sys.exit()

        else:
            self.main_screen_exit: tkinter.messagebox.askyesno = tkinter.messagebox.askyesno(title="выход", message="желайте выйти?")
            if self.main_screen_exit: sys.exit()
	
    @functools.cache
    def __run__(self) -> None:
	    self.mainloop()
	    
if __name__ == "__main__":
	try:
		program: Program = Program()
		program.__run__()
															 
	except FileNotFoundError:
		tkinter.messagebox.showerror(title="file not found error", message=f"срб: грешка: није нађен фајл \n eng: error: missing data file \nрус: ошибка: не найден файл")

	except tkinter.TclError:
		tkinter.messagebox.showerror(title="icon file not found error", message=f"срб: грешка: није нађен фајл иконица \neng: error: missing icon file \nрус: ошибка: не найден файл с иконкой")

	except EOFError:
		tkinter.messagebox.showerror(title="corrupted file error", message=f"срб: грешка: повређен фајл \n eng: error: corrupted data file \nрус: ошибка: повреждён файл")