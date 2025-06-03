from typing import Protocol


class SymbolGenerator[T](Protocol):
    def generate_symbol(self) -> T: ...
