import abc, typing

class My_Code_AI_window_interface(abc.ABC):

   @abc.abstractmethod
   def __response__(self: typing.Self, prompt: str) -> None:
       pass

   @abc.abstractmethod
   def __audio_input__(self: typing.Self) -> None:
       pass
