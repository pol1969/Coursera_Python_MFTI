from test_decorator import *

def visio(d):
    print(d.__class__.__name__)
    print(d.get_stats())
    print(d.get_positive_effects())
    print(d.get_negative_effects())


h = Hero()
print("h = Hero()")
visio(h)

#e = EvilEye(h)
#visio(e)
#
#e1 = EvilEye(e)
#visio(e1)
#
#e2 = EvilEye(e1)
#visio(e2)
#
#e2.base = e
#visio(e2)
#
#b = Blessing(e2)
#visio(b)
#
#b.base = h
#visio(b)
#



b = Berserk(h)
visio(b)

b2 = Berserk(b)
visio(b2)

b3 = Berserk(b2)
visio(b3)

b3.base = b 
visio(b3)



