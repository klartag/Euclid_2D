from ..terms.basic_function_term import BasicFunctionTerm


class TokenTracker[T]:
    tokens: list[T | BasicFunctionTerm[T]]
    reverse_tokens: dict[T | BasicFunctionTerm[T], int]
    
    def __init__(self):
        self.tokens = []
        self.reverse_tokens = {}
    
    def add(self, value: T | BasicFunctionTerm[T]):
        if value in self.reverse_tokens:
            return
        key = len(self.tokens)
        self.tokens.append(value)
        self.reverse_tokens[value] = key
