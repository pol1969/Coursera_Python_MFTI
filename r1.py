from decomb import *
from pprint import pprint
h = Hero()
#pprint(h.get_positive_effects())
#pprint(h.get_negative_effects())
#pprint(h.get_stats())



e = EvilEye(h)
e1 = EvilEye(e)
e2 = EvilEye(e1)
e3 = EvilEye(e2)
e4 = EvilEye(e3)

e3.base = e1


pprint(e4.get_positive_effects())
pprint(e4.get_negative_effects())

pprint(e4.get_stats())
    
