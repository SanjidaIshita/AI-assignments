%data
%
neighbor(a,d,7).
neighbor(d,c,2).
neighbor(c,e,3).
neighbor(e,i,4).
neighbor(e,h,3).
neighbor(h,g,6).
neighbor(g,f,4).
neighbor(g,b,1).




path(X,Y,D):-
    neighbor(X,Y,D), !.

path(X,Y,D):-
    neighbor(X,Z,D1),path(Z,Y,D2), D is D1+D2.

mainfunc:-
    write('Start Node: '), read(X),
    write('End Node: '), read(Y),
    write('Distance: '),path(X,Y,D), write(D),
    tab(2),fail.

