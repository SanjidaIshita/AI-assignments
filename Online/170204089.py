gtp=[
    (1,1,1),
    (2,3,1),
    (3,1,2),
    (4,3,2),
    (5,1,3),
    (6,2,3),
    (7,2,2),
    (8,3,3)
    ]

gblnk=(2,1)

tp=[
    (1,1,1),
    (2,2,1),
    (3,3,1),
    (4,1,2),
    (5,2,2),
    (6,3,2),
    (7,1,3),
    (8,2,3)
    ]

blnk=(3,3)

i=0
h=0

while(i<=7):
    if((gtp[i][1] != tp[i][1]) or (gtp[i][2] != tp[i][2])):
        h=h+1
    i=i+1

print("Heuristic 1 : ",h)
