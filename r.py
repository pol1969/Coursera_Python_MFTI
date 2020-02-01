from test_decorator import *
h = Hero()
#print("h.get_stats()",h.get_stats())
b = Berserk(h)
#print("Berserk get_stats ",b.get_stats())
#print("Berserk get_positive_effects ",b.get_positive_effects())
b2 = Berserk(b)
#print("B2 get_stats()",b2.get_stats())
#print("B2 get_positive_effects ",b2.get_positive_effects())

print(f"before assignment") 

print("b2.get_stats()",b2.get_stats())
print("b2.get_positive_effects()",b2.get_positive_effects())

b2.base = h
print(f"after assignment") 

print("b2.get_stats()",b2.get_stats())
print("b2.get_positive_effects()",b2.get_positive_effects())

