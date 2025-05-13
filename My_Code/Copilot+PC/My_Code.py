import customtkinter, tkinterdnd2, My_Code_Interface, tkinter.messagebox, tkinter.filedialog, typing, locale, tkinter, My_Code_window, CTkCodeBox, CTkMenuBar, sys, warnings, My_Code_bash_terminal, os, CTkToolTip, My_Code_AI, My_Code_AI_window_interface, speech_recognition

warnings.filterwarnings(f"ignore")

SLM: My_Code_AI.My_Code_LM = My_Code_AI.My_Code_LM().__initialize_model__()

class Program(My_Code_window.Window, My_Code_Interface.My_Code_Interface):
    
    TITLE: typing.Final[str] = f"My Code (Copilot+PC edition)"
    ICON: typing.Final[str] = f"My Code icon.ico"
    COLOR_THEME: typing.Final[str] = f"dark-blue"
    THEME: typing.Final[str] = f"system"
    
    def __init__(self: typing.Self, *args: typing.Any, **kwargs: typing.Any) -> None:
        My_Code_window.Window.__init__(self, *args, **kwargs)
        
        customtkinter.set_default_color_theme(self.COLOR_THEME)
        customtkinter.set_appearance_mode(self.THEME)
        
        self.title(self.TITLE)   
        self.iconbitmap(self.ICON)
        self.protocol(f"WM_DELETE_WINDOW", self.__exit__)

        self.main_screen_code_field: CTkCodeBox.CTkCodeBox = CTkCodeBox.CTkCodeBox(self, language=f"python", line_numbering=True, menu=True, undo=True, theme=f"default", fg_color=f"black")
        self.main_screen_code_field.pack(fill=f"both", expand=True)
        
        self.main_screen_code_field.drop_target_register(tkinterdnd2.DND_ALL)
        self.main_screen_code_field.dnd_bind(f"<<Drop>>", self.__drop_file_into_code_field__)
        
        self.main_screen_title_menu: CTkMenuBar.CTkTitleMenu = CTkMenuBar.CTkTitleMenu(self)
        
        self.main_screen_title_menu_menu_button: customtkinter.CTkButton = self.main_screen_title_menu.add_cascade(text=f"☰")
        
        self.main_screen_title_menu_undo_button: customtkinter.CTkButton = self.main_screen_title_menu.add_cascade(text=f"⟲", command=lambda: self.main_screen_code_field.edit_undo())
        self.main_screen_title_menu_redo_button: customtkinter.CTkButton = self.main_screen_title_menu.add_cascade(text=f"⟳", command=lambda: self.main_screen_code_field.edit_redo())

        self.main_screen_title_menu_submenu: CTkMenuBar.CustomDropdownMenu = CTkMenuBar.CustomDropdownMenu(widget=self.main_screen_title_menu_menu_button, fg_color=f"transparent")
        
        if locale.getdefaultlocale()[0] == f"sr_RS":            
            self.main_screen_title_menu_submenu_run_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"пусти", command=self.__run_code__)
            self.main_screen_title_menu_submenu_open_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"отвори", command=self.__open_code__)
            self.main_screen_title_menu_submenu_save_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"сачувај", command=self.__save_code__)
            self.main_screen_title_menu_submenu_delete_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"обриши", command=self.__delete_code__)
            self.main_screen_title_menu_submenu_ai_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"AI", command=lambda: My_Code_AI_Window()) 
            self.main_screen_title_menu_submenu_bash_terminal_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f">_", command=lambda: My_Code_bash_terminal.My_Code_bash_terminal())

        elif locale.getdefaultlocale()[0] == f"ru_RU":            
            self.main_screen_title_menu_submenu_run_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"запустить", command=self.__run_code__)
            self.main_screen_title_menu_submenu_open_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"открыть", command=self.__open_code__)
            self.main_screen_title_menu_submenu_save_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"сохранить", command=self.__save_code__)
            self.main_screen_title_menu_submenu_delete_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"стереть", command=self.__delete_code__)
            self.main_screen_title_menu_submenu_ai_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"ИИ (локальная нейросеть)", command=lambda: My_Code_AI_Window())
            self.main_screen_title_menu_submenu_bash_terminal_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f">_", command=lambda: My_Code_bash_terminal.My_Code_bash_terminal())

        else:            
            self.main_screen_title_menu_submenu_run_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"run", command=self.__run_code__)
            self.main_screen_title_menu_submenu_open_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"open", command=self.__open_code__)
            self.main_screen_title_menu_submenu_save_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"save", command=self.__save_code__)
            self.main_screen_title_menu_submenu_delete_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"delete", command=self.__delete_code__)
            self.main_screen_title_menu_submenu_ai_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"AI", command=lambda: My_Code_AI_Window())
            self.main_screen_title_menu_submenu_bash_terminal_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f">_", command=lambda: My_Code_bash_terminal.My_Code_bash_terminal())

        self.main_screen_title_menu_create_code_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"📝 (my coder)", command=self.__create_code__)
        self.main_screen_title_whisper_me_code_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"whisper me code", command=self.__code_explanation__)

        if locale.getdefaultlocale()[0] == f"sr_RS":
            self.main_screen_title_menu_submenu_create_code_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_title_menu_create_code_button, message=f"креирај код на основу вашег питања")
            self.main_screen_title_whisper_me_code_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_title_whisper_me_code_button, message=f"објасни ми шта ради код")

        elif locale.getdefaultlocale()[0] == f"ru_RU":
            self.main_screen_title_menu_submenu_create_code_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_title_menu_create_code_button, message=f"создать код на основе вашего вопроса")
            self.main_screen_title_whisper_me_code_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_title_whisper_me_code_button, message=f"объясни мне, что делает код")

        else:
            self.main_screen_title_menu_submenu_create_code_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_title_menu_create_code_button, message=f"create code based on user prompt")
            self.main_screen_title_whisper_me_code_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_title_whisper_me_code_button, message=f"explain me what code does")

        self.bind(f"<F1>", lambda event: self.main_screen_code_field.edit_undo())
        self.bind(f"<F2>", lambda event: self.main_screen_code_field.edit_redo())
        self.bind(f"<F3>", self.__open_code__)
        self.bind(f"<F4>", self.__save_code__)
        self.bind(f"<F5>", self.__run_code__)
        self.bind(f"<F6>", self.__delete_code__)
        self.bind(f"<F7>", lambda: My_Code_AI_Window())
        self.bind(f"<F8>", lambda event: My_Code_bash_terminal.My_Code_bash_terminal())
        self.bind(f"<F9>", lambda event: self.__create_code__())
        self.bind(f"<F10>", lambda event: self.__code_explanation__())
        
    @typing.override
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

    @typing.override     
    def __save_code__(self: typing.Self, event: str | None = None) -> None:
        try:
            self.file_name: tkinter.filedialog = tkinter.filedialog.asksaveasfilename(title=f"save python file", filetypes=[(f"Python file (*.py)", f"*.py")], defaultextension=[(f"Python file (*.py)", f"*.py")])

            with open(self.file_name, f"w+", encoding=f"UTF-8") as self.file:
                self.file_data: str = self.main_screen_code_field.get("1.0", tkinter.END)
                self.file.write(self.file_data)

        except Exception as exception: pass

    @typing.override
    def __open_code__(self: typing.Self, event: str | None = None) -> None:
        try:
            self.opened_name_file: tkinter.filedialog = tkinter.filedialog.askopenfilename(title=f"open python file", filetypes=[(f"Python file (*.py)", f"*.py")], defaultextension=[(f"Python file (*.py)", f"*.py")])

            with open(self.opened_name_file, f"r+", encoding=f"UTF-8") as self.openned_file: self.main_screen_code_field.insert(f"1.0", self.openned_file.read())

        except Exception as exception: pass
    
    def __drop_file_into_code_field__(self: typing.Self, event: str | None = None) -> None:
        self.main_screen_code_field.delete(f"1.0", tkinter.END)
        if event.data.endswith(f".py"):
            with open(event.data, f"r+", encoding=f"UTF-8") as self.openned_file: 
                self.main_screen_code_field.insert(f"1.0", self.openned_file.read())
                
        elif os.path.isfile(event.data):
            if locale.getdefaultlocale()[0] == f"sr_RS":
                tkinter.messagebox.showerror(title=f"грешка", message=f"то није python фајл")
                
            elif locale.getdefaultlocale()[0] == f"ru_RU":
                tkinter.messagebox.showerror(title=f"ошибка", message=f"это не python файл")
                
            else:
                tkinter.messagebox.showerror(title=f"error", message=f"this is not python file")

        else:
            self.main_screen_code_field.insert(f"1.0", event.data)

    @typing.override
    def __delete_code__(self: typing.Self, event: str | None = None) -> None:
        self.main_screen_code_field.delete(f"1.0", tkinter.END)

    def __code_explanation__(self: typing.Self, event: str | None = None) -> None:
        self.summary: str = My_Code_AI.My_Code_LM().__response__(pipe=SLM, query=f"<|system|>Explain the following code:<|end|><|user|>{self.main_screen_code_field.get(f"1.0", tkinter.END)}<|end|><|assistant|>")
        if locale.getdefaultlocale()[0] == f"sr_RS":
            tkinter.messagebox.showinfo(title=f"long story short", message=f"Резиме: {self.summary}")
        
        elif locale.getdefaultlocale()[0] == f"ru_RU":
            tkinter.messagebox.showinfo(title=f"long story short", message=f"Сводка: {self.summary}")
        
        else:
            tkinter.messagebox.showinfo(title=f"long story short", message=f"Summary: {self.summary}")

    def __create_code__(self: typing.Self, event: str | None = None) -> None:
        if locale.getdefaultlocale()[0] == f"sr_RS":
            self.code_prompt_input: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(title=f"нови код", text=f"унесите тему кода")
            self.code_prompt_input.after(250, lambda: self.code_prompt_input.iconbitmap(self.ICON))

        elif locale.getdefaultlocale()[0] == f"ru_RU":
            self.code_prompt_input: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(title=f"новый код", text=f"введите тему кода")
            self.code_prompt_input.after(250, lambda: self.code_prompt_input.iconbitmap(self.ICON))

        else:
            self.code_prompt_input: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(title=f"new code", text=f"enter code topic")
            self.code_prompt_input.after(250, lambda: self.code_prompt_input.iconbitmap(self.ICON))

        self.create_text: str = My_Code_AI.My_Code_LM().__response__(pipe=SLM, query=f"<|system|>Create python code based on user prompt:<|end|><|user|>{self.code_prompt_input.get_input()}<|end|><|assistant|>")
        self.main_screen_code_field.insert(f"1.0", self.create_text)
        
    def __exit__(self: typing.Self) -> None:
        if locale.getdefaultlocale()[0] == f"sr_RS":
            self.main_screen_exit: tkinter.messagebox = tkinter.messagebox.askyesno(title=f"излаз", message=f"желите да изађете?")
            if self.main_screen_exit: sys.exit()

        elif locale.getdefaultlocale()[0] == f"ru_RU":
            self.main_screen_exit: tkinter.messagebox = tkinter.messagebox.askyesno(title=f"выход", message=f"желайте выйти?")
            if self.main_screen_exit: sys.exit()
			
        else:
            self.main_screen_exit: tkinter.messagebox = tkinter.messagebox.askyesno(title=f"exit", message=f"would you like to exit?")
            if self.main_screen_exit: sys.exit()

class My_Code_AI_Window(customtkinter.CTkToplevel, My_Code_AI_window_interface.My_Code_AI_window_interface):

	TITLE: typing.Final[str] = f"My Code AI assistant (Copilot+PC edition)"
	HEIGHT: typing.Final[int] = 300
	WIDTH: typing.Final[int] = 525
	ICON: typing.Final[str] = f"My Code icon.ico"
	THEME: typing.Final[str] = f"system"

	def __init__(self: typing.Self, *args, **kwargs) -> None:
		customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

		self.title(self.TITLE)
		self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
		self.resizable(False, False)
		self.after(250, lambda: self.iconbitmap(self.ICON))

		self.ai_window_textbox: customtkinter.CTkTextbox = customtkinter.CTkTextbox(master=self, height=265, width=524, corner_radius=0, fg_color=f"transparent", text_color=(f"black", f"white"))
		self.ai_window_textbox.place(x=0, y=0)

		self.ai_window_textbox.configure(state=f"disabled")

		self.ai_window_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self, height=30, width=465, border_width=0, fg_color=f"transparent", placeholder_text=f"...")
		self.ai_window_entry.place(x=0, y=269)

		self.ai_window_microphone_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=30, width=30, border_width=0, fg_color=f"transparent", text=f"🎤", command=self.__audio_input__)
		self.ai_window_microphone_button.place(x=465, y=269)

		self.ai_window_send_request_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=30, width=30, border_width=0, fg_color=f"transparent", text=f"->", command=self.__response__)
		self.ai_window_send_request_button.place(x=495, y=269)

		self.ai_window_entry.bind(f"<Return>", self.__response__)

	@typing.override
	def __response__(self: typing.Self, configure: str | None = None) -> None:
		self.ai_window_entry_data: str = self.ai_window_entry.get()

		self.ai_window_textbox.configure(state=f"normal")
		self.query: str = My_Code_AI.My_Code_LM().__response__(pipe=SLM, query=f"<|system|>You are a helpful and experienced coder.<|end|><|user|>{self.ai_window_entry_data}<|end|><|assistant|>")

		self.ai_window_textbox.insert(tkinter.END, f"USER:\n{self.ai_window_entry_data}\nPhi3:\n{self.query}\n", f"-1.0")
		self.ai_window_textbox.configure(state=f"disabled")
		self.ai_window_entry.delete(f"-1", tkinter.END)

	def __audio_input__(self: typing.Self) -> None:
		self.recognizer: speech_recognition.Recognizer = speech_recognition.Recognizer()
		with speech_recognition.Microphone() as self.source:
			self.audio_data: speech_recognition.AudioData = self.recognizer.record(self.source, duration=5)
			self.text: str = self.recognizer.recognize_google(self.audio_data)

		self.ai_window_entry.insert(f"0", self.text)

if __name__ == f"__main__":
    program: Program = Program()
    program.mainloop()                   