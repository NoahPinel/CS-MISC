lemma add_succ_zero (a : mynat) : a + succ(0) = succ(a) :=

begin
	rw add_succ,
	-- We get 
	-- ⊢ succ (a + 0) = succ a

	-- ⊢ succ (a) = succ a
	rw add_zero,

	refl,
end
