class Value:
    def __init__(self):
        self.val = 0

    def __get__(self, obj, obj_type):
        return self.val

    def __set__(self, obj, value):
        if (obj.commission >= 0) and (obj.commission <= 1):
            self.val = value - value*obj.commission
        else:
            self.val = value
        #    print('Значение комиссии д. б. от 0 до 1')



   
