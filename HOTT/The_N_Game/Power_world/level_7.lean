lemma pow_pow (a m n : mynat) : (a ^ m) ^ n = a ^ (m * n) :=

begin
	induction n with k h,
	refl,

	rw pow_succ, -- ⊢ (a ^ m) ^ k * a ^ m = a ^ (m * succ k)
	rw mul_succ, -- ⊢ (a ^ m) ^ k * a ^ m = a ^ (m * k + m)
	rw pow_add, -- ⊢ (a ^ m) ^ k * a ^ m = a ^ (m * k) * a ^ m
	rw h, -- ⊢ a ^ (m * k) * a ^ m = a ^ (m * k) * a ^ m
	refl,
end
