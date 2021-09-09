from hw1 import *

alt_sum = [
    (15, 5, [15, 30, 60, 75, 105]),
    (28, 10, [28, 56, 112, 140, 196, 308, 448, 644, 952, 1400]),
    (-1, 5, []),
    (15, 4, []),
]

for t in alt_sum:
    print("test alternative_sum(%s, %s)" % (t[0], t[1]))
    r = alternative_sum(t[0], t[1])
    try:
        assert(r == t[2])
        print("  pass")
    except:
        print("  fail")

ord_s = ["Shawn", "Samuel", "Allen", "Mabel", "Ian", "Clayton", "Ethan", "Kate", "Nicholas", "Mable"]
assert(order_scores() == ord_s)
print()
print("order_scores() test ok")

