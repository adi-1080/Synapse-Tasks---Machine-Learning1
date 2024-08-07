gadgets = [
    ("Explosive Batarangs", 3, True),
    ("Batarangs", 5, True),
    ("Smoke Pellets", 0, False),
    ("Tear Gas Grenades", 2, True),
    ("Night Vision Googles", 1, True),
    ("Batclaw", 0, False),
    ("Grapple Gun", 3, True),
    ("Batsignal", 0, False),
    ("Utility Belt", 1, True),
    ("Batmobile Tires", 4, True),
]

from operator import itemgetter

# k = itemgetter(1)

# print(list(map(k, gadgets)))




sorted_gadgets = sorted(gadgets, key=itemgetter(1,0), reverse=True)

for each_gadget in sorted_gadgets:
    print(each_gadget)