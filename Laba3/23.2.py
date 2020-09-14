import math


def find_farthest_orbit(list_of_orbits):
    max_s = list_of_orbits[0][0] * list_of_orbits[0][1] * math.pi
    for i in list_of_orbits:
        if i[0] * i[1] * math.pi > max_s and i[0] != i[1]:
            max_s = i[0] * i[1] * math.pi

    for i in list_of_orbits:
        if i[0] * i[1] * math.pi == max_s:
            return [i[0], i[1]]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
