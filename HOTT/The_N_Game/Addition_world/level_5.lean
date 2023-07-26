begin
	-- Induction
	induction n with k h,
	-- Base Case
	{rw one_eq_succ_zero,
	refl},

	-- HT
	{rw succ_add,
	rw h,
	refl},

	-- Fast way
	{rw one_eq_succ_zero,
	rw add_succ,
	refl},
end
