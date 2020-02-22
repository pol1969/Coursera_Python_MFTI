my_float, my_int, my_str = "float","int","str"

class NullHandler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, obj, event):

        if self._successor is not None:
            return self._successor.handle(obj, event)

class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == my_int:
            if event.pr is None:
                return obj.integer_field
            else:
                obj.integer_field = event.pr
        else:
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):

        if event.kind == my_float:
            if event.pr is None:
                return obj.float_field
            else:
                obj.float_field = event.pr
        else:
            return super().handle(obj, event)




class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == my_str:
            if event.pr is None:
                return obj.string_field
            else:
                obj.string_field = event.pr
        else:
            return super().handle(obj, event)




class EventGet:
    def __init__(self, pr):
        self.kind = {int:my_int, float:my_float, str:my_str}[pr]
        self.pr = None


class EventSet:
    def __init__(self, pr):
        self.kind = {int:my_int, float:my_float, str:my_str}[type(pr)]
        self.pr = pr


