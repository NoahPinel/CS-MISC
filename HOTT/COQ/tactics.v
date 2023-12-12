
(** 
  reflexivity

Use of form x = x
It does not need to be
syntactically == it just
needs both sides to eval
to the same thing.
 **)
Lemma you_are_you :
forall x : Set,
x = x.
Proof.
  intro.
  reflexivity.
Qed.

Inductive nat : Set :=
  | O
  | S : nat -> nat.

Fixpoint add (x y : nat) : nat :=
  match x with
  | O => y
  | S n => S (add n y)
  end.

(** (3 + 2) = (1 + 4) **)
Lemma real_maths:
(
add (S (S (S O))) (S (S O))
=
add (S O) (S (S (S (S O))))
).
Proof.
  reflexivity.
Qed.

(** 
   assumption
Tactic to be used when your goal
is allready in the same context
 **)
Lemma you_imply_you_imply_you :
forall p : Prop,
p -> p -> p.
Proof.
  intros.
  assumption.
Qed.

(** constructor **)
Inductive is_even : nat -> Prop :=
| even_O : is_even O
| even_S : forall n, is_even n -> is_even (S (S n)).

Lemma is_zero_even :
is_even O.
Proof.
  constructor.
Qed.

Lemma is_two_even :
is_even (S (S O)).
Proof.
  constructor.
  apply is_zero_even.
Qed.

Lemma is_four_even :
is_even (S (S (S (S O)))).
Proof.
  constructor.
  apply is_two_even.
Qed.

(** apply **)

Lemma modus_ponens :
forall p q : Prop, (p -> q) -> p -> q.
Proof.
  intros.
  apply H in H0.
  exact H0.
Qed.

(** subst **)

Inductive bool : Set :=
  | true
  | false.

Lemma eq_comm :
forall (x y : bool), x = y -> y = x.
Proof.
  intros.
  subst.
  reflexivity.
Qed.

(** rewrite **)

Lemma func_eq_comm :
forall (f : bool -> bool) x y,
(f x) = (f y) -> (f y) = (f x).
Proof.
  intros.
  rewrite H.
  reflexivity.
Qed.

Lemma func_eq_trans :
forall (f : bool -> bool) x y z,
(f x) = (f y) -> 
(f y) = (f z) -> 
(f z) = (f z).
Proof.
  intros.
  rewrite <- H in H0.
  reflexivity.
Qed.
