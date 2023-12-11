Inductive day : Type :=
  | Monday
  | Tuesday
  | Wednesday
  | Thursday
  | Friday
  | Saturday
  | Sunday.

Definition next_weekday (d : day) : day :=
  match d with
  | Monday => Tuesday
  | Tuesday => Wednesday
  | Wednesday => Thursday
  | Thursday => Friday
  | Friday => Monday
  | Saturday => Monday
  | Sunday => Monday
  end.

Compute (next_weekday Sunday).

Compute (next_weekday (next_weekday Saturday)).

Example test_next_weekday :
  (next_weekday (next_weekday Tuesday)) = Thursday.

Proof. 
  simpl.
  reflexivity.
Qed.
