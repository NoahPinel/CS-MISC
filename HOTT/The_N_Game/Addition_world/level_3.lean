begin
	induction b with n hn,
	-- Base Case
	--rw add_zero,
	--rw add_zero,
	--refl,
	-- Or more simply, since this is T by def
	{refl},

	-- HT
	rw add_succ, -- ⊢ succ (succ a + n) = succ (a + succ n)
	rw hn, -- ⊢ succ (succ (a + n)) = succ (a + succ n)
	rw add_succ, -- ⊢ succ (succ (a + n)) = succ (succ (a + n))
	refl,
end
