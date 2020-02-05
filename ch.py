class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class NullHandler:
    pass


class IntHandler(NullHandler):
    pass


class FloatHandler(NullHandler)::
    pass


class StrHandler(NullHandler)::
    pass

class EventGet:
    pass

class EventSet:
    pass

obj = SomeObject()
obj.integer_field = 42
obj.float_field = 3.14
obj.string_field = "some text"


chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
assert(chain.handle(obj, EventGet(int))==42)
assert(chain.handle(obj, EventGet(float))==3.14)
assert(chain.handle(obj, EventGet(str))=='some text')
chain.handle(obj, EventSet(100))
assert(chain.handle(obj, EventGet(int))==100)
chain.handle(obj, EventSet(0.5))
assert(chain.handle(obj, EventGet(float))==0.5)
chain.handle(obj, EventSet('new text'))
assert(chain.handle(obj, EventGet(str))=='new text')
