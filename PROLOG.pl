male(jack).
male(rex).
female(daisy).
female(rose).

parent_of(jack,rex).
parent_of(jack,daisy).
parent_of(rose, rex).

father_of(X,Y):- male(X),
    parent_of(X,Y).

mother_of(X,Y):- female(X),
    parent_of(X,Y).
