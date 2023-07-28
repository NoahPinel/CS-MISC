lemma and_trans (P Q R : Prop) : P ∧ Q → Q ∧ R → P ∧ R :=

begin
	intros h h1,
	-- h : P ∧ Q
	-- h1 : Q ∧ R
	split,
	-- ⊢ P
	cases h with p q,
	exact p,

	-- ⊢ Q
	cases h1 with p r,
	exact r,
end
