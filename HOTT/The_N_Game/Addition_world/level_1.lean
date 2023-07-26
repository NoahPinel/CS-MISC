-- New tactic induction

begin
	-- 2 new goal's BC and H
	induction n with d hd,
	
	-- Solve BC
	rw add_zero,
	refl,

	-- Now we just prove ⊢ 0 + succ d = succ d
	rw add_succ,
	
	-- ⊢ succ (0 + d) = succ d
	rw hd,

	-- ⊢ succ d = succ d
	refl,
end
