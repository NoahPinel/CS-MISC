lemma pow_add (a m n : mynat) : a ^ (m + n) = a ^ m * a ^ n :=

begin
	induction n with k h,
	{rw add_zero,
	rw pow_zero,
	rw mul_one,
	refl}, -- BC

	{rw add_succ, -- ⊢ a ^ succ (m + k) = a ^ m * a ^ succ k
	rw pow_succ, -- ⊢ a ^ (m + k) * a = a ^ m * a ^ succ k
	rw pow_succ, -- ⊢ a ^ (m + k) * a = a ^ m * (a ^ k * a)
	rw h, -- IH
	simp},
end
