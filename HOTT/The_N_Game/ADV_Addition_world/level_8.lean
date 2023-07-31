lemma eq_zero_of_add_right_eq_self {a b : mynat} : a + b = a → b = 0 :=

begin
	induction a with k hyp,
	rw zero_add,
	cc,

	rw succ_add,
	rw succ_eq_succ_iff,
	exact hyp,
end 
