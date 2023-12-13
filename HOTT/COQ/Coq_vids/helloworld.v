Definition succ (n : nat) : nat :=
  S n.

Definition pred (n : nat) : nat :=
  match n with
    | O => O
    | S n' => n'
  end.


Eval compute in (pred 4).
Eval compute in (pred (succ (succ (succ O)))).
