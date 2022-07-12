class NonPositiveDigitException(ValueError):
    pass
class Square:
    _a = None
    def __init__(self, a):
        self.a = a
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError('Число должно быть положительным')
    @property
    def area(self):
        return self.a ** 2
