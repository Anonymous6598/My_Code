from customtkinter import *
import My_Code_AI, My_Code_AI_window_interface, typing, asyncio, tkinter

class AI_Window(CTkToplevel, My_Code_AI_window_interface.My_Code_AI_window_interface):

	TITLE: typing.Final[str] = f"My Code AI assistant"
	HEIGHT: typing.Final[int] = 300
	WIDTH: typing.Final[int] = 525
	ICON: typing.Final[str] = f"My Code icon.ico"
	THEME: typing.Final[str] = f"system"

	def __init__(self: typing.Self, *args, **kwargs) -> None:
		CTkToplevel.__init__(self, *args, **kwargs)

		self.title(self.TITLE)
		self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
		self.resizable(False, False)
		self.after(250, lambda: self.iconbitmap(self.ICON))

		self.ai_window_textbox: CTkTextbox = CTkTextbox(master=self, height=265, width=524, corner_radius=0, fg_color=f"transparent")
		self.ai_window_textbox.place(x=0, y=0)

		self.ai_window_textbox.configure(state=f"disabled")

		self.ai_window_entry: CTkEntry = CTkEntry(master=self, height=30, width=524, border_width=0, fg_color=f"transparent", placeholder_text=f"...")
		self.ai_window_entry.place(x=0, y=269)

		self.ai_window_entry.bind(f"<Return>", self.__response__)

	@typing.override
	def __response__(self: typing.Self, configure: str | None = None) -> None:
		self.ai_window_entry_data: str = self.ai_window_entry.get()

		self.ai_window_textbox.configure(state=f"normal")
		self.query: str = asyncio.run(My_Code_AI.My_Code_LM().__response__(self.ai_window_entry_data))

		self.ai_window_textbox.insert(tkinter.END, f"{self.query}\n", f"-1.0")
		self.ai_window_textbox.configure(state=f"disabled")
		self.ai_window_entry.delete(f"-1", tkinter.END)

