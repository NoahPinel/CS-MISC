lemma add_squared (a b : mynat) : 
	(a + b) ^ (2 : mynat) = a ^ (2 : mynat) + b ^ (2 : mynat) + 2 * a * b :=

begin
	rw two_eq_succ_one,
	-- ⊢ (a + b) ^ succ 1 = a ^ succ 1 + b ^ succ 1 + succ 1 * a * b

	rw one_eq_succ_zero,
	-- ⊢ (a + b) ^ succ (succ 0) = a ^ succ (succ 0) + b ^ succ (succ 0) + succ (succ 0) * a * b

	repeat{rw pow_succ},
	-- ⊢ (a + b) ^ 0 * (a + b) * (a + b) = a ^ 0 * a * a + b ^ 0 * b * b + succ (succ 0) * a * b

	repeat{rw pow_zero},
	-- ⊢ 1 * (a + b) * (a + b) = 1 * a * a + 1 * b * b + succ (succ 0) * a * b

	-- ring, Black Magic

	repeat{rw one_mul},
	-- ⊢ (a + b) * (a + b) = a * a + b * b + succ (succ 0) * a * b

	rw add_mul,
	--⊢ a * (a + b) + b * (a + b) = a * a + b * b + succ (succ 0) * a * b

	repeat{rw mul_add},
	-- ⊢ a * a + a * b + (b * a + b * b) = a * a + b * b + succ (succ 0) * a * b

	rw succ_mul,
	-- ⊢ a * a + a * b + (b * a + b * b) = a * a + b * b + (succ 0 * a + a) * b

	rw succ_mul,
	-- ⊢ a * a + a * b + (b * a + b * b) = a * a + b * b + (0 * a + a + a) * b

	rw zero_mul,
	-- ⊢ a * a + a * b + (b * a + b * b) = a * a + b * b + (0 + a + a) * b

	rw zero_add,
	-- ⊢ a * a + a * b + (b * a + b * b) = a * a + b * b + (a + a) * b

	rw add_mul,
	-- ⊢ a * a + a * b + (b * a + b * b) = a * a + b * b + (a * b + a * b)

	simp,
end
