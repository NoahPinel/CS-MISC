(**
  I found this website that contained what appears
  to be an assignment for a past course at umass.

  Provided the basic "group" laws, prove some basic
  lemmas...

 Link := https://people.cs.umass.edu/~arjun/courses/cs691pl-spring2014/assignments/groups.html

**)
Require Import Setoid.

(* The set of the group. *)
Parameter G : Set.

(* The binary operator. *)
Parameter f : G -> G -> G.

(* The group identity. *)
Parameter e : G.

(* The inverse operator. *)
Parameter i : G -> G.

(* For readability, we use infix <+> to stand for the binary operator. *)
Infix "<+>" := f (at level 50, left associativity).

(* The operator [f] is associative. *)
Axiom assoc : forall a b c, a <+> b <+> c = a <+> (b <+> c).

(* [e] is the right-identity for all elements [a] *)
Axiom id_r : forall a, a <+> e = a.

(* [i a] is the right-inverse of [a]. *)
Axiom inv_r : forall a, a <+> i a = e.

(* The identity [e] is unique. *)
Lemma unique_id : forall a, a <+> a = a -> a = e.
Proof.
  intros.
  assert (a <+> (i a) = a <+> (i a)).
  trivial.  
  rewrite <- H in H0 at 1.
  rewrite assoc in H0.
  rewrite inv_r in H0.
  rewrite id_r in H0.
  exact H0.
Qed.

(* [i a] is the left-inverse of [a]. *) 
Lemma left_inv :
forall a, i a <+> a = e.
Proof.
  intros.
