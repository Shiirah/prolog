% Faits
homme('pierre').
homme('marc').
homme('paul').
homme('jacques').
femme('marie').
femme('sophie').
femme('julie').

parent('pierre', 'paul').
parent('marie', 'paul').
parent('marc', 'sophie').
parent('jacques', 'marc').
parent('julie', 'sophie')

% Règles
mere(X, Y) :- femme(X), parent(X, Y).
pere(X, Y) :- homme(X), parent(X, Y).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
frereetsoeur(X, Y) :- parent(X, Z), parent(Y, Z), X \=Y.
longueur([], 0).
longueur([_ | Queue], N) :- longueur(Queue, M), N is M + 1.
present(X, [X | _]).
present(X, [_ | Q]) :- present(X, Q), !.
oncletante(X, Y) :- frereetsoeur(X, Z), parent(Z, Y).
cousin(X, Y) :- parent(Z, X,), frereetsoeur(Z, W), parent(W, Y).