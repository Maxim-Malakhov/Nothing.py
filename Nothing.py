'''There is really Nothing!'''
class Nothing(object):
    '''A basic class of all...'''
    def __init__(self, *args, **kwargs):
        '''Does nothing...'''
        for method in ["__add__", "__sub__", "__mul__", "__floordiv__", "__div__", "__truediv__", "__mod__", "__divmod__", "__pow__", "__lshift__", "__rshift__", "__and__", "__or__", "__xor__", "__radd__", "__rsub__", "__rmul__", "__rfloordiv__", "__rdiv__", "__rtruediv__", "__rmod__", "__rdivmod__", "__rlshift__", "__rrshift__", "__rand__", "__ror__", "__rxor__", "__iadd__", "__isub__", "__imul__", "__ifloordiv__", "__idiv__", "__itruediv__", "__imod__", "__ipow__", "__ilshift__", "__irshift__", "__iand__", "__ior__", "__ixor__"]:
            setattr(self.__class__, method, classmethod(lambda self, other: other))
        for method in ["__cmp__", "__eq__", "__ne__", "__lt__", "__gt__", "__le__", "__ge__"]:
            setattr(self.__class__, method, classmethod(lambda self, other: False))
        for method in ["__int__", "__long__", "__float__", "__complex__", "__oct__", "__hex__", "__index__", "__trunc__"]:
            setattr(self.__class__, method, classmethod(lambda self: self))
    @classmethod
    def __len__(self):
        return
    @classmethod
    def __sizeof__(self):
        return
    @classmethod
    def __str__(self):
        return "This is really Nothing!"
    @classmethod
    def __repr__(self):
        return f'I said: "{self.__str__()}"'
    def nothing(self, *args, **kwargs):
        '''Return Nothing...'''
        return self
