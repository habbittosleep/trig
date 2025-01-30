class TLogElement:
    """Базовый класс для логического элемента."""
    def __init__(self):
        self.__in1 = 0
        self.__in2 = 0
        self._res = 0
        if hasattr(self, "_calc"):
            pass
        else:
            raise NotImplementedError("This object cannot be created!!!")

    def __setIn1(self, newIn1):
        if newIn1 in (0, 1):
            self.__in1 = newIn1
            self._calc()

    def __setIn2(self, newIn2):
        if newIn2 in (0, 1):
            self.__in2 = newIn2
            self._calc()

    In1 = property(lambda x: x.__in1, __setIn1)
    In2 = property(lambda x: x.__in2, __setIn2)
    Res = property(lambda x: x._res)

class TNot(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = int(not(self.In1))

class TAnd(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = self.In1 * self.In2

class TOr(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = self.In1 or self.In2

class TEq(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = int(self.In1 == self.In2)

class TXor(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = self.In1 ^ self.In2

class TImp(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = int(self.In1 <= self.In2)

class TNand(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = int(not(self.In1 * self.In2))

class TNor(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = int(not(self.In1 or  self.In2))

class TTrigger(TLogElement):
    def __init__(self, q):
        TLogElement.__init__(self)
        self.q = q

    def _calc(self):
        if self.q == 1:
            if self.In1 >= self.In2:
                self._res = 1
            else:
                self._res = 0
        elif self.q == 0:
            self._res = self.In1 + (self.In2 and self.q)