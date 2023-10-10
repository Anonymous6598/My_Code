import customtkinter, tkinter, pickle, tkinter.messagebox, Pickle_jar_settings_window_interface, Pickle_jar, typing

with open("pickle_jar_settings.pickle", "rb+") as data:
	language_data: str = pickle.load(data)

with open("pickle_jar_text_color.pickle", "rb+") as text_color_data:
	text_color: str = pickle.load(text_color_data)

with open("pickle_jar_button_color.pickle", "rb+") as button_color_data:
	button_color: str = pickle.load(button_color_data)

class Pickle_jar_settings_window(customtkinter.CTkToplevel, Pickle_jar_settings_window_interface.Pickle_jar_settings_window_interface):
    
    WIDTH: typing.Final[int] = 655 
    HEIGHT: typing.Final[int] = 471
    TITLE: typing.Final[str] = "Pickle jar settings window"
    WINDOW: typing.Final[str] = "-toolwindow"

    def __init__(self, *args, **kwargs) -> None:
        customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

        self.minsize(width=self.WIDTH, height=self.HEIGHT)
        self.resizable(False, False)
        self.title(self.TITLE)
        self.attributes(self.WINDOW, True)

        self.main_screen_settings_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text="Подешавања", text_color=text_color, font=("Roboto Bold", 75))
        self.main_screen_settings_text.place(x=0, y=0)

        self.main_screen_language_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text="Језици", text_color=text_color, font=("Roboto Bold", 50))
        self.main_screen_language_text.place(x=0, y=87)

        self.main_screen_settings_language_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self, values=["Српски", "English", "Русский"], selected_color=button_color, command=self.__change_language__)
        self.main_screen_settings_language_option.place(x=15, y=147)

        self.main_screen_settings_language_option.set(language_data)
        
        self.main_screen_settings_customatization_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text="Спољни изглед", text_color=text_color, font=("Roboto Bold", 36))
        self.main_screen_settings_customatization_text.place(x=15, y=207)

        self.main_screen_settings_customatization_table: customtkinter.CTkTabview = customtkinter.CTkTabview(master=self, height=50, width=400, border_width=1, border_color=("black", "white"), segmented_button_selected_color=button_color, text_color=text_color)
        self.main_screen_settings_customatization_table.place(x=15, y=243)

        self.main_screen_settings_customatization_table.add("1")
        self.main_screen_settings_customatization_table.add("2")

        self.main_screen_settings_customatization_text_color_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self.main_screen_settings_customatization_table.tab("1"), text="Боја текста", text_color=text_color, font=("Roboto Bold", 36))
        self.main_screen_settings_customatization_text_color_text.grid(column=0, row=0)

        self.main_screen_settings_customatization_text_color_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab("1"), text_color=text_color, values=["red", "blue", "green", "black", "white"], selected_color=button_color, command=self.__change_text_color__)
        self.main_screen_settings_customatization_text_color_option.grid(column=0, row=1)


        self.main_screen_settings_customatization_button_color_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self.main_screen_settings_customatization_table.tab("2"), text="Боја дугма", text_color=text_color, font=("Roboto Bold", 36))
        self.main_screen_settings_customatization_button_color_text.grid(column=0, row=0)

        self.main_screen_settings_customatization_button_color_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab("2"), values=["red", "blue", "green", "black", "orange", "yellow", "purple"], text_color=text_color, selected_color=button_color, command=self.__change_button_color__)
        self.main_screen_settings_customatization_button_color_option.grid(column=0, row=1)

        self.main_screen_settings_customatization_text_color_option.set(text_color)

        self.main_screen_settings_customatization_button_color_option.set(button_color)

        if language_data == "Српски":
            self.main_screen_settings_text.configure(text="Подешавања")
            self.main_screen_language_text.configure(text="Језици")
            self.main_screen_settings_customatization_text.configure(text="Спољни изглед")
            self.main_screen_settings_customatization_text_color_text.configure(text="Боја текста")
            self.main_screen_settings_customatization_button_color_text.configure(text="Боја дугма")

        elif language_data == "English":
            self.main_screen_settings_text.configure(text="Settings")
            self.main_screen_language_text.configure(text="Languages")
            self.main_screen_settings_customatization_text.configure(text="Customatization")
            self.main_screen_settings_customatization_text_color_text.configure(text="Text color")
            self.main_screen_settings_customatization_button_color_text.configure(text="Button color")

        else:
            self.main_screen_settings_text.configure(text="Настройки")
            self.main_screen_language_text.configure(text="Языки")
            self.main_screen_settings_customatization_text.configure(text="Внешний вид")
            self.main_screen_settings_customatization_text_color_text.configure(text="Цвет текста")
            self.main_screen_settings_customatization_button_color_text.configure(text="Цвет кнопки")

    def __change_language__(self, pickle_serializer: pickle) -> None:
        self.main_screen_settings_language_option_data: str = self.main_screen_settings_language_option.get()
        with open("pickle_jar_settings.pickle", "wb+") as self.data:
            pickle.dump(self.main_screen_settings_language_option_data, self.data)

        if self.main_screen_settings_language_option_data == "Српски":
            tkinter.messagebox.showwarning(title="Пажња", message="Рестартуј програм")

        elif self.main_screen_settings_language_option_data == "English":
            tkinter.messagebox.showwarning(title="Warning", message="Restart program")
            
        else:
            tkinter.messagebox.showwarning(title="Внимание", message="Перезагрузите программу")
    
    def __change_text_color__(self, pickle_serializer: pickle) -> None:
        self.main_screen_settings_customatization_text_color_option_data: str = self.main_screen_settings_customatization_text_color_option.get()
        with open("pickle_jar_text_color.pickle", "wb+") as self.text_color_data:
            pickle.dump(self.main_screen_settings_customatization_text_color_option_data, self.text_color_data)            

        if language_data == "Српски":        
            tkinter.messagebox.showwarning(title="Пажња", message="Рестартуј програм")
            
        elif language_data == "English":
            tkinter.messagebox.showwarning(title="Warning", message="Restart program")
            
        else:
            tkinter.messagebox.showwarning(title="Внимание", message="Перезагрузите программу")

    def __change_button_color__(self, pickle_serialization: pickle) -> None:
        self.main_screen_settings_customatization_button_color_option_data: str = self.main_screen_settings_customatization_button_color_option.get()
        with open("pickle_jar_button_color.pickle", "wb+") as self.button_color_data:
            pickle.dump(self.main_screen_settings_customatization_button_color_option_data, self.button_color_data)

        if language_data == "Српски":
            tkinter.messagebox.showwarning(title="Пажња", message="Рестартуј програм")

        elif language_data == "English":
            tkinter.messagebox.showwarning(title="Warning", message="Restart program")

        else:
            tkinter.messagebox.showwarning(title="Внимание", message="Перезагрузите программу")
            
pickle_jar: Pickle_jar.Program = Pickle_jar.Program()