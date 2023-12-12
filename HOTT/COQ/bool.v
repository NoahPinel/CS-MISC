(**
  This file starts from a raw boolean type, (True False)
  
  From this, we are able to construct all the familiar 
  boolean operations, such as; negate, and, or, nand...
   
  With these defined, we then are able to use Coq to validate
  the validation is correct!
   
  After the "tools" are built and proved, I go on to 
  show the construction of many Tautologies and Logical Equivalences
  that are very common in Propositional logic.
     
**)

Inductive bool : Type :=
  | true
  | false.

Definition negateb (b : bool) : bool :=
  match b with
  | true => false
  | false => true
  end.

Definition andb (a : bool) (b : bool) : bool :=
  match a with 
  | true => b
  | false => false
  end.

(** 
   Lets prove that AND is correct
  
    P   Q  | P AND Q
    T   T  |    T   
    T   F  |    F   
    F   T  |    F   
    F   F  |    F   
 **)

Example and_row1 : (andb true true) = true.
Proof.
  simpl.
  reflexivity.
Qed.

Example and_row2 : (andb true false) = false.
Proof.
  simpl.
  reflexivity.
Qed.

Example and_row3 : (andb false true) = false.
Proof.
  simpl.
  reflexivity.
Qed.

Example and_row4 : (andb false false) = false.
Proof.
  simpl.
  reflexivity.
Qed.


(** Note the packing of params -- Very nice...**)

Definition orb (a b : bool) : bool :=
  match a with
  | true => true
  | false => b
  end.

(** 
   Lets prove that OR is correct
  
    P   Q  | P or Q
    T   T  |    T   
    T   F  |    T   
    F   T  |    T   
    F   F  |    F   
 **)

Example or_row1 : (orb true true) = true.
Proof.
  simpl.
  reflexivity.
Qed.

Example or_row2 : (orb true false) = true.
Proof.
  simpl.
  reflexivity.
Qed.

Example or_row3 : (orb false true) = true.
Proof.
  simpl.
  reflexivity.
Qed.

Example or_row4 : (orb false false) = false.
Proof.
  simpl.
  reflexivity.
Qed.

Notation "a && b" := (andb a b).
Notation "a || b" := (orb a b).

Example or_comp : false || false || true = true.
Proof.
  simpl.
  reflexivity.
Qed.

Definition nandb (a b : bool) : bool :=
  match a with
  | false => true
  | true =>
      match b with
      | false => true
      | true => false
      end
  end.

(** 
   Lets prove that NAND is correct
  
    P   Q  | P NAND Q
    T   T  |    F   
    T   F  |    T   
    F   T  |    T   
    F   F  |    T   

**)

Example nand_row1 : (nandb true true) = false.
Proof.
  simpl.
  reflexivity.
Qed.


Example nand_row2 : (nandb true false) = true.
Proof.
  simpl.
  reflexivity.
Qed.


Example nand_row3 : (nandb false true) = true.
Proof.
  simpl.
  reflexivity.
Qed.


Example nand_row4 : (nandb false false) = true.
Proof.
  simpl.
  reflexivity.
Qed.


Definition implyb (a b : bool) : bool :=
  match a with
  | true => b 
  | false => true
  end.

(** 
   Lets prove that -> is correct
  
   P   Q  | P -> Q
    T   T  |    T   
    T   F  |    F   
    F   T  |    T   
    F   F  |    T   
 **)

Example imp_row1 : (implyb true true) = true.
Proof.
  simpl.
  reflexivity.
Qed.


Example imp_row2 : (implyb true false) = false.
Proof.
  simpl.
  reflexivity.
Qed.


Example imp_row3 : (implyb false true) = true.
Proof.
  simpl.
  reflexivity.
Qed.

Example imp_row4 : (implyb false false) = true.
Proof.
  simpl.
  reflexivity.
Qed.


Definition iffb (a b : bool) : bool :=
  match a with
  | true => b 
  | false =>
      match b with 
      | true => false
      | false => true
      end
  end.

(** 
   Lets prove that iff is correct
  
    P   Q  | P iff Q
    T   T  |    T   
    T   F  |    F   
    F   T  |    F  
    F   F  |    T   
 **)

Example iff_row1 : (iffb true true) = true.
Proof.
  simpl.
  reflexivity.
Qed.


Example iff_row2 : (iffb true false) = false.
Proof.
  simpl.
  reflexivity.
Qed.


Example iff_row3 : (iffb false true) = false.
Proof.
  simpl.
  reflexivity.
Qed.

Example iff_row4 : (iffb false false) = true.
Proof.
  simpl.
  reflexivity.
Qed.

(** 
   ~P AND (P --> Q) 

    P        Q      ~P AND (P --> Q)
    T        T             F    
    T        F             F
    F        T             T
    F        F             T

 **)
Definition P_T : bool := true.
Definition P_F : bool := false.

Definition Q_T : bool := true.
Definition Q_F : bool := false.

Example comp_row1 : negateb P_T && implyb P_T Q_T = false.
Proof.
  simpl.
  reflexivity.
Qed.

Example comp_row2 : negateb P_T && implyb P_T Q_F = false.
Proof.
  simpl.
  reflexivity.
Qed.

Example comp_row3 : negateb P_F && implyb P_F Q_T = true.
Proof.
  simpl.
  reflexivity.
Qed.

Example comp_row4 : negateb P_F && implyb P_F Q_F = true.
Proof.
  simpl.
  reflexivity.
Qed.


(** 
    P        Q      (P --> Q) or (Q --> P)
    T        T             T    
    T        F             T
    F        T             T
    F        F             T

 **)

Example Taut_row1 : implyb P_T Q_T || implyb Q_T P_T = true.
Proof.
  tauto.
Qed.

Example Taut_row2 : implyb P_T Q_F || implyb Q_F P_T = true.
Proof.
  tauto.
Qed.


Example Taut_row3 : implyb P_F Q_T || implyb Q_T P_F = true.
Proof.
  simpl.
  reflexivity.
Qed.


Example Taut_row4 : implyb P_F Q_F || implyb Q_F P_F = true.
Proof.
  reflexivity.
Qed.

(** Some more tautologies and logical equivalences **)

(** Double negation : ~(~p) iff p **) 
Example dbl_negate_pos : iffb (negateb (negateb P_T)) P_T = true.
Proof.
  simpl.
  reflexivity.
Qed.

(** Double negation : ~(~p) iff p **)
Example dbl_negate_neg : iffb (negateb (negateb P_F)) P_F = true.
Proof.
  simpl.
  reflexivity.
Qed.

(** 
   DeMorgan's Law ~(p \/ q) <-> (~p /\ ~q) 
      p	q	| (¬(p ∨ q) ↔ (¬p ∧ ¬q))
      F	F             T
      F	T             T
      T	F             T
      T	T             T

 **)

Theorem DeMorgan_or : 
forall (p q : bool), iffb (negateb (p || q)) (negateb p && negateb q) = true.
Proof.
  intros p q.
  destruct p, q;
  reflexivity.
Qed.

Theorem DeMorgan_and : 
forall (p q : bool), iffb (negateb (p && q)) (negateb p || negateb q) = true.
Proof.
  intros p q.
  destruct p, q;
  reflexivity.
Qed.

(** 
  Contrapositive : (p->q) <-> (~q -> ~p)

   p	q   ((p → q) ↔ (¬q → ¬p))
   F	F             T
   F	T             T
   T	F             T
   T	T             T
**)

Theorem Contrapositive : 
forall (p q : bool), iffb (implyb p q) (implyb (negateb q) (negateb p)) = true.
Proof.
  intros p q.
  destruct p, q;
  reflexivity.
Qed.

(**
  Modus ponens : (p /\ (p->q)) -> q
   p	q	((p ∧ (p → q)) → q)
   F	F           T
   F	T           T
   T	F           T
   T	T           T
**)

Theorem Modus_ponens : 
forall (p q : bool), implyb (p && (implyb p q)) (q) = true.
Proof.
  intros p q.
  destruct p, q;
  reflexivity.
Qed.

(**
  Modus tollens : (~q /\ (p->q)) -> ~p
   p	q	((~q ∧ (p → q)) → ~p)
   F	F           T
   F	T           T
   T	F           T
   T	T           T
**)

Theorem Modus_tollens : 
forall (p q : bool), implyb (negateb q && (implyb p q)) (negateb p) = true.
Proof.
  intros p q.
  destruct p, q;
  reflexivity.
Qed.

(**
  Lets try and use our theorems!

   ~(p \/ ~q) <-> ~p /\ q

   The proof looks like:
   ~(p \/ ~q) <-> ~p /\ ~~ q (DeMorgan)
              <-> ~p /\ q .
**)



Example Equate_ex1 : 
forall (p q : bool), 
iffb (negateb (p || negateb q)) ((negateb p) && negateb (negateb q)) = true. 
Proof.
  intros p q.
  apply DeMorgan_or.
Qed.


Example Equate_ex2 :
forall (p q : bool),
implyb (negateb p && negateb (negateb q)) (negateb p && q) = true. 
Proof.
  intros p q.
  destruct p, q;
  reflexivity.
Qed.


Example  Equate_ex3:
forall (p q : bool),
iffb (negateb (p || negateb q)) (negateb p && q) = true.
Proof.
  intros p q.
  destruct p, q;
  reflexivity.
Qed.

(** Transitivity for BOOL and PROP **)
Theorem transitivity_bool : 
forall (p q r : bool), implyb ((implyb p q) && (implyb q r)) (implyb p r) = true.
Proof.
  intros p q r.
  destruct p, q, r;
  reflexivity.
Qed.

Theorem transitivity_prop : 
forall (p q r : Prop), ((p -> q) /\ (q -> r)) -> (p -> r).
Proof.
  intros p q r hyp.
  destruct hyp as [h1 h2].
  intro h.
  apply h2.
  apply h1.
  apply h.
Qed.

(** Lets prove commutativity for /\ and \/ **)

Theorem and_commutes :
forall (p q : bool), implyb (p && q) (q && p) = true.
Proof.
  intros p q.
  destruct p, q;
  reflexivity.
Qed.

Theorem or_commutes :
forall (p q : bool), implyb (p || q) (q || p) = true.
Proof.
  intros p q.
  destruct p, q;
  reflexivity.
Qed.

(** Associativity for /\ and \/ **)

Theorem and_assoc :
forall (p q r : bool), implyb ((p && q) && r) (p && (q && r)) = true.
Proof.
  intros p q r.
  destruct p, q, r;
  reflexivity.
Qed.

Theorem or_assoc :
forall (p q r : bool), implyb ((p || q) || r) (p || (q || r)) = true.
Proof.
  intros p q r.
  destruct p, q, r;
  reflexivity.
Qed.

(** Distributivity for /\ and \/ **)

Theorem and_distr :
forall (p q r : bool), implyb (p && (q || r)) ((p && q) || (p && r)) = true.
Proof.
  intros p q r.
  destruct p, q, r;
  reflexivity.
Qed.

Theorem or_distr :
forall (p q r : bool), implyb (p || (q && r)) ((p || q) || (p || r)) = true.
Proof.
  intros p q r.
  destruct p, q, r;
  reflexivity.
Qed.

(** Simplification for /\ and \/ **)

Theorem and_simp :
forall (p : bool),
iffb (p && p) (p) = true.
Proof.
  intro p.
  destruct p;
  reflexivity.
Qed.
 
Theorem or_simp :
forall (p : bool),
iffb (p || p) (p) = true.
Proof.
  intro p.
  destruct p;
  reflexivity.
Qed.
 
(** Disjunctive syllogism **)

Theorem dis_syll :
forall (p q : bool),
implyb ((p || q) && negateb p) (q) = true.
Proof.
  intros p q.
  destruct p, q;
  reflexivity.
Qed.
