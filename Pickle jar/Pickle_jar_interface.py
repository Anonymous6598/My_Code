import abc

class Pickle_jar_interface(abc.ABC):
    
    @abc.abstractmethod
    def __undo__(self) -> None:
        pass
    
    @abc.abstractmethod
    def __redo__(self) -> None:
        pass
    
    @abc.abstractmethod
    def __save_file__(self) -> None:
        pass
   
    @abc.abstractmethod
    def __open_file__(self) -> None:
        pass


