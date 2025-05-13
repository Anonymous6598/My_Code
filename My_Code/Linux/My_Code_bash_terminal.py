import customtkinter, tkterm, typing

class My_Code_bash_terminal(customtkinter.CTkToplevel):
    
    TITLE: typing.Final[str] = f"My Code Bash window"
    
    def __init__(self: typing.Self, *args, **kwargs):
        customtkinter.CTkToplevel.__init__(self, *args, **kwargs)
        
        self.title(self.TITLE)

        self.bash_terminal: tkterm.Terminal = tkterm.Terminal(self)
        self.bash_terminal.shell = True
        self.bash_terminal.pack(expand=True, fill=f"both")