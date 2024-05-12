from typing import TextIO, Callable

class Archiwith:
    def __init__(self, file_path: str) -> Callable:
        """
        :param file_path: Path to your file.
        """
        self.file_path: str = file_path
    
    def abrir(self, binari: bool = False) -> TextIO:
        """
        :param binari: Set it to True if the file to be read is binary. Default False.
        """
        if binari:
            self.file = open(self.file_path, 'rb')
        else:
            self.file = open(self.file_path, 'r')
        self._with = True
        return self.file
    
    def escribir(self) -> TextIO:
        self.file = open(self.file_path, 'w')
        self._with = True
        return self.file
    
    def leer(self) -> str:
        self.file = open(self.file_path, 'r').read()
        self._with = False
        return self.file
    
    def __exit__(self):
        if self._with:
            self.file.close()