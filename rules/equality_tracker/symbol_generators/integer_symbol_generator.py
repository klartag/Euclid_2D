from .symbol_generator import SymbolGenerator


class IntegerSymbolGenerator(SymbolGenerator[int]):
    previous_symbol: int = -1

    def generate_symbol(self) -> int:
        self.next_symbol += 1
        return self.next_symbol
