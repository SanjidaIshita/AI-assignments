nh = [('i', 'a', 35), ('i', 'b', 45), ('a', 'c', 20), ('a',
'd', 30),
 ('b', 'd', 25), ('b', 'e', 35), ('b', 'f', 27),
 ('c', 'd', 30), ('c', 'g', 47), ('d', 'g', 30), ('e',
 'g', 25)]
v = [0] * len(nh)

def distanceLength(X, Y, L=[]):
 if X == Y:
    total_weight = sum(L)
    print("The Length: ", total_weight)
    return

 i = 0
 child = ''
 while i <= len(nh) - 1:
    if v[i] == 0 and nh[i][0] == X:
        v[i] = 1
        child = nh[i][1]
        L.append(nh[i][2])
        distanceLength(child, Y)
    i = i + 1
 if len(L) >= 1:
    L.pop()

start = str(input('Starting Node: '))
finish = str(input('Finishing Node: '))
distanceLength(start, finish)
