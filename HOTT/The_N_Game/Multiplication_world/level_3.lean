-- With this done we have now shown that 1 is both a
-- left and right identity!

begin
	rw one_eq_succ_zero, -- Not needed but I like this path better :)
	induction m with k h,
	refl, -- Base case by DEF

	rw mul_succ, -- ⊢ succ 0 * k + succ 0 = succ k
	rw h, -- Just invoke IH
	refl,
end
