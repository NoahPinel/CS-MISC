lemma or_symm (P Q : Prop) : P ∨ Q → Q ∨ P :=

begin
	intro h,
	cases h with p q,
	--{cc,
	--left,
	--exact q}, This is faster but I dont get why it works
	right,
	exact p,

	left,
	exact q,
end
