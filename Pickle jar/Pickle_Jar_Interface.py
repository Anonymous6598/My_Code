import abc, typing

class Pickle_Jar_Interface(abc.ABC):
    
    @abc.abstractmethod
    def __run_code__(self: typing.Self, event: str | None = None) -> None:
        pass

    @abc.abstractmethod
    def __save_code__(self: typing.Self, event: str | None = None) -> None:
        pass
    
    @abc.abstractmethod
    def __open_code__(self: typing.Self, event: str | None = None) -> None:
        pass
    
    @abc.abstractmethod
    def __delete_code__(self: typing.Self, event: str | None = None) -> None:
        pass
    
    @abc.abstractmethod
    def __open_ai_window__(self: typing.Self, event: str | None = None) -> None:
        pass

