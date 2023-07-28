lemma iff_trans (P Q R : Prop) : (P ↔ Q) → (Q ↔ R) → (P ↔ R) :=

begin
	-- cc, Cheeky finish
	
	intro h,
	cases h with hpq hqp,
	intro t,
	cases t with h1 h2,
	split,
	-- hpq : P → Q,
	-- hqp : Q → P,
	-- h1 : Q → R,
	-- h2 : R → Q

	-- ⊢ P → R
	intro p,
	apply h1,
	apply hpq,
	exact p,

	-- ⊢ R → P
	intro r,
	apply hqp,
	apply h2,
	exact r,
end
