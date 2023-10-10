import abc

class Pickle_jar_settings_window_interface(abc.ABC):
    
    @abc.abstractmethod
    def __change_language__(self) -> None:
        pass
    
    @abc.abstractmethod
    def __change_text_color__(self) -> None:
        pass
    
    @abc.abstractmethod
    def __change_button_color__(self) -> None:
        pass




