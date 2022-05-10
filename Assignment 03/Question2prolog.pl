nh(i,a,35).
nh(i,b,45).
nh(a,c,20).
nh(a,d,30).
nh(b,d,25).
nh(b,e,35).
nh(b,f,27).
nh(c,d,30).
nh(c,g,47).
nh(d,g,30).
nh(e,g,25).
distanceLength(X,Y,L):-
 nh(X,Y,L),!.
distanceLength(X,Y,L):-
 nh(X,Z,L1), distanceLength(Z,Y,L2), L is L1+L2.
