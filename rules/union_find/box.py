class Box[T]:
    """
    A class that is effectively just a pointer to an object.
    """

    inner: T

    def __init__(self, value: T):
        self.inner = value

    def __eq__(self, other: 'Box[T]'):
        return self.inner == other.inner
