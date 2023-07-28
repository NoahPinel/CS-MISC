-- New tactic, cases

begin
	intro h,
	-- h : P ∧ Q
	-- ⊢ Q ∧ P

	cases h with p q,
	-- p : P,
	-- q : Q
	-- ⊢ Q ∧ P
	split,
	exact q,
	exact p,
end
